import connexion
from copy import deepcopy
from flask import abort, send_from_directory, g
import json
import pandas

from papahana.controllers import controller_helper as utils
# from papahana.controllers import authorization_controller as auth_utils
from papahana.controllers import observation_block_controller_utils as ob_utils

from papahana.models.body import Body  
from papahana.models.body1 import Body1  
from papahana.models.date_schema import DateSchema  
from papahana.models.observation_block import ObservationBlock  
from papahana.models.sem_id_schema import SemIdSchema  
from papahana.models.template_id_schema import TemplateIdSchema  
from papahana.models.template_schema import TemplateSchema  
from papahana import util

# directory used for writing files to return
OUT_DIR = "/tmp"


def ob_get(ob_id):
    """
    Retrieves the general parameters of an OB.
        /obsBlocks

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: ObservationBlock
    """
    print("user", g.user)
    # will return one result,  and throw 404 if not found
    ob = utils.get_by_id(ob_id, 'obCollect')
    ob_utils.check_ob_allowed(ob)

    return ob


def ob_post(body):
    """
    Inserts an observation block.

    :param body: Observation block to be added.
    :type body: dict | bytes

    :rtype: str of new OB ID.
    """
    ob_utils.check_ob_allowed(body)
    result = utils.insert_into_collection(body, 'obCollect')

    return str(result)


def ob_put(body, ob_id):
    """
    Updates the observation block with the new one.

    :param body: Observation block replacing ob_id.
    :type body: dict | bytes
    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    # check that access is allowed to the ob being replaced.
    ob_utils.check_ob_id_allowed(ob_id)

    utils.update_doc(utils.query_by_id(ob_id), body, 'obCollect', clear=True)


def ob_delete(ob_id):
    """
    Removes the observation block

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    # check that access is allowed to the ob being replaced.
    ob_utils.check_ob_id_allowed(ob_id)

    utils.delete_by_id(ob_id, 'obCollect')


def ob_duplicate(ob_id, sem_id=None):
    """
    Duplicate the OB, default is current semId.

    :param ob_id: observation block id
    :type ob_id: str
    :param sem_id: program id including semester
    :type sem_id: str

    :rtype: str
    """
    ob = utils.get_by_id(ob_id, 'obCollect', cln_oid=False)
    ob_utils.check_ob_allowed(ob)

    del ob['_id']

    if sem_id:
        ob['metadata']['sem_id'] = sem_id

    result = utils.insert_into_collection(ob, 'obCollect')

    return str(result)


def ob_executions(ob_id): 
    """
    Retrieves the list of execution attempts for a specific OB.

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: List[str]
    """
    ob = utils.get_by_id(ob_id, 'obCollect', cln_oid=False)

    if "status" not in ob or "executions" not in ob["status"]:
        return []

    return ob["status"]["executions"]


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
    fields = {"observations": 1, "_id": 0, "status": 1}
    ob_info = utils.get_fields_by_id(ob_id, fields, 'obCollect')

    if not ob_info or 'observations' not in ob_info:
        return 0.0

    # The OB either has a state of Complete=3 or aborted=4.
    if ob_info['status']['state'] >= 3:
        return 0.0

    # take into account what sequences have been completed
    current_seq = ob_info['status']['current_seq']

    total_tm = 0.0
    for obs in ob_info['observations']:
        ob_seq = obs['metadata']['sequence_number']

        if ob_seq >= current_seq:
            # takes into account the step and exposure number
            total_tm += ob_utils.calc_dither_time(obs)

    # return time in minutes
    total_tm /= 60.0

    return total_tm


#TODO this is only retrieving the OB -- does it need more?
def ob_export(ob_id):
    """
    Exports an OB in human-readable format. 
        /obsBlocks/export

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: ObservationBlock
    """
    return utils.get_by_id(ob_id, 'obCollect')


def ob_sequence_filled(ob_id):
    """
    Verify that the required parameters have been filled in.
        /obsBlocks/completelyFilledIn

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: bool
    """
    fields = {"parameters": 1, "_id": 0}
    observations = ob_sequences_get(ob_id)

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


def ob_sequences_get(ob_id):
    """
    Retrieves the list of sequences associated with the OB
        /obsBlocks/sequences

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: List[Observation]
    """
    fields = {"_id": 0, "observations": 1, "acquisition": 1}
    ob_sequences = utils.get_fields_by_id(ob_id, fields, 'obCollect')

    sequence_list = []
    if "acquisition" in ob_sequences:
        sequence_list.append(ob_sequences["acquisition"])

    if "observations" in ob_sequences:
        for seq in ob_sequences["observations"]:
            sequence_list.append(seq)

    return sequence_list


