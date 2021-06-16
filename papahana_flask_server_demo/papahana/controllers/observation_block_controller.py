import connexion
from copy import deepcopy
from flask import abort, send_from_directory
from io import StringIO
import json
import pandas
import io

from papahana.models.observation_block import ObservationBlock
from papahana.models.observation import Observation
from papahana.controllers import controller_helper as utils

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

    curl -v -H "Content-Type: application/json" -X POST -d '{ "signature" : { "name" : "standard stars #8", "pi_id" : 8899, "sem_id" : "2019A_N020", "instrument" : "KCWI" }, "version" : 0.1, "target" : { "name" : "ndli", "ra" : "01 20 39", "dec" : "-41 45 44", "equinox" : 5.271497685479858, "frame" : "vfjw", "ra_offset" : 8.284293063826414, "dec_offset" : 0.526794111139437, "pa" : 9.340237658316866, "pm_ra" : 0.5265900313218896, "pm_dec" : 4.31815072224234, "epoch" : 8.842424493992965, "obstime" : 7.120039595910197, "mag" : [ { "band" : "V", "mag" : 0.5866992315816202 }, { "band" : "K", "mag" : 0.3795908856613399 } ], "wrap" : "south", "d_ra" : 3.833963780902916, "d_dec" : 4.009906121406269, "comment" : "I am one of the few honest people I have ever known." }, "acquisition" : { "name" : "KCWI_ifu_acq_direct", "instrument" : "KCWI", "type" : "acq", "version" : 0.1, "GUIDER_PO" : "IFU", "wrap" : "shortest", "rotmode" : "stationary", "GUIDER_GS_RA" : "14 03 15", "GUIDER_GS_DEC" : "+54 20 43", "GUIDER_GS_MODE" : "User", "index" : 0 }, "science" : [ { "name" : "KCWI_ifu_sci_test", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 1 }, { "name" : "KCWI_ifu_sci_test", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 2 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 3 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 4 } ], "associations" : [ "jpuzq", "ezoas", "ozjto" ], "priority" : 58.26288430222885, "status" : { "state" : "inqueue", "executions" : [ "2019-05-16 11:27:27", "2019-06-25 21:34:27", "2019-10-12 05:41:27", "2020-09-08 21:37:27", "2018-12-22 06:40:27" ] }, "comment" : "Here?s some money. Go see a star war." }' "http://vm-webtools.keck:50001/v0/obsBlocks"

    :param body: Observation block to be added.
    :type body: dict | bytes

    :rtype: str of new OB ID.
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()

    result = utils.insert_into_collection(body, 'obCollect')

    return str(result)


def ob_put(body, ob_id):
    """
    Updates the observation block with the new one
    [webdev@vm-webtools ~]$ curl -v -H "Content-Type: application/json" -X PUT -d '{"signature.instrument": "KCWI-test"}' "http://vm-webtools.keck.hawaii.edu:50000/v0/obsBlocks?ob_id=609c27515ef7b19168a7f646"

    :param body: Observation block replacing ob_id.
    :type body: dict | bytes
    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()

    utils.update_doc(utils.query_by_id(ob_id), body, 'obCollect')


def ob_delete(ob_id):
    """
    Removes the observation block

    curl -v -H "Content-Type: application/json" -X DELETE "http://vm-webtools.keck.hawaii.edu:50001/v0/obsBlocks?ob_id=609c27515ef7b19168a7f646"

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    utils.delete_by_id(ob_id, 'obCollect')


def ob_duplicate(ob_id, sem_id=None):
    """
    Duplicate the OB, default is current semId.

    curl -v -H "Content-Type: application/json" -X POST "http://vm-webtools.keck.hawaii.edu:50001/v0/obsBlocks/duplicate?ob_id=609c27515ef7b19168a7f646"

    :param ob_id: observation block id
    :type ob_id: str
    :param sem_id: program id including semester
    :type sem_id: str

    :rtype: str
    """
    ob = utils.get_by_id(ob_id, 'obCollect', cln_oid=False)

    del ob['_id']

    if sem_id:
        ob['signature']['sem_id'] = sem_id

    result = utils.insert_into_collection(ob, 'obCollect')

    return str(result)


def ob_executions(ob_id): 
    """
    Retrieves the list of execution attempts for a specific OB
    (for a specific night).

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
    http://vm-webtools.keck.hawaii.edu:50001/v0/obsBlocks/executionTime/?ob_id=2

    Calculates the execution time.

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: float
    """
    fields = {"science.parameters": 1, "_id": 0}
    science = utils.get_fields_by_id(ob_id, fields, 'obCollect')

    if not science:
        return

    total_tm = 0
    for block in science:
        total_tm += utils.calc_exec_time(block)

    return total_tm


