import connexion
import six
import pymongo

from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.group_summary import GroupSummary  # noqa: E501
from swagger_server.models.observation_block import ObservationBlock  # noqa: E501
from swagger_server.controllers import observation_block_controller as ob_control
from swagger_server.controllers import controller_helper as utils

# from swagger_server import util
from config import config_collection
from bson.objectid import ObjectId


def groups_get(group_id):  # noqa: E501
    """
    Retrieves a specific group's information # noqa: E501

    error:
    http://vm-webtools.keck.hawaii.edu:50000/v0/groups?group_id=09ad6fc4062bf346f1b0437
    result:
    http://vm-webtools.keck.hawaii.edu:50000/v0/groups?group_id=609ad6fc4062bf346f1b0437

    :param group_id: group identifier
    :type group_id: str

    :rtype: Group
    """
    result = utils.get_by_id(group_id, 'groupCollect')

    if result:
        result = str(result[0])
    else:
        result = ""

    return result


def groups_post(body):  # noqa: E501
    """
    Creates a group # noqa: E501

    test:
    curl -v -H "Content-Type: application/json" -X POST -d '{"semester":"2030A"}' http://vm-webtools.keck:50000/v0/groups
        db.groups.find({"semester": "2030A"})

    :param body:
    :type body: dict | bytes

    :rtype: str: the ObjectID of the inserted document
    """
    if connexion.request.is_json:
        body = Group.from_dict(connexion.request.get_json())  # noqa: E501

    new_doc = {"name": body.name, "semester": body.semester,
               "ob_blocks": body.observation_blocks, "comment": body.comment}

    result = utils.insert_into_collection(new_doc, 'groupCollect')

    return str(result.inserted_id)


def groups_put(body, group_id):  # noqa: E501
    """groups_put

    test :
    curl -v -H "Content-Type: application/json" -X PUT -d '{"semester":"2024A","observation_blocks":["2","3"]}' 'http://vm-webtools.keck:50000/v0/groups?group_id=609ad6fc4062bf346f1b0437'

    Overwrites a group # noqa: E501

    :param body:
    :type body: dict | bytes
    :param group_id: group identifier
    :type group_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Group.from_dict(connexion.request.get_json())  # noqa: E501

    group_dict = body.to_dict()

    new_vals = {}
    for key, val in group_dict.items():
        if val and key != 'group_id':
            new_vals[key] = val

    query = utils.query_by_id(group_id)
    utils.update_doc(query, new_vals, 'groupCollect')


def groups_delete(group_id):  # noqa: E501
    """groups_delete

    Delete group by id # noqa: E501

    :param group_id: group identifier
    :type group_id: str

    :rtype: None
    """
    query = utils.query_by_id(group_id)
    utils.delete_from_collection(query, 'groupCollect')


def groups_append_put(body, group_id):  # noqa: E501
    """groups_append_put

    Appends a list of observation blocks to a group by id.

    test (appends ob_id=9 to group_id=609306745ec7a7825e28af85):
    curl -v -H "Content-Type: application/json" -X PUT -d '["9"]' 'http://vm-webtools.keck:50000/v0/groups/append?group_id=609306745ec7a7825e28af85'

    :param body:
    :type body: list | bytes
    :param group_id: group identifier
    :type group_id: str

    :rtype: None
    """
    ob_list = utils.get_ob_list(group_id)

    # update the group collection with new values
    unique_obs = list(set(ob_list + body))
    if not unique_obs:
        return

    new_vals = {"observation_blocks": unique_obs}
    utils.update_doc(utils.query_by_id(group_id), new_vals, 'groupCollect')


def groups_execution_times_get(group_id):  # noqa: E501
    """
    Calculate the total execution time of a group

    http://vm-webtools.keck.hawaii.edu:50000/v0/groups/executionTimes?group_id=609306745ec7a7825e28af85

    :param group_id: group identifier
    :type group_id: str

    :rtype: float
    """
    ob_list = utils.get_ob_list(group_id)
    total_time = 0
    for ob in ob_list:
        total_time += ob_control.ob_execution_time(str(ob))

    return total_time


def groups_export_get(group_id):  # noqa: E501
    """
    Retrieves a specific group information in a file format (default .json)

    :param group_id: group identifier
    :type group_id: str

    :rtype: Group
    """
    query = utils.query_by_id(group_id)

    return 'do some magic!'


def groups_items_get(group_id):  # noqa: E501
    """groups_items_get

    Retrieves the ordered list of observing blocks in a group.

    :param group_id: group identifier
    :type group_id: str

    :rtype: List[Group]
    """
    ob_list = utils.get_ob_list(group_id)
    ob_list.sort()

    return str(ob_list)


# TODO this seems like it is the same as /groups_get
def groups_items_summary_get(group_id):  # noqa: E501
    """
    Retrieves a summary of group information # noqa: E501

    :param group_id: group identifier
    :type group_id: str

    :rtype: GroupSummary
    """

    return 'do some magic!'


def groups_schedule_too_post(body):  # noqa: E501
    """
    Submits a group for Target of Opportunity (ToO) (all the elements)

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Group.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def groups_verify_get(group_id):  # noqa: E501
    """
    Request verification of the elements of a group. Sends group summary
    as a successful response

    :param group_id: group identifier
    :type group_id: str

    :rtype: GroupSummary
    """
    #TODO get summary from the ob_block

    return 'do some magic!'


def sem_id_groups_get(sem_id):  # noqa: E501
    """sem_id_groups_get
    /semesters/groups

    Retrieves all groups associated with a program.

    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Group]
    """
    #TODO get sem_id from the ob_block
    return 'do some magic!'

