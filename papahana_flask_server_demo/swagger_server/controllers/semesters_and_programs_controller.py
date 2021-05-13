import connexion
import six

from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.program import Program  # noqa: E501
from swagger_server.models.target import Target  # noqa: E501
from swagger_server import util


def sem_id_groups_get(sem_id):  # noqa: E501
    """sem_id_groups_get

    Retrieves all groups associated with a program # noqa: E501

    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Group]
    """
    return 'do some magic!'


def semester_programs_get(obs_id, sem_id):  # noqa: E501
    """retrieves all the programs associated with an observer

     # noqa: E501

    :param obs_id: observer id
    :type obs_id: dict | bytes
    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Program]
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def semesters_get(obs_id):  # noqa: E501
    """retrieves all the programs associated with a PI

     # noqa: E501

    :param obs_id: observer id
    :type obs_id: dict | bytes

    :rtype: List[Program]
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def semesters_observing_blocks_get(obs_id, sem_id):  # noqa: E501
    """retrieves all the programs associated with an observer

     # noqa: E501

    :param obs_id: observer id
    :type obs_id: dict | bytes
    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Program]
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def semesters_proposal_get(obs_id, sem_id):  # noqa: E501
    """semesters_proposal_get

    retrieves the proposal associated with the program # noqa: E501

    :param obs_id: observer id
    :type obs_id: dict | bytes
    :param sem_id: semester id
    :type sem_id: str

    :rtype: Program
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def semesters_submit_post(sem_id, obs_id):  # noqa: E501
    """semesters_submit_post

    Submits a program (OBs) # noqa: E501

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def semesters_submit_put(obs_id, sem_id):  # noqa: E501
    """semesters_submit_put

    updates a program (OBs) # noqa: E501

    :param obs_id: observer id
    :type obs_id: dict | bytes
    :param sem_id: semester id
    :type sem_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def semesters_targets_get(obs_id, sem_id):  # noqa: E501
    """semesters_targets_get

    Retrieves all the targets associated with a program # noqa: E501

    :param obs_id: observer id
    :type obs_id: dict | bytes
    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Target]
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
