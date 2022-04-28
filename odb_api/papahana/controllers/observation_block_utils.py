from datetime import datetime
from flask import abort, g
import json
import ast
import pymongo

from papahana.util import config_collection

from papahana.controllers import controller_helper as utils
from papahana.controllers import authorization_utils as auth_utils
from papahana.models.observation_block import ObservationBlock
from papahana.models.status import Status


def update_ob(_ob_id, new_ob):
    metadata = {"timestamp": datetime.now()}
    coll = config_collection('obCollect')

    coll.patch_one(new_ob, metadata=metadata)


def ob_get(_ob_id):
    coll = config_collection('obCollect')

    ob = coll.latest({'_ob_id': _ob_id})

    if not ob:
        abort(422, f'No results in: Observation Block collections.')

    ob = clean_revision_metadata(ob)

    return ob


def clean_revision_metadata(ob):
    try:
        del ob['_revision_metadata']
    except KeyError:
        pass

    return ob


def ob_id_associated(ob_id):
    """
    Minimally check that the OB can be viewed by the user logged in.  The
    returned OB is the original OB,  not the most recent.
    """
    # will return one result,  and throw 422 if not found
    ob = utils.get_by_id(ob_id, 'obCollect')
    auth_utils.check_sem_id_associated(ob['metadata']['sem_id'])

    return ob


def insert_ob(ob_doc):
    """
    Add a new document to a collection.
    :param ob_doc: the document to insert
    :type ob_doc: dict
    rtype: document id
    """
    coll = config_collection('obCollect')

    # generate the _ob_id -- don't allow it to be inserted manually
    sem_id = ob_doc['metadata']['sem_id']
    n_ob = coll.count_documents({'metadata.sem_id': sem_id}) + 1
    ob_doc['_ob_id'] = f"{sem_id}_{str(n_ob).zfill(4)}"

    metadata = {"timestamp": datetime.now()}
    result = coll.patch_one(ob_doc, metadata=metadata)

    return result.inserted_id_obj.inserted_id


def calc_exp_time(obs):
    """
    calculate the total time to execute all observing blocks by exp. time.
    Excludes any read out time and overheads.

    :param obs: The observing Block document.
    :type obs: Dict

    :rtype: int
    """
    if "parameters" not in obs:
        return 0

    # take into account what steps have been completed (0-based)]
    cur_det1_step = 0
    cur_det2_step = 0
    try:
        cur_det1_step -= obs['metadata']['current_step']
    except KeyError:
        pass
    try:
        cur_det2_step -= obs['metadata']['current_step']
    except KeyError:
        pass

    exp1 = 0
    exp2 = 0
    seq_blk = obs["parameters"]
    try:
        n_exp_remain = seq_blk['det1_exp_number'] - cur_det1_step
        exp1 = seq_blk['det1_exp_time'] * n_exp_remain
    except KeyError:
        exp1 = 0

    if seq_blk.keys() >= {"det1_exp_time", "det2_exp_time",
                          "det1_exp_number", "det2_exp_number"}:

        try:
            n_exp_remain = seq_blk['det2_exp_number'] - cur_det2_step
            exp2 = seq_blk['det2_exp_time'] * n_exp_remain
        except KeyError:
            exp2 = 0

    return max(exp1, exp2)


def calc_dither_time(obs):
    """
    calculate the total time to execute all observing blocks by exp. time.
    Excludes any read out time and overheads.

    :param obs: The observing Block document.
    :type obs: Dict

    :rtype: int
    """
    if "parameters" not in obs:
        return 0

    max_exp = calc_exp_time(obs)
    seq_blk = obs["parameters"]

    if 'seq_dither_number' in seq_blk:
        n_offsets = seq_blk['seq_dither_number']
    else:
        n_offsets = 1

    # take into account what steps have been completed (0-based)
    try:
        n_offsets -= obs['metadata']['current_step']
    except KeyError:
        pass

    return max_exp * n_offsets


def get_sequence(sequences, sequence_number, return_all=False):
    """
    returns a single sequence matching the sequence_number.

    Acquisitions always have sequence_number = 0,  observations > 0
    """
    if sequence_number < 1:
        seq_type = 'acquisition'
    else:
        seq_type = 'observations'

    msg = f"Sequence of type: {seq_type}, and index {sequence_number} does not exist."
    if (seq_type not in sequences or
            sequence_number > len(sequences[seq_type])):
        abort(422, msg)

    if seq_type == 'acquisition' or return_all:
        return sequences[seq_type]
    else:
        for seq in sequences[seq_type]:
            if seq['metadata']['sequence_number'] == sequence_number:
                return seq

    return {}


def write_json(dict_data, output):
    with open(output, 'w') as fp:
        json.dump(dict_data, fp)

    fp.close()


def check_ob_id_allowed(ob_id):
    ob = utils.get_by_id(ob_id, 'obCollect')
    check_ob_allowed(ob)


def check_ob_allowed(ob):
    sem_id = ob['metadata']['sem_id']
    if not auth_utils.is_authorized_semid(sem_id):
        abort(401, f'Observer with Keck ID {g.user} is not authorized to access'
                   f' OB - the semester ID does not match allowed programs.')


def add_default_status(body, json_body):
    ob_obj = ObservationBlock.from_dict(json_body)
    if not ob_obj.status:
        body['status'] = ast.literal_eval(str(Status()).replace("\n", ""))

    return body