def ob_sequence_id_get(ob_id, sequence_number):
    """
    Retrieves the specified sequence within the OB
        /obsBlocks/sequence/id

    :param ob_id: observation block id
    :type ob_id: str
    :param sequence_number: index of template within the OB, seq0, acq0.
    :type sequence_number: str

    :rtype: Template
    """
    fields = {"_id": 0, "observations": 1, "acquisition": 1}
    ob_sequences = utils.get_fields_by_id(ob_id, fields, 'obCollect')

    sequence = ob_utils.get_sequence(ob_sequences, sequence_number)

    return sequence


def ob_sequence_id_put(body, ob_id, sequence_number):
    """
    Updates the specified template within the OB
        /obsBlocks/sequence/id

    :param body:
    :type body: dict | bytes
    :param ob_id: observation block id
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

    :param ob_id: observation block id
    :type ob_id: str
    :param sequence_number: index and type of template within the OB.
    :type sequence_number: str

    :rtype: None
    """
    ob = ob_get(ob_id)
    observations = utils.get_sequence(ob, sequence_number)

    if obs_type not in ob:
        return

    # this is assumed to be an acquisition
    if type(observations) is not list:
        del ob[obs_type]
    else:
        n_obs = len(observations)
        if n_obs <= 1:
            abort(400, "Not allowed to delete the last observation template.")
        elif n_obs < obs_indx:
            return
        del observations[obs_indx]

        for cnt in range(0, len(observations)):
            observations[cnt]['sequence_number'] = f'{obs_type[:3]}{cnt}'

        ob[obs_type] = observations

    utils.update_doc(utils.query_by_id(ob_id), ob, 'obCollect')


#TODO come back to types other then json
#TODO think through cleanup
def ob_sequence_id_file_get(ob_id, sequence_number, file_parameter):
    """
    Returns the specified template within the OB as a file

    :param ob_id: observation block id
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
def ob_sequence_id_file_put(body, ob_id, sequence_number, file_parameter):
    """
    Updates the specified template within the OB
        /obsBlocks/sequence/{sequence_number}/{file_parameter}

    :param ob_id: observation block id
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
        /obsBlocks/sequence/duplicate/{sequence_number}

    :param ob_id: observation block id
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

    #todo this isn't right anymore
    new_sequence['template_index'] = f'seq{len(observations)}'

    observations.append(new_sequence)
    utils.update_doc(utils.query_by_id(ob_id), {"sequences": observations},
                     'obCollect')

    return new_sequence


def ob_sequence_post(body, ob_id, obs_type):
    """
    Creates the list of observations associated with the OB

    :param body:
    :type body: list or dict
    :param ob_id: observation block id
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
    :param ob_id: observation block id
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

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: List[str]
    """
    fields = {"time_constraints": 1}
    results = utils.get_fields_by_id(ob_id, fields, 'obCollect')
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
    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    if not isinstance(body, list):
        abort(400, 'Invalid input type -- time constraints must be an array.')

    utils.update_doc(utils.query_by_id(ob_id), {"time_constraints": body},
                     'obCollect')


def ob_upgrade(ob_id, sem_id=None):
    """
    When an instrument package changes, attempts to port an existing OB
    to the new package, default is the current semId.

    :param ob_id: observation block ObjectId
    :type ob_id: str
    :param sem_id: program id including semester
    :type sem_id: dict | bytes

    :rtype: ObservationBlock
    """
    if connexion.request.is_json:
        sem_id = SemIdSchema.from_dict(connexion.request.get_json())

    return 'do some magic!'


def ob_schedule_put(ob_id):  
    """
    On success updates an existing ob schedule.

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """

    #TODO need schedule  in db

    return 'do some magic!'


def ob_schedule_get(ob_id):  
    """
    Retrieves scheduling information. 

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: List[str]
    """

    return 'Need schedule information in db'


def ob_sequence_supplement(ob_id):
    """
    Retrieves list of files.

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    return 'do some magic!'

def ob_last_version(ob_id):  # noqa: E501
    """ob_last_version

    Retrieves the last saved version an OB. # noqa: E501

    :param ob_id: observation block ObjectId
    :type ob_id: str

    :rtype: ObservationBlock
    """
    return 'do some magic!'

def ob_revisions(ob_id, revision_n=None):  # noqa: E501
    """ob_revisions

    Retrieves the last ten revisions,  unless the number of revisions is specified # noqa: E501

    :param ob_id: observation block ObjectId
    :type ob_id: str
    :param revision_n: The number of revisions to return
    :type revision_n: int

    :rtype: ObservationBlock
    """
    return 'do some magic!'

def ob_revision_index(ob_id, revision_index):  # noqa: E501
    """ob_revision_index

    Retrieves the nth (revision_index) revision # noqa: E501

    :param ob_id: observation block ObjectId
    :type ob_id: str
    :param revision_index: The index of the single revision to return.
    :type revision_index: int

    :rtype: ObservationBlock
    """
    return 'do some magic!'


