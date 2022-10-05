import connexion
from copy import deepcopy
from flask import abort, send_from_directory
import json
import pandas

from papahana.controllers import controller_helper as utils
from papahana.controllers import observation_block_utils as ob_utils
from papahana.controllers import authorization_utils as auth_utils

from papahana.models.observation_block import ObservationBlock
from papahana.models.sem_id_schema import SemIdSchema
from papahana.models.status_subset import StatusSubset

from papahana.util import config_collection


# directory used for writing files to return
OUT_DIR = "/tmp"


def ob_get(ob_id, return_with_tagid=False):
    """
    Retrieves the most recent version of an OB.
        /obsBlocks

    :param ob_id: observation block Object ID
    :type ob_id: str

    :rtype: ObservationBlock
    """
    # will return one result,  and throw 422 if not found
    ob_orig = ob_utils.ob_id_associated(ob_id)

    # get latest version
    ob = ob_utils.ob_get(ob_orig['_ob_id'])

    if not return_with_tagid:
        ob['metadata']['tags'] = ob_orig['metadata']['tags']

    return utils.json_with_objectid(ob)


def ob_post(body):
    """
    Inserts an observation block.

    :param body: Observation block to be added.
    :type body: dict | bytes

    :rtype: str of new OB ID.
    """
    auth_utils.check_sem_id_associated(body['metadata']['sem_id'])
    if connexion.request.is_json:
        # check that status is complete,  add defaults
        body = ob_utils.add_default_status(body, connexion.request.get_json())

    # the id will be generated on inserting
    if '_ob_id' in body:
        del body['_ob_id']

    result = ob_utils.insert_ob(body)

    return str(result)


def ob_put(body, ob_id):
    """
    Updates the observation block with the new one.

    :param body: Observation block replacing OB with Object ID = ob_id.
    :type body: dict | bytes
    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    # check that access is allowed to the ob being replaced,  422 if not found.
    ob_orig = ob_get(ob_id, return_with_tagid=True)

    # add the id required by history
    body['_ob_id'] = ob_orig['_ob_id']
    body['metadata']['sem_id'] = ob_orig['metadata']['sem_id']

    if connexion.request.is_json:
        body = ob_utils.add_default_status(body, connexion.request.get_json())

    utils.update_doc(utils.query_by_id(ob_id), body, 'obCollect', clear=True)


def ob_delete(ob_id):
    """
    Removes the observation block

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    # check that access is allowed to be deleted,  422 if not found.
    _ = ob_utils.ob_id_associated(ob_id)

    # mark deleted in the original OB document since this is a status field
    new_vals = {'status.deleted': True}
    _ = utils.update_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')


def ob_duplicate(ob_id, sem_id=None):
    """
    Duplicate the OB, default is current semId.

    :param ob_id: observation block id
    :type ob_id: str
    :param sem_id: program id including semester
    :type sem_id: str

    :rtype: str
    """
    # check that access is allowed and get ob,  422 if not found
    ob_orig = ob_utils.ob_id_associated(ob_id)

    # remove IDs
    del ob_orig['_id']
    del ob_orig['_ob_id']

    # check the sem_id is associated
    if sem_id:
        ob_orig['metadata']['sem_id'] = sem_id
        auth_utils.check_sem_id_associated(sem_id)

    result = ob_utils.insert_ob(ob_orig)

    return utils.json_with_objectid(result)


# routes for the completion status
def ob_status_get(ob_id, status_field=None):  
    """
    retrieve the completion status of the observation block.  Optionally
    a field can be added to return only a subset of the status.

        /obsBlocks/status

    :param ob_id: observation block ObjectId
    :type ob_id: str
    :param status_field: The completion status field to update
    :type status_field: str

    :rtype: StatusSubset
    """
    if status_field:
        fields = {f'status.{status_field}': 1, '_id': 0}
    else:
        fields = {'status': 1, '_id': 0}
    results = utils.get_fields_by_id(ob_id, fields, 'obCollect')

    if not results:
        return {}

    return results


def ob_status_update(ob_id, status_field, new_status):
    """
    update the status of the observation block.  It is meant to be used by
    the execution engine to record the completion status of the Observation Block.
        /obsBlocks/status/{status_field}/update

    :param ob_id: observation block ObjectId
    :type ob_id: str
    :param new_status: The completion status field to update
    :type new_status: str

    :rtype: StatusSubset
    """

    query = utils.query_by_id(ob_id)
    new_vals = {f'status.{status_field}': new_status}
    result = utils.update_doc(query, new_vals, 'obCollect')

    return ob_status_get(ob_id, status_field=status_field)


