import connexion
from copy import deepcopy
from flask import abort
from io import StringIO
import json

from papahana.models.observation_block import ObservationBlock
from papahana.models.observation import Observation
from papahana.controllers import controller_helper as utils

from papahana import util


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
    :rtype: str
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
    response = utils.delete_by_id(ob_id, 'obCollect')


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
def ob_execution_time(ob_id):  # noqa: E501
    """
    http://vm-webtools.keck.hawaii.edu:50001/v0/obsBlocks/executionTime/?ob_id=2

    Calculates the execution time. # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: float
    """
    fields = {"science.properties": 1, "_id": 0}
    ob_science = utils.get_fields_by_query(utils.query_by_id(ob_id),
                                           fields, 'obCollect')

    if not ob_science:
        return 0

    total_tm = 0
    sci_blks = ob_science[0]['science']
    for block in sci_blks:
        total_tm += utils.calc_exec_time(block)

    return total_tm


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
    fields = {"schema": 1, "_id": 0}
    templates = ob_template_get(ob_id)
    for filled in templates:
        if filled.keys() < {"name", "version", "properties"}:
            return False

        query = {"name": filled["name"], "version": filled["version"]}
        schema = utils.get_fields_by_query(query, fields, 'templateCollect')
        if not schema:
            return False

        required = schema[0]['schema']['required']
        properties = schema[0]['schema']['properties']

        return check_required(required, properties, filled)


def check_required(required, properties, filled):

    for key in required:
        if ('properties' not in filled or key not in filled['properties'] or
                not filled['properties'][key]):
            return False
        key_props = properties[key]
        key_type = key_props['type']
        if key_type is 'number' or key_type is 'integer':
            if (filled[key] > key_props['maximum'] or
                    filled[key] < key_props['minimum']):
                return False
        elif key_type is 'array':
            req = key_props['items']['required']
            props = key_props['items']['properties']
            for key2 in req:
                # TODO figure out the array ....
                continue


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
    :param template_id: index of template within the OB.
    :type template_id: int

    :rtype: None
    """
    ob = ob_get(ob_id)
    if template_id == 0:
        if 'acquisition' not in ob:
            return
        del ob['acquisition']
    else:
        if 'science' not in ob:
            return
        indx = template_id - 1
        sci_templates = ob['science']

        if len(sci_templates) < indx:
            return
        del sci_templates[indx]

        for cnt in range(0, len(sci_templates)):
            sci_templates[cnt]['index'] = cnt + 1

        ob['science'] = sci_templates

    utils.update_doc(utils.query_by_id(ob_id), ob, 'obCollect')


def ob_template_id_file_get(ob_id, template_id, file_parameter):
    """
    Retrieves the specified template within the OB

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index of template within the OB.
    :type template_id: int
    :param file_parameter: file paramter description here
    :type file_parameter: str

    :rtype: ObservationBlock
    """
    template = ob_template_id_get(ob_id, template_id)
    file = StringIO(template)

    return file.getvalue()


def ob_template_id_file_put(ob_id, template_id, file_parameter):
    """
    Updates the specified template within the OB

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index of template within the OB.
    :type template_id: int
    :param file_parameter: file paramter description here
    :type file_parameter: str

    :rtype: None
    """
    return 'do some magic!'


def ob_template_id_get(ob_id, template_id):
    """
    Retrieves the specified template within the OB

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index of template within the OB.
    :type template_id: int

    :rtype: Observation
    """
    ob = ob_get(ob_id)

    if template_id == 0:
        return ob['acquisition']

    template_indx = template_id - 1
    if 'science' not in ob:
        return {}

    sci_templates = ob['science']
    if sci_templates and len(sci_templates) > template_indx:
        return sci_templates[template_indx]

    return {}


def ob_template_duplicate(ob_id, template_id):
    """
    Generate a new copy of the template and add it to the list of templates in
    the OB.

    curl -v -H "Content-Type: application/json" -X POST "http://vm-webtools.keck.hawaii.edu:50001/v0/obsBlocks/template/duplicate/1?ob_id=60aec72417469e6111a54d78"

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index of template within the OB.
    :type template_id: int

    :rtype: Observation
    """
    if template_id == 0:
        abort(404, 'Invalid template ID')

    ob = ob_get(ob_id)

    if 'science' not in ob or len(ob['science']) < template_id:
        abort(404, 'Invalid template ID')

    sci_templates = ob['science']
    new_template = deepcopy(sci_templates[template_id - 1])
    new_template['index'] = len(sci_templates) + 1

    sci_templates.append(new_template)
    utils.update_doc(utils.query_by_id(ob_id), {"science": sci_templates},
                     'obCollect')

    return new_template


def ob_template_id_put(body, ob_id, template_id):
    """
    Updates the specified template within the OB

    :param body:
    :type body: dict | bytes
    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index of template within the OB.
    :type template_id: int

    :rtype: None
    """

    if connexion.request.is_json:
        body = json.loads(json.dumps(connexion.request.get_json()))

    ob = ob_get(ob_id)
    if template_id == 0:
        key = 'acquisition'
    else:
        key = 'science'

    if key not in ob or len(ob[key]) < template_id:
        abort(404, 'Invalid template ID')

    if template_id == 0:
        templates = body
    else:
        templates = ob[key]
        body['index'] = template_id
        templates[template_id - 1] = body

    utils.update_doc(utils.query_by_id(ob_id), {key: templates},
                     'obCollect')


def ob_template_post(body, ob_id, template_type):  # noqa: E501
    """
    Creates the list of templates associated with the OB

    curl -v -H "Content-Type: application/json" -X POST -d '[ { "name" : "KCWI_ifu_sci_stare", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 1200, "DET1_NEXP" : 2, "DET2_EXPTIME" : 1200, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "index" : 1 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 2 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 3 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 4 } ]' "http://vm-webtools.keck:50001/v0/obsBlocks/template?ob_id=60bab915ddb1146b87136414&template_type=sci"

    :param body:
    :type body: list or dict
    :param ob_id: observation block id
    :type ob_id: str
    :param template_type: A string to indicate template, (acq, sci, eng, cal)
    :type template_type: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = json.loads(json.dumps(connexion.request.get_json()))

    if type(body) is not list:
        body = [body]

    full_type = {'sci': 'science', 'acq': 'acquisition', 'eng': 'engineering',
                 'cal': 'calibration'}

    new_vals = {full_type[template_type]: body}

    utils.update_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')


