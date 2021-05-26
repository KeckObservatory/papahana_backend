import connexion
from bson.objectid import ObjectId

from papahana.models.observation_block import ObservationBlock
from papahana.models.observation import Observation
from papahana.controllers import controller_helper as utils

from papahana import util
import pdb


def ob_get(ob_id):  # noqa: E501
    """
    Retrieves the general parameters of an OB.

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: ObservationBlock
    """
    try:
        return utils.get_by_id(ob_id, 'obCollect')
    except ValueError as err:
        return err


def ob_post(body):  # noqa: E501
    """
    Inserts an observation block.

    :param body: Observation block to be added.
    :type body: dict | bytes
    :rtype: str
    """
    if connexion.request.is_json:
        obDict = connexion.request.get_json()

    result = utils.insert_into_collection(obDict, 'obCollect')
    return str(result)


def ob_put(body, ob_id, helper=False):  # noqa: E501
    """
    Updates the observation block with the new one
    [webdev@vm-webtools ~]$ curl -v -H "Content-Type: application/json" -X PUT -d '{"signature.instrument": "KCWI-test"}' "http://vm-webtools.keck.hawaii.edu:50000/v0/obsBlocks?ob_id=609c27515ef7b19168a7f646"

    :param body: Observation block replacing ob_id.
    :type body: dict | bytes
    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    if not helper and connexion.request.is_json:
        body = connexion.request.get_json()

    print("here")
    print(body)
    utils.update_doc(utils.query_by_id(ob_id), body, 'obCollect')


def ob_delete(ob_id):  # noqa: E501
    """
    Removes the observation block # noqa: E501

    curl -v -H "Content-Type: application/json" -X DELETE "http://vm-webtools.keck.hawaii.edu:50001/v0/obsBlocks?ob_id=609c27515ef7b19168a7f646"

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    response = utils.delete_by_id(ob_id, 'obCollect')
    return str(response)


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
    try:
        ob = utils.get_by_id(ob_id, 'obCollect', cln_oid=False)
    except ValueError as err:
        return err

    if not ob:
        return f'No observing block with id {ob_id}'

    del ob['_id']

    if sem_id:
        ob['signature']['sem_id'] = sem_id

    result = utils.insert_into_collection(ob, 'obCollect')

    return str(result)


def ob_executions(ob_id):  # noqa: E501
    """
    Retrieves the list of execution attempts for a specific OB
    (for a specific night).

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: List[str]
    """
    try:
        ob = utils.get_by_id(ob_id, 'obCollect', cln_oid=False)
    except ValueError as err:
        return err

    if not ob or "status" not in ob or "executions" not in ob["status"]:
        return []

    return ob["status"]["executions"]


def ob_schedule_put(ob_id):  # noqa: E501
    """
    On success updates an existing ob schedule.

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """

    #TODO need schedule constraints in db

    return 'do some magic!'


#TODO should this only be the remaining execution time
def ob_execution_time(ob_id):  # noqa: E501
    """
    http://vm-webtools.keck.hawaii.edu:50001/v0/obsBlocks/executionTime/?ob_id=2

    Calculates the execution time. # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: float
    """
    try:
        ob = utils.get_by_id(ob_id, 'obCollect', cln_oid=False)
    except ValueError as err:
        return err

    if not ob or "science" not in ob:
        return 0

    sci_blk = ob['science']

    exp1 = 0
    exp2 = 0
    if sci_blk.keys() >= {"det1_exptime", "det1_nexp"}:
        if sci_blk['det1_exptime'] and sci_blk['det1_nexp']:
            exp1 = sci_blk['det1_exptime'] * sci_blk['det1_nexp']

    if sci_blk.keys() >= {"det1_exptime", "det2_exptime",
                          "det1_nexp", "det2_nexp"}:
        if sci_blk['det2_exptime'] and sci_blk['det2_nexp']:
            exp2 = sci_blk['det2_exptime'] * sci_blk['det2_nexp']

    return max(exp1, exp2)