def ob_previous_version(ob_id):
    """
    Retrieves the last saved version an OB.
        /obsBlocks/previousVersion

    :param ob_id: observation block Object ID string
    :type ob_id: str

    :rtype: ObservationBlock
    """

    revisions = ob_revisions(ob_id, revision_n=2)
    if not revisions:
        return {}

    if len(revisions) > 1:
        prev_version = revisions[-2]
    else:
        prev_version = revisions[-1]

    prev_version = ob_utils.clean_revision_metadata(prev_version)

    return prev_version


def ob_revisions(ob_id, revision_n=None):
    """
    Retrieves the last ten revisions,  unless the number of revisions
    is specified
        /obsBlocks/revisions

    :param ob_id: observation block Object ID string
    :type ob_id: str
    :param revision_n: The number of revisions to return
    :type revision_n: int

    :rtype: ObservationBlock
    """
    if not revision_n:
        revision_n = 10

    # returns ordered list of full OB 0 = original 1,2, .. = later revisions

    ob = ob_get(ob_id)
    _ob_id = ob['_ob_id']

    coll = config_collection('obCollect')

    revisions = list(coll.revisions({'_ob_id': _ob_id}))

    return utils.list_with_objectid(revisions[-revision_n:])


def ob_revision_index(ob_id, revision_index):
    """ob_revision_index

    Retrieves the nth (revision_index) revision

    :param ob_id: observation block Object ID string
    :type ob_id: str
    :param revision_index: The index of the single revision to return.
    :type revision_index: int

    :rtype: ObservationBlock
    """
    revision_list = ob_revisions(ob_id, revision_n=revision_index)

    return revision_list[-1]


def ob_executions(ob_id):
    """
    Retrieves the list of execution attempts for a specific OB.
        /obsBlocks/executions

    :param ob_id: observation block Object ID str
    :type ob_id: str

    :rtype: List[str]
    """
    # get and check access is allowed
    ob = ob_get(ob_id)

    ob_obj = ObservationBlock.from_dict(ob)
    if not ob_obj.status or not ob_obj.status.executions:
        return []

    ob_obj = ObservationBlock.from_dict(ob)

    return ob_obj.status.executions


def ob_execution_time(ob_id):
    """
    Calculates the execution time.  Only uncompleted sequence steps are
    used in the calculation.  If the OB is Aborted or Complete,  it will
    return 0.
        /obsBlocks/executionTime

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: float
    """
    # get and check access is allowed
    ob = ob_get(ob_id)

    ob_obj = ObservationBlock.from_dict(ob)
    if not ob_obj.status:
        return 0.0

    if ob_obj.status.state >= 3:
        return 0.0

    current_seq = ob_obj.status.current_seq
    total_tm = 0.0
    for obs in ob_obj.observations:
        ob_seq = obs['metadata']['sequence_number']

        if ob_seq >= current_seq:
            # takes into account the step and exposure number
            total_tm += ob_utils.calc_dither_time(obs)

    # return time in minutes
    total_tm /= 60.0

    return total_tm


def ob_completely_filled(ob_id):
    """
    Verify that the required parameters have been filled in.
        /obsBlocks/completelyFilledIn

    :param ob_id: observation block Object ID string
    :type ob_id: str

    :rtype: bool
    """
    fields = {"parameters": 1, "_id": 0}
    observations = ob_observations_get(ob_id)

    for filled in observations:
        if filled.keys() < {"metadata", "parameters"}:
            abort(422, "The Observation Block Template is missing the keys: "
                       "metadata or parameters.")

        metadata = filled["metadata"]
        if metadata.keys() < {"name", "ui_name", "instrument", "type",
                              "version", "script"}:
            abort(422, "The Observation Block Template is missing one"
                       "of the metadata keys.")

        query = {"metadata.name": metadata['name'],
                 "metadata.version": metadata['version']}

        template = utils.get_fields_by_query(query, fields, 'templateCollect')
        if not template:
            abort(422, f"No template found with name {metadata['name']} "
                       f"and version {metadata['version']}.")

        if not utils.check_required_values(template[0]['parameters'],
                                           filled['parameters']):
            return False

    return True


def ob_observations_get(ob_id):
    """
    Retrieves the list of observation sequences associated with the OB
        /obsBlocks/observations

    :param ob_id: observation block Object ID string
    :type ob_id: str

    :rtype: List[Observation]
    """
    fields = {"_id": 0, "observations": 1, "acquisition": 1,
              'metadata.sem_id': 1}
    obs = utils.get_fields_by_id(ob_id, fields, 'obCollect')

    if not obs:
        return []

    # check the OB is associated
    auth_utils.check_sem_id_associated(obs['metadata']['sem_id'])

    sequence_list = []
    if "acquisition" in obs:
        sequence_list.append(obs["acquisition"])

    if "observations" in obs:
        for seq in obs["observations"]:
            sequence_list.append(seq)

    return sequence_list