def ob_template_put(body, ob_id, template_type):
    """
    Updates the list of templates associated with the OB

    curl -v -H "Content-Type: application/json" -X PUT -d '[ { "name" : "KCWI_ifu_sci_stare", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 1200, "DET1_NEXP" : 2, "DET2_EXPTIME" : 1200, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "index" : 1 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 2 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 3 }, { "name" : "KCWI_ifu_sci_dither", "instrument" : "KCWI", "type" : "sci", "version" : 0.1, "DET1_EXPTIME" : 60, "DET1_NEXP" : 2, "DET2_EXPTIME" : 60, "DET2_NEXT" : 2, "CFG_CAM1_GRATING" : "BM", "CFG_CAM1_CWAVE" : 4500, "CFG_SLICER" : "Medium", "SEQ_NDITHER" : 3, "SEQ_DITARRAY" : [ [ 0, 0, "T", "Guided" ], [ 5, 5, "T", "Guided" ], [ -10, -10, "T", "Guided" ] ], "index" : 4 } ]' "http://vm-webtools.keck:50001/v0/obsBlocks/template?ob_id=60bab915ddb1146b87136414&template_type=sci"

    :param body:
    :type body: dict | bytes
    :param ob_id: observation block id
    :type ob_id: str
    :param template_type: A string to indicate template, (acq, sci, eng, cal)
    :type template_type: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = json.loads(json.dumps(connexion.request.get_json()))

    full_type = {'sci': 'science', 'acq': 'acquisition', 'eng': 'engineering',
                 'cal': 'calibration'}

    if type(body) is list:
        for val in body:
            new_vals = {full_type[template_type]: val}
            utils.update_add_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')
    else:
        new_vals = {full_type[template_type]: body}
        utils.update_add_doc(utils.query_by_id(ob_id), new_vals, 'obCollect')


def ob_template_supplement(ob_id):
    """
    Retrieves list of files.

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    return 'do some magic!'


def ob_time_constraint_get(ob_id, sidereal):
    """
    Retrieves the time constraints (from, to).

    :param ob_id: observation block id
    :type ob_id: str
    :param sidereal: tracking rate
    :type sidereal: bool

    :rtype: None
    """
    return 'do some magic!'


def ob_time_constraint_put(body, ob_id, sidereal):
    """
    Updates the time constraints (from, to).

    :param body:
    :type body: dict | bytes
    :param ob_id: observation block id
    :type ob_id: str
    :param sidereal: tracking rate
    :type sidereal: bool

    :rtype: None
    """
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())
    return 'do some magic!'


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