def ob_export(ob_id):  # noqa: E501
    """
    http://vm-webtools.keck.hawaii.edu:50001/v0/obsBlocks/export/?ob_id=2

    Exports an OB in human-readable format. # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: ObservationBlock
    """
    try:
        return utils.get_by_id(ob_id, 'obCollect')
    except ValueError as err:
        return err


def ob_schedule_get(ob_id):  # noqa: E501
    """
    Retrieves scheduling information. # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: List[str]
    """

    return 'Need schedule information in db'


def ob_template_duplicate(ob_id, template_id):
    """
    Generate a new copy of the template

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index of template within the OB.
    :type template_id: int

    :rtype: ObservationBlock
    """

    return 'do some magic!'


def ob_template_filled(ob_id):  # noqa: E501
    """ob_template_filled

    Verify that the required parameters have been filled in.

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: bool
    """
    return 'do some magic!'


def ob_template_get(ob_id):  # noqa: E501
    """
    Retrieves the list of templates associated with the OB

    curl -v -H "Content-Type: application/json" -X DELETE "http://vm-webtools.keck.hawaii.edu:50001/v0/obsBlocks/template/0?ob_id=60adc652e7781dfbc33d2f18"

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: ObservationBlock
    """
    template_list = []

    ob = ob_get(ob_id)
    if not ob:
        return template_list

    if 'acquisition' in ob:
        acq = ob['acquisition']
        if acq:
            template_list.append(acq)

    if 'science' in ob:
        sci_templates = ob['science']
        if sci_templates:
            template_list.append(sci_templates)

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
        ob['acquisition'] = {}
    else:
        if 'science' not in ob:
            return
        indx = template_id - 1
        sci_templates = ob['science']
        if len(sci_templates) > indx:
            del sci_templates[indx]

        for template in sci_templates:
            template['index'] = template['index'] - 1

        ob['science'] = sci_templates

    ob_put(ob, ob_id, helper=True)


def ob_template_id_file_get(ob_id, template_id, file_parameter):  # noqa: E501
    """ob_template_id_file_get

    Retrieves the specified template within the OB # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index of template within the OB.
    :type template_id: int
    :param file_parameter: file paramter description here
    :type file_parameter: str

    :rtype: ObservationBlock
    """
    return 'do some magic!'


def ob_template_id_file_put(ob_id, template_id, file_parameter):  # noqa: E501
    """ob_template_id_file_put

    Updates the specified template within the OB # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index of template within the OB.
    :type template_id: int
    :param file_parameter: file paramter description here
    :type file_parameter: str

    :rtype: None
    """
    return 'do some magic!'


def ob_template_id_get(ob_id, template_id):  # noqa: E501
    """ob_template_id_get

    Retrieves the specified template within the OB # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index of template within the OB.
    :type template_id: int

    :rtype: ObservationBlock
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


def ob_template_id_put(ob_id, template_id):  # noqa: E501
    """ob_template_id_put

    Updates the specified template within the OB # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str
    :param template_id: index of template within the OB.
    :type template_id: int

    :rtype: None
    """
    return 'do some magic!'


def ob_template_post(ob_id):  # noqa: E501
    """ob_template_post

    Creates the list of templates associated with the OB # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    return 'do some magic!'


def ob_template_put(ob_id):  # noqa: E501
    """ob_template_put

    Updates the list of templates associated with the OB # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    return 'do some magic!'


def ob_template_supplement(ob_id):  # noqa: E501
    """ob_template_supplement

    Retrieves list of files. # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    return 'do some magic!'


def ob_time_constraint_get(ob_id, sidereal):  # noqa: E501
    """ob_time_constraint_get

    Retrieves the time constraints (from, to). # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str
    :param sidereal: tracking rate
    :type sidereal: bool

    :rtype: None
    """
    return 'do some magic!'


def ob_time_constraint_put(ob_id, sidereal):  # noqa: E501
    """ob_time_constraint_put

    Updates the time constraints (from, to). # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str
    :param sidereal: tracking rate
    :type sidereal: bool

    :rtype: None
    """
    return 'do some magic!'


def ob_upgrade(ob_id):  # noqa: E501
    """ob_upgrade

    When an instrument package changes, attempts to port an existing OB
    to the new package, default is the current semId. # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: ObservationBlock
    """
    return 'do some magic!'