def ob_observations_id_get(ob_id, sequence_number):
    """
    Retrieves the specified observation sequence within the OB
        /obsBlocks/observations/id

    :param ob_id: observation block Object ID string
    :type ob_id: str
    :param sequence_number: index of template within the OB, seq0, acq0.
    :type sequence_number: str

    :rtype: Template
    """
    fields = {"_id": 0, "observations": 1, "acquisition": 1, "metadata.sem_id": 1}
    observations = utils.get_fields_by_id(ob_id, fields, 'obCollect')

    # check the OB is associated
    auth_utils.check_sem_id_associated(observations['metadata']['sem_id'])

    sequence = ob_utils.get_sequence(observations, sequence_number)

    return sequence


def ob_sequence_id_put(body, ob_id, sequence_number):
    """
    Updates the specified template within the OB
        /obsBlocks/sequence/id

    :param body:
    :type body: dict | bytes
    :param ob_id: observation block Object ID string
    :type ob_id: str
    :param sequence_number: index and type of template within the OB.
    :type sequence_number: str

    :rtype: None
    """
    ob = ob_get(ob_id)
    observations = ob_utils.get_sequence(ob, sequence_number, return_all=True)

    if not observations:
        return

    # observations will be a list,  and acquisition is not
    if type(observations) is list:
        body['metadata']['sequence_number'] = sequence_number

        obs_type = 'observations'
        obs_indx = 0
        for indx, obs in enumerate(observations):
            if obs['metadata']['sequence_number'] == sequence_number:
                obs_indx = indx
                break

        observations[obs_indx] = body
    else:
        obs_type = 'acquisition'
        observations = body

    new_vals = {obs_type: observations}
    utils.update_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')


#TODO COME BACK -- nothing below here updated 20220322

#TODO open question -- currently does not allow deleting the last observation.
def ob_sequence_id_delete(ob_id, sequence_number):
    """
    Removes the specified template within the OB

    :param ob_id: observation block Object ID string
    :type ob_id: str
    :param sequence_number: index and type of template within the OB.
    :type sequence_number: str

    :rtype: None
    """
    # check association and get ob
    ob = ob_get(ob_id)
    ob_obj = ObservationBlock.from_dict(ob)

    # observations

    # if 'obs_type' not in ob:
    #     return
    #
    # # this is assumed to be an acquisition
    # if type(observations) is not list:
    #     del ob[obs_type]
    # else:
    #     n_obs = len(observations)
    #     if n_obs <= 1:
    #         abort(400, "Not allowed to delete the last observation template.")
    #     elif n_obs < obs_indx:
    #         return
    #     del observations[obs_indx]
    #
    #     for cnt in range(0, len(observations)):
    #         observations[cnt]['sequence_number'] = f'{obs_type[:3]}{cnt}'
    #
    #     ob[obs_type] = observations
    #
    # utils.update_doc(utils.query_by_id(ob_id), ob, 'obCollect')


#TODO come back to types other then json
def ob_sequence_id_get(ob_id, sequence_number, file_parameter):
    """
    Returns the specified template within the OB as a file

    :param ob_id: observation block Object ID string
    :type ob_id: str
    :param sequence_number: index and type of template within the OB.
    :type sequence_number: str
    :param file_parameter: file paramter description here
    :type file_parameter: str

    :rtype: file
    """
    template = ob_sequence_id_get(ob_id, sequence_number)
    docs = pandas.DataFrame(template)
    filename = f"{ob_id}.{file_parameter}"
    output = f"{OUT_DIR}/{filename}"

    if file_parameter == 'json':
        ob_utils.write_json(template, output)
    else:
        file_writer = {'json': docs.to_json, 'csv': docs.to_csv,
                       'html': docs.to_html, 'txt': docs.to_string}
        file_writer[file_parameter](output)

    return send_from_directory(OUT_DIR, f'{ob_id}.{file_parameter}',
                               as_attachment=True)


#TODO currently only working with JSON
def ob_sequence_id_put(body, ob_id, sequence_number, file_parameter):
    """
    Updates the specified template within the OB
        /obsBlocks/sequence/{sequence_number}/{file_parameter}

    :param ob_id: observation block Object ID string
    :type ob_id: str
    :param sequence_number: index and type of template within the OB.
    :type sequence_number: str
    :param file_parameter: file parameter description here
    :type file_parameter: str

    :rtype: None
    """
    json_data = json.loads(body.decode('ascii'))

    ob_sequence_id_put(json_data, ob_id, sequence_number)


