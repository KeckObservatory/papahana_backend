import connexion
from copy import deepcopy
from flask import abort, send_from_directory
import json
import pandas

from papahana.controllers import controller_helper as utils

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

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: ObservationBlock
    """
    return utils.get_by_id(ob_id, 'obCollect')


def ob_post(body):
    """
    Inserts an observation block.

    :param body: Observation block to be added.
    :type body: dict | bytes

    :rtype: str of new OB ID.
    """
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
    utils.update_doc(utils.query_by_id(ob_id), body, 'obCollect', clear=True)


def ob_delete(ob_id):
    """
    Removes the observation block

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
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


#TODO should this only be the remaining execution time
def ob_execution_time(ob_id):
    """
    Calculates the execution time.

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: float
    """
    fields = {"sequences.parameters": 1, "_id": 0}
    ob_seq = utils.get_fields_by_id(ob_id, fields, 'obCollect')

    if not ob_seq or 'sequences' not in ob_seq:
        return 0

    total_tm = 0
    for block in ob_seq['sequences']:
        total_tm += utils.calc_exec_time(block)

    return total_tm


#TODO this is only retrieving the OB
def ob_export(ob_id):
    """
    Exports an OB in human-readable format. 

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: ObservationBlock
    """
    return utils.get_by_id(ob_id, 'obCollect')


def ob_template_filled(ob_id):
    """
    Verify that the required parameters have been filled in.

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: bool
    """
    fields = {"parameters": 1, "_id": 0}
    templates = ob_templates_get(ob_id)

    for filled in templates:
        if filled.keys() < {"metadata", "parameters"}:
            abort(422, "The Observation Block Template is missing the keys: "
                       "metadata or parameters.")

        metadata = filled["metadata"]
        if metadata.keys() < {"name", "ui_name", "instrument", "template_type",
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


def ob_templates_get(ob_id):
    """
    Retrieves the list of templates associated with the OB

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: List[Observation]
    """
    fields = {"_id": 0, "sequences": 1, "acquisition": 1}
    ob_templates = utils.get_fields_by_id(ob_id, fields, 'obCollect')

    template_list = []
    if "acquisition" in ob_templates:
        template_list.append(ob_templates["acquisition"])

    if "sequences" in ob_templates:
        for seq in ob_templates["sequences"]:
            template_list.append(seq)

    return template_list


def ob_template_id_get(ob_id, template_id):
    """
    Retrieves the specified template within the OB

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index of template within the OB, seq0, acq0.
    :type template_id: str

    :rtype: Template
    """
    ob = ob_get(ob_id)
    template_indx, template_type = utils.template_indx_type(template_id)
    templates = utils.get_templates(ob, template_type, template_indx)

    if type(templates) is not list:
        return ob[template_type]
    else:
        return templates[template_indx]


def ob_template_id_put(body, ob_id, template_id):
    """
    Updates the specified template within the OB

    :param body:
    :type body: dict | bytes
    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index and type of template within the OB.
    :type template_id: str

    :rtype: None
    """
    ob = ob_get(ob_id)
    template_indx, template_type = utils.template_indx_type(template_id)
    templates = utils.get_templates(ob, template_type, template_indx)

    if type(templates) is list:
        body['template_index'] = template_id
        templates[template_indx] = body
    else:
        templates = body

    new_vals = {template_type: templates}
    utils.update_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')


#TODO open question -- currently does not allow deleting the last observation.
def ob_template_id_delete(ob_id, template_id):
    """
    Removes the specified template within the OB

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index and type of template within the OB.
    :type template_id: str

    :rtype: None
    """
    ob = ob_get(ob_id)
    template_indx, template_type = utils.template_indx_type(template_id)
    templates = utils.get_templates(ob, template_type, template_indx)

    if template_type not in ob:
        return

    # this is assumed to be an acquisition
    if type(templates) is not list:
        del ob[template_type]
    else:
        n_templates = len(templates)
        if n_templates <= 1:
            abort(400, "Not allowed to delete the last observation template.")
        elif n_templates < template_indx:
            return
        del templates[template_indx]

        for cnt in range(0, len(templates)):
            templates[cnt]['template_id'] = f'{template_type[:3]}{cnt}'

        ob[template_type] = templates

    utils.update_doc(utils.query_by_id(ob_id), ob, 'obCollect')


#TODO come back to types other then json
#TODO think through cleanup
def ob_template_id_file_get(ob_id, template_id, file_parameter):
    """
    Returns the specified template within the OB as a file

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index and type of template within the OB.
    :type template_id: str
    :param file_parameter: file paramter description here
    :type file_parameter: str

    :rtype: file
    """
    template = ob_template_id_get(ob_id, template_id)
    docs = pandas.DataFrame(template)
    filename = f"{ob_id}.{file_parameter}"
    output = f"{OUT_DIR}/{filename}"

    if file_parameter == 'json':
        utils.write_json(template, output)
    else:
        file_writer = {'json': docs.to_json, 'csv': docs.to_csv,
                       'html': docs.to_html, 'txt': docs.to_string}
        file_writer[file_parameter](output)

    return send_from_directory(OUT_DIR, f'{ob_id}.{file_parameter}',
                               as_attachment=True)


#TODO currently only working with JSON
def ob_template_id_file_put(body, ob_id, template_id, file_parameter):
    """
    Updates the specified template within the OB

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index and type of template within the OB.
    :type template_id: str
    :param file_parameter: file parameter description here
    :type file_parameter: str

    :rtype: None
    """
    json_data = json.loads(body.decode('ascii'))

    ob_template_id_put(json_data, ob_id, template_id)


def ob_template_duplicate(ob_id, template_id):
    """
    Generate a new copy of the template and add it to the list of templates in
    the OB.

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index and type of template within the OB.
    :type template_id: str

    :rtype: Observation
    """
    if 'seq' not in template_id:
        abort(400, f'Invalid template_id: {template_id}, currently '
                   f'duplicating acquisition templates is NOT supported.')

    ob = ob_get(ob_id)

    template_indx, templates = utils.get_templates_by_id(ob, template_id)

    new_template = deepcopy(templates[template_indx])

    #todo this isn't right anymore
    new_template['template_index'] = f'seq{len(templates)}'

    templates.append(new_template)
    utils.update_doc(utils.query_by_id(ob_id), {"sequences": templates},
                     'obCollect')

    return new_template


def ob_template_post(body, ob_id, template_type):
    """
    Creates the list of templates associated with the OB

    :param body:
    :type body: list or dict
    :param ob_id: observation block id
    :type ob_id: str
    :param template_type: A string to indicate the type of template,
                          (acquisition, science, engineering, calibration)
    :type template_type: str

    :rtype: None
    """
    if type(body) is not list:
        body = [body]

    new_vals = {template_type: body}

    utils.update_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')


def ob_template_put(body, ob_id, template_type):
    """
    Updates the list of templates associated with the OB

    :param body:
    :type body: dict | bytes
    :param ob_id: observation block id
    :type ob_id: str
    :param template_type: A string to indicate the type of template,
                          (acquisition, science, engineering, calibration)
    :type template_type: str

    :rtype: None
    """
    if type(body) is list:
        for val in body:
            new_vals = {template_type: val}
            utils.update_add_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')
    else:
        new_vals = {template_type: body}
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
        abort(404, f'Observation block id not found')

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


def ob_template_supplement(ob_id):
    """
    Retrieves list of files.

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    return 'do some magic!'