#TODO this is only retrieving the OB
def ob_export(ob_id):
    """
    http://vm-webtools.keck.hawaii.edu:50001/v0/obsBlocks/export/?ob_id=2

    Exports an OB in human-readable format. # noqa: E501

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
    templates = ob_template_get(ob_id)
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

        if not utils.check_required(template[0]['parameters'],
                                    filled['parameters']):
            return False

    return True


def ob_template_get(ob_id):
    """
    Retrieves the list of templates associated with the OB

    curl -v -H "Content-Type: application/json" -X GET "http://vm-webtools.keck.hawaii.edu:50001/v0/obsBlocks/template/0?ob_id=60adc652e7781dfbc33d2f18"

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: List[Observation]
    """
    ob = ob_get(ob_id)

    template_list = []
    for key in ['acquisition', 'science', 'engineering', 'calibration']:
        if key not in ob:
            continue

        templates = ob[key]
        if type(templates) is list:
            for template in templates:
                template_list.append(template)
        else:
            template_list.append(templates)

    return template_list


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

    if type(templates) is not list:
        del ob[template_type]
    else:
        if len(templates) < template_indx:
            return
        del templates[template_indx]

        for cnt in range(0, len(templates)):
            templates[cnt]['index'] = cnt

        ob[template_type] = templates

    utils.update_doc(utils.query_by_id(ob_id), ob, 'obCollect')


#TODO come back to types other then json
#TODO think through cleanup
def ob_template_id_file_get(ob_id, template_id, file_parameter):
    """
    Retrieves the specified template within the OB

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index and type of template within the OB.
    :type template_id: str
    :param file_parameter: file paramter description here
    :type file_parameter: str

    :rtype: ObservationBlock
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

    curl -X PUT "http://vm-webtools.keck:50001/v0/obsBlocks/template/sci3/json?ob_id=60c8eb93d131fb50a4b06f6f" --upload-file /tmp/60c8eb93d131fb50a4b06f6f.json

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


def ob_template_id_get(ob_id, template_id):
    """
    Retrieves the specified template within the OB

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index of template within the OB, sci0, acq0.
    :type template_id: str

    :rtype: Observation
    """
    ob = ob_get(ob_id)
    template_indx, template_type = utils.template_indx_type(template_id)
    templates = utils.get_templates(ob, template_type, template_indx)

    if type(templates) is not list:
        return ob[template_type]
    else:
        return templates[template_indx]


def ob_template_duplicate(ob_id, template_id):
    """
    Generate a new copy of the template and add it to the list of templates in
    the OB.

    curl -v -H "Content-Type: application/json" -X POST "http://vm-webtools.keck.hawaii.edu:50001/v0/obsBlocks/template/duplicate/1?ob_id=60aec72417469e6111a54d78"

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index and type of template within the OB.
    :type template_id: str

    :rtype: Observation
    """

    if 'sci' not in template_id:
        abort(400, 'Invalid template_id, only duplicating science is supported.')

    ob = ob_get(ob_id)

    template_indx, templates = utils.get_templates_by_id(ob, template_id)

    new_template = deepcopy(templates[template_indx])
    new_template['template_index'] = f'sci{len(templates)}'

    templates.append(new_template)
    utils.update_doc(utils.query_by_id(ob_id), {"science": templates},
                     'obCollect')

    return new_template


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

    if connexion.request.is_json:
        body = json.loads(json.dumps(connexion.request.get_json()))

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


def ob_template_post(body, ob_id, template_type):
    """
    Creates the list of templates associated with the OB

    curl -v -H "Content-Type: application/json" -X POST -d '[ { "name" : "KCWI_ifu_sci_stare", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 1200, "DET1_NEXP" : 2, "DET2_EXPTIME" : 1200, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "index" : 1 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 2 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 3 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 4 } ]' "http://vm-webtools.keck:50001/v0/obsBlocks/template?ob_id=60bab915ddb1146b87136414&template_type=sci"

    :param body:
    :type body: list or dict
    :param ob_id: observation block id
    :type ob_id: str
    :param template_type: A string to indicate the type of template,
                          (acquisition, science, engineering, calibration)
    :type template_type: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = json.loads(json.dumps(connexion.request.get_json()))

    if type(body) is not list:
        body = [body]

    new_vals = {template_type: body}

    utils.update_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')


def ob_template_put(body, ob_id, template_type):
    """
    Updates the list of templates associated with the OB

    curl -v -H "Content-Type: application/json" -X PUT -d '[ { "name" : "KCWI_ifu_sci_stare", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 1200, "DET1_NEXP" : 2, "DET2_EXPTIME" : 1200, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "index" : 1 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 2 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 3 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 4 } ]' "http://vm-webtools.keck:50001/v0/obsBlocks/template?ob_id=60bab915ddb1146b87136414&template_type=sci"

    :param body:
    :type body: dict | bytes
    :param ob_id: observation block id
    :type ob_id: str
    :param template_type: A string to indicate the type of template,
                          (acquisition, science, engineering, calibration)
    :type template_type: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = json.loads(json.dumps(connexion.request.get_json()))

    if type(body) is list:
        for val in body:
            new_vals = {template_type: val}
            utils.update_add_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')
    else:
        new_vals = {template_type: body}
        utils.update_add_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')


def ob_template_supplement(ob_id):
    """
    Retrieves list of files.

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    return 'do some magic!'


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

    curl -v -H "Content-Type: application/json" -X PUT -d '["2021-05-01 08:00:11", "2021-05-01 08:00:22"]' "http://vm-webtools.keck:50001/v0/obsBlocks/timeConstraints?ob_id=60bfddd9ae0bf221a676bf33"

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


def ob_upgrade(ob_id):
    """ob_upgrade

    When an instrument package changes, attempts to port an existing OB
    to the new package, default is the current semId. # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: ObservationBlock
    """
    return 'do some magic!'


def ob_schedule_put(ob_id):  # noqa: E501
    """
    On success updates an existing ob schedule.

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """

    #TODO need schedule constraints in db

    return 'do some magic!'


def ob_schedule_get(ob_id):  # noqa: E501
    """
    Retrieves scheduling information. # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: List[str]
    """

    return 'Need schedule information in db'

