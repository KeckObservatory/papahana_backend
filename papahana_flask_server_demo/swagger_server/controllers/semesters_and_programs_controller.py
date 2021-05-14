import connexion
import six

from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.program import Program  # noqa: E501
from swagger_server.models.target import Target  # noqa: E501
from swagger_server import util


def semester_programs_get(obs_id, semester=None):  # noqa: E501
    """retrieves all the programs associated with an observer

     # noqa: E501

    :param obs_id: observer id
    :type obs_id: str
    :param semester: semester
    :type semester: str

    :rtype: List[Program]
    """
    return 'do some magic!'


def semesters_get(obs_id):  # noqa: E501
    """retrieves all the programs associated with a PI

     # noqa: E501

    :param obs_id: observer id
    :type obs_id: str

    :rtype: List[Program]
    """
    return 'do some magic!'


def semesters_groups_get(sem_id):  # noqa: E501
    """semesters_groups_get

    Retrieves all groups associated with a program # noqa: E501

    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Group]
    """
    return 'do some magic!'


def semesters_observing_blocks_get(obs_id, sem_id):  # noqa: E501
    """retrieves all the programs associated with an observer

     # noqa: E501

    :param obs_id: observer id
    :type obs_id: str
    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Program]
    """
    return 'do some magic!'


def semesters_proposal_get(obs_id, sem_id):  # noqa: E501
    """semesters_proposal_get

    retrieves the proposal associated with the program # noqa: E501

    :param obs_id: observer id
    :type obs_id: str
    :param sem_id: semester id
    :type sem_id: str

    :rtype: Program
    """
    return 'do some magic!'


def semesters_submit_post(sem_id, obs_id):  # noqa: E501
    """semesters_submit_post

    Submits a program (OBs) # noqa: E501

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: str

    :rtype: None
    """
    return 'do some magic!'


def semesters_submit_put(obs_id, sem_id):  # noqa: E501
    """semesters_submit_put

    updates a program (OBs) # noqa: E501

    :param obs_id: observer id
    :type obs_id: str
    :param sem_id: semester id
    :type sem_id: str

    :rtype: None
    """
    return 'do some magic!'


def semesters_targets_get(obs_id, sem_id):  # noqa: E501
    """semesters_targets_get

    Retrieves all the targets associated with a program # noqa: E501

    :param obs_id: observer id
    :type obs_id: str
    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Target]
    """
    return 'do some magic!'
