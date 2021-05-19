import connexion
import six

from swagger_server.models.container import Container
from swagger_server.models.program import Program
from swagger_server.models.target import Target
from swagger_server.controllers import controller_helper as utils
from swagger_server.controllers import containers_controller

from swagger_server import util


def programs_get(obs_id):
    """
    retrieves all the programs associated with an observer.

    http://vm-webtools.keck.hawaii.edu:50001/v0/semesterIds/?obs_id=2003

    :param obs_id: observer id
    :type obs_id: int

    :rtype: List[Program]
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())

    sem_ids = utils.get_proposal_ids(obs_id)

    prg_list = []
    for sem_id in sem_ids:
        prg = program_semid_get(sem_id, obs_id)
        if prg:
            prg_list.append(prg)

    return prg_list


def sem_id_proposal_get(sem_id, obs_id):
    """
    retrieves the proposal associated with the program.

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: Object
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())

    #TODO get the pdf from the proposals API.

    return 'do some magic! sem_id_proposal_get'


def program_semester_get(semester, obs_id):
    """
    retrieves all the programs associated with an observer for the semester.

    :param semester: semester id
    :type semester: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: List[Program]
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())

    semester_list = []
    prg_list = programs_get(obs_id)
    for prg in prg_list:
        if 'sem_id' in prg and semester in prg['sem_id']:
            semester_list.append(prg)

    return semester_list


def program_semid_get(sem_id, obs_id):
    """
    Retrieves the specified program.

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: Program
    """

    sem_ids = utils.get_proposal_ids(obs_id)

    # check that the observer is associated with the sem_id passed in.
    if sem_id not in sem_ids:
        return None

    query = {'sem_id': sem_id}
    prg = utils.get_by_query(query, 'prgCollect')

    if prg:
        prg[0]['_id'] = str(prg[0]['_id'])
        return prg[0]

    return None


def program_submit_post(sem_id, obs_id):
    """
    Submits a program (OBs).  Uses the obsid in the authentication
    header and provided semId to retrieve the proposal file
    associated with the program

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())
    return 'do some magic! program_submit_post'


def program_submit_put(sem_id, obs_id):
    """sem_id_submit_put

    updates a program (OBs) # noqa: E501

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic! program_submit_put'


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
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())

    prg = program_semid_get(sem_id, obs_id)
    if 'container_list' not in prg:
        return None

    return prg['container_list']


def sem_id_targets_get(sem_id, obs_id):
    """
    Retrieves all the targets associated with a program. # noqa: E501

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: List[Target]
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())

    container_list = program_containers_get(sem_id, obs_id)

    for container_id in container_list:
        ob_blocks = containers_controller.containers_items_get(container_id)

    #TODO get targets from ob_blocks

    return 'do some magic! sem_id_targets_get'