def ob_sequence_duplicate(ob_id, sequence_number):
    """
    Generate a new copy of the template and add it to the list of templates in
    the OB.
        /obsBlocks/sequence/duplicate

    :param ob_id: observation block Object ID string
    :type ob_id: str
    :param sequence_number: index and type of template within the OB.
    :type sequence_number: str

    :rtype: Observation
    """
    if sequence_number == 0:
        abort(400, f'Invalid sequence_number: {sequence_number}, currently '
                   f'duplicating acquisition sequence is NOT supported.')

    ob = ob_get(ob_id)

    # TODO return the template number
    observation = ob_utils.get_sequence(ob, sequence_number)

    new_template = deepcopy(observation)

    # #todo this isn't right anymore
    # new_sequence['template_index'] = f'seq{len(observations)}'
    #
    # observations.append(new_sequence)
    # utils.update_doc(utils.query_by_id(ob_id), {"sequences": observations},
    #                  'obCollect')
    #
    # return new_sequence


def ob_sequence_post(body, ob_id, obs_type):
    """
    Creates the list of observations associated with the OB

    :param body:
    :type body: list or dict
    :param ob_id: observation block Object ID string
    :type ob_id: str
    :param obs_type: A string to indicate the type of template,
                          (acquisition, science, engineering, calibration)
    :type obs_type: str

    :rtype: None
    """
    if type(body) is not list:
        body = [body]

    new_vals = {obs_type: body}

    utils.update_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')


def ob_sequence_put(body, ob_id, obs_type):
    """
    Updates the list of observations associated with the OB

    :param body:
    :type body: dict | bytes
    :param ob_id: observation block Object ID string
    :type ob_id: str
    :param obs_type: A string to indicate the type of template,
                          (acquisition, science, engineering, calibration)
    :type obs_type: str

    :rtype: None
    """
    if type(body) is list:
        for val in body:
            new_vals = {obs_type: val}
            utils.update_add_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')
    else:
        new_vals = {obs_type: body}
        utils.update_add_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')


def ob_time_constraint_get(ob_id):
    """
    Retrieves the time constraints (from, to).

    :param ob_id: observation block Object ID string
    :type ob_id: str

    :rtype: List[str]
    """
    fields = {"time_constraints": 1, "metadata.sem_id": 1}
    results = utils.get_fields_by_id(ob_id, fields, 'obCollect')

    # check the OB is associated
    auth_utils.check_sem_id_associated(results['metadata']['sem_id'])

    if not results:
        abort(422, f'Observation block id not found')

    if 'time_constraints' not in results:
        return []

    return results['time_constraints']


def ob_time_constraint_put(body, ob_id):
    """
    Create / replace the time constraints (from, to).

    :param body:
    :type body: list
    :param ob_id: observation block Object ID string
    :type ob_id: str

    :rtype: None
    """
    if not isinstance(body, list):
        abort(400, 'Invalid input type -- time constraints must be an array.')

    # check that access is allowed to the ob being replaced.
    ob = ob_get(ob_id)
    if not ob:
        abort(422, f'Observation Block id: {ob_id} not found.')

    utils.update_doc(utils.query_by_id(ob_id), {"time_constraints": body},
                     'obCollect')


def ob_upgrade(ob_id, sem_id=None):
    """
    When an instrument package changes, attempts to port an existing OB
    to the new package, default is the current sem_id.

    :param ob_id: observation block Object ID string
    :type ob_id: str
    :param sem_id: program id including semester
    :type sem_id: dict | bytes

    :rtype: ObservationBlock
    """
    if connexion.request.is_json:
        sem_id = SemIdSchema.from_dict(connexion.request.get_json())

    # check that access is allowed to the ob being replaced.
    ob = ob_get(ob_id)
    if not ob:
        abort(422, f'Observation Block id: {ob_id} not found.')

    if not sem_id:
        sem_id = ob['metadata']['sem_id']

    # check the OB is associated
    auth_utils.check_sem_id_associated(sem_id)

    # TODO find the new package,  port,  etc

    return 'do some magic!'


def ob_schedule_put(ob_id):  
    """
    On success updates an existing ob schedule.

    :param ob_id: observation block Object ID string
    :type ob_id: str

    :rtype: None
    """

    #TODO need schedule  in db

    return 'do some magic!'


def ob_schedule_get(ob_id):  
    """
    Retrieves scheduling information. 

    :param ob_id: observation block Object ID string
    :type ob_id: str

    :rtype: List[str]
    """

    return 'Need schedule information in db'


def ob_sequence_supplement(ob_id):
    """
    Retrieves list of files.

    :param ob_id: observation block Object ID string
    :type ob_id: str

    :rtype: None
    """
    return 'do some magic!'


