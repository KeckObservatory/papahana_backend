import connexion
import six

from papahana.controllers import controller_helper as utils
from papahana.controllers import containers_controller
from papahana.controllers import observation_block_controller


from papahana.models.container import Container  
from papahana.models.observation_block import ObservationBlock  
from papahana.models.sem_id_schema import SemIdSchema  
from papahana.models.target import Target  
from papahana import util


def sem_id_get(obs_id):
    """
    Retrieves all the sem_ids associated with an observer

    http://vm-webtools.keck.hawaii.edu:50001/v0/semesterIds/?obs_id=2003

    :param obs_id: observer id
    :type obs_id: int

    :rtype: List[str]
    """
    semid_list = utils.get_proposal_ids(obs_id)

    return semid_list


# def sem_id_proposal_get(sem_id, obs_id):
#     """
#     retrieves the proposal associated with the program.
#
#     :param sem_id: semester id
#     :type sem_id: str
#     :param obs_id: observer id
#     :type obs_id: int
#
#     :rtype: file
#     """
#     #TODO get the pdf from the proposals API.
#
#     return 'do some magic! sem_id_proposal_get'


def sem_id_semester_get(semester, obs_id):
    """
     retrieves all the sem_id associated with an observer for the semester.

    :param semester: semester id
    :type semester: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: List[str]
    """
    semester_list = []
    sem_ids = utils.get_proposal_ids(obs_id)
    for semid in sem_ids:
        if semester in semid:
            semester_list.append(semid)

    return semester_list


def sem_id_ob_get(sem_id, obs_id):
    """
    Retrieves the ob_blocks for a sem_id

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: List[ObservationBlock]
    """
    if not utils.obs_id_associated(sem_id, obs_id):
        return []

    query = {"signature.sem_id": sem_id}
    ob_blocks = utils.get_by_query(query, 'obCollect')

    return utils.list_with_objectid(ob_blocks)


def sem_id_containers_get(sem_id, obs_id):
    """
    Retrieves all containers associated with a program
    http://vm-webtools.keck.hawaii.edu:50001/v0/semesterIds/2020A_U169/containers?obs_id=2003

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: List[Container]
    """
    if not utils.obs_id_associated(sem_id, obs_id):
        return []

    query = {"sem_id": sem_id}
    containers = utils.get_by_query(query, 'containerCollect')

    return utils.list_with_objectid(containers)


def sem_id_targets_get(sem_id, obs_id):
    """
    Retrieves all the targets associated with a program.

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: List[Target]
    """
    ob_blocks = sem_id_ob_get(sem_id, obs_id)

    all_targets = []
    for ob_block in ob_blocks:
        if 'target' in ob_block:
            all_targets.append(ob_block['target'])

    return all_targets


# def sem_id_submit_post(body, obs_id, sem_id):
#     """
#     Submits OBs for a program.  Uses the obsid in the authentication
#     header and provided semId to retrieve the proposal file
#     associated with the program
#
#     :param body:
#     :type body: dict | bytes
#     :param sem_id: semester id
#     :type sem_id: str
#     :param obs_id: observer id
#     :type obs_id: int
#
#     :rtype: None
#     """
#     return 'do some magic! sem_id_submit_post'
#
#
# def sem_id_submit_put(obs_id, sem_id, body=None):
#     """sem_id_submit_put
#
#     updates a program (OBs)
#
#     :param sem_id: semester id
#     :type sem_id: str
#     :param obs_id: observer id
#     :type obs_id: int
#     :param body:
#     :type body: dict | bytes
#
#     :rtype: None
#     """
#     return 'do some magic! sem_id_submit_put'
#










