import connexion
import six

<<<<<<< HEAD
from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.program import Program  # noqa: E501
from swagger_server.models.target import Target  # noqa: E501
from swagger_server import util


def semester_programs_get(obs_id, semester=None):  # noqa: E501
    """retrieves all the programs associated with an observer

     # noqa: E501

=======
from swagger_server.models.group import Group
from swagger_server.models.program import Program
from swagger_server.models.target import Target
from swagger_server.controllers import controller_helper as utils

from swagger_server import util


#TODO rthis needs to be changed to observer instead of pi
# def semester_programs_get(obs_id, semester=None):
#     """retrieves all the programs associated with an observer
#
#     :param obs_id: observer id
#     :type obs_id: str
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


#TODO rthis needs to be changed to observer instead of pi
def semester_programs_get(obs_id, semester=None):
    """retrieves all the programs associated with an observer

>>>>>>> main
    :param obs_id: observer id
    :type obs_id: str
    :param semester: semester
    :type semester: str

    :rtype: List[Program]
    """
<<<<<<< HEAD
    return 'do some magic!'
=======

    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())

    query = {"$or": [{"pi_id": obs_id}, {"observers_id": obs_id}]}
    if semester:
        query["sem_id"] = {'$regex': f'{semester}_.*'}

    results = utils.get_by_query(query, 'prgCollect')

    cln_results = []
    for result in results:
        result['_id'] = str(result['_id'])
        cln_results.append(result)
    # > db.programs.find({$ or: [{"pi_id": "88"}, {"observers_id": "88"}]})

    # utils.get_by_id(obs_id, 'prgCollect')

    return cln_results
>>>>>>> main


def semesters_get(obs_id):  # noqa: E501
    """retrieves all the programs associated with a PI

     # noqa: E501

    :param obs_id: observer id
<<<<<<< HEAD
    :type obs_id: str

    :rtype: List[Program]
    """
=======
    :type obs_id: dict | bytes

    :rtype: List[Program]
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
>>>>>>> main
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
<<<<<<< HEAD
    """retrieves all the programs associated with an observer
=======
    """
    retrieves all the programs associated with an observer
>>>>>>> main

     # noqa: E501

    :param obs_id: observer id
<<<<<<< HEAD
    :type obs_id: str
=======
    :type obs_id: dict | bytes
>>>>>>> main
    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Program]
    """
<<<<<<< HEAD
=======
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
>>>>>>> main
    return 'do some magic!'


def semesters_proposal_get(obs_id, sem_id):  # noqa: E501
<<<<<<< HEAD
    """semesters_proposal_get

    retrieves the proposal associated with the program # noqa: E501

    :param obs_id: observer id
    :type obs_id: str
=======
    """
    retrieves the proposal associated with the program

    :param obs_id: observer id
    :type obs_id: dict | bytes
>>>>>>> main
    :param sem_id: semester id
    :type sem_id: str

    :rtype: Program
    """
<<<<<<< HEAD
=======
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
>>>>>>> main
    return 'do some magic!'


def semesters_submit_post(sem_id, obs_id):  # noqa: E501
    """semesters_submit_post

    Submits a program (OBs) # noqa: E501

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
<<<<<<< HEAD
    :type obs_id: str

    :rtype: None
    """
=======
    :type obs_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
>>>>>>> main
    return 'do some magic!'


def semesters_submit_put(obs_id, sem_id):  # noqa: E501
<<<<<<< HEAD
    """semesters_submit_put

    updates a program (OBs) # noqa: E501

    :param obs_id: observer id
    :type obs_id: str
=======
    """
    updates a program (OBs) # noqa: E501

    :param obs_id: observer id
    :type obs_id: dict | bytes
>>>>>>> main
    :param sem_id: semester id
    :type sem_id: str

    :rtype: None
    """
<<<<<<< HEAD
=======
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
>>>>>>> main
    return 'do some magic!'


def semesters_targets_get(obs_id, sem_id):  # noqa: E501
    """semesters_targets_get

    Retrieves all the targets associated with a program # noqa: E501

    :param obs_id: observer id
<<<<<<< HEAD
    :type obs_id: str
=======
    :type obs_id: dict | bytes
>>>>>>> main
    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Target]
    """
<<<<<<< HEAD
=======
    if connexion.request.is_json:
        obs_id = object.from_dict(connexion.request.get_json())  # noqa: E501
>>>>>>> main
    return 'do some magic!'
