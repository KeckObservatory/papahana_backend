import connexion
import six

from swagger_server.models.container import Container
from swagger_server.models.program import Program
from swagger_server.models.target import Target
from swagger_server.controllers import controller_helper as utils

from swagger_server import util


#TODO rthis needs to be changed to observer instead of pi
# def semester_programs_get(obs_id, semester=None):
#     """retrieves all the programs associated with an observer
#
#     :param obs_id: observer id
#     :type obs_id: int
#     :param semester: semester
#     :type semester: str
#
#     :rtype: List[Program]
#     """
#
#     if connexion.request.is_json:
#         obs_id = object.from_dict(connexion.request.get_json())
#
#     if not obs_id:
#         return []
#
#     query = {"signature.pi_id": obs_id}
#     if semester:
#         query["signature.sem_id"] = {'$regex': f'{semester}_.*'}
#
#     ob_blocks = utils.get_by_query(query, 'obCollect')
#
#     prog_dict = {}
#     for ob in ob_blocks:
#         if ('_id' not in ob or 'signature' not in ob
#                 or "sem_id" not in ob['signature']):
#             continue
#
#         sem_id = ob['signature']['sem_id']
#         block_id = str(ob['_id'])
#         if sem_id in prog_dict:
#             program = prog_dict[sem_id]
#             ob_list = program.observation_blocks
#             if block_id not in ob_list:
#                 ob_list.append(block_id)
#             program.observation_blocks = ob_list
#             prog_dict[sem_id] = program
#         else:
#             parts = sem_id.split('_')
#             if len(parts) == 2:
#                 name = parts[1]
#             else:
#                 name = ""
#             prog_dict[sem_id] = Program(name, sem_id, [block_id])
#
#     program_list = list(prog_dict.values())
#
#     return program_list

#
# def semester_programs_get(obs_id, semester=None):
#     """
#     retrieves all the programs associated with an observer
#
#     :param obs_id: observer id
#     :type obs_id: int
#     :param semester: semester
#     :type semester: str
#
#     :rtype: List[Program]
#     """
#
#     if connexion.request.is_json:
#         obs_id = object.from_dict(connexion.request.get_json())
#
#     query = {"$or": [{"pi_id": obs_id}, {"observers_id": obs_id}]}
#     if semester:
#         query["sem_id"] = {'$regex': f'{semester}_.*'}
#
#     results = utils.get_by_query(query, 'prgCollect')
#
#     return utils.clean_objectid(results)


def programs_get(obs_id):  # noqa: E501
    """retrieves all the programs associated with an observer.

     # noqa: E501

    :param obs_id: observer id
    :type obs_id: int

    :rtype: List[Program]
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())

    sem_ids = utils.get_proposal_ids(obs_id)

    return sem_ids


    # query = {"pi_id": obs_id}
    #
    # # if semester:
    # #     query["sem_id"] = {'$regex': f'{semester}_.*'}
    #
    # results = utils.get_by_query(query, 'prgCollect')
    # return utils.clean_objectid(results)

def sem_id_proposal_get(sem_id, obs_id):  # noqa: E501
    """sem_id_proposal_get

    retrieves the proposal associated with the program. # noqa: E501

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: Object
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic! sem_id_proposal_get'


def program_semester_get(semester, obs_id):  # noqa: E501
    """retrieves all the programs associated with an observer for the semester.

    :param semester: semester id
    :type semester: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: List[Program]
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic! program_semester_get'


def program_semid_get(sem_id, obs_id):  # noqa: E501
    """Retrieves the specified program.

     # noqa: E501

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: Program
    """

    sem_ids = utils.get_proposal_ids(obs_id)
    if sem_id not in sem_ids:
        return 'No Results'

    query = {'sem_id': sem_id}
    prg = utils.get_by_query(query, 'prgCollect')

    if prg:
        prg[0]['_id'] = str(prg[0]['_id'])
        return prg[0]

    return 'No results'


def program_submit_post(sem_id, obs_id):  # noqa: E501
    """
    Submits a program (OBs).  Uses the obsid in the authentication
    header and provided semId to retrieve the proposal file
    associated with the program # noqa: E501

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic! program_submit_post'


def program_submit_put(sem_id, obs_id):  # noqa: E501
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


def sem_id_targets_get(sem_id, obs_id):  # noqa: E501
    """
    Retrieves all the targets associated with a program. # noqa: E501

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: int

    :rtype: List[Target]
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic! sem_id_targets_get'


def sem_id_targets_get(sem_id):  # noqa: E501
    """
    Retrieves all containers associated with a program # noqa: E501

    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Container]
    """
    return 'do some magic! sem_id_targets_get'


def program_containers_get(sem_id):  # noqa: E501
    """program_containers_get

    Retrieves all containers associated with a program # noqa: E501

    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Container]
    """
    return 'do some magic! program_containers_get'









