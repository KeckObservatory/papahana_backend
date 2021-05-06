import connexion
import six
import pymongo

from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.group_summary import GroupSummary  # noqa: E501
from swagger_server.models.observation_block import ObservationBlock  # noqa: E501
from swagger_server import util
from config import config_collection


def groups_get(group_id):  # noqa: E501
    """groups_get

    Retrieves a specific group&#x27;s information # noqa: E501

    :param group_id: group identifier
    :type group_id: str

    :rtype: Group
    """
    coll = config_collection('groupCollect', 'dev', config='./config.live.yaml')
    query = {"group_id": group_id}
    curse = coll.find(query)

    results = ""
    for result in curse:
        results += str(result)

    return results


def groups_post(body):  # noqa: E501
    """groups_post

    test:
    curl -v -H "Content-Type: application/json" -X POST -d '{"semester":"2020A"}' http://vm-webtools.keck:50001/v0/groups

    Creates a group # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: str: the ObjectID of the inserted document
    """
    if connexion.request.is_json:
        body = Group.from_dict(connexion.request.get_json())  # noqa: E501

    group_id = next_id('groups')

    coll = config_collection('groupCollect', 'dev', config='./config.live.yaml')

    new_doc = {"group_id": group_id, "name": body.name,
               "semester": body.semester, "ob_blocks": body.observation_blocks,
               "comment": body.comment}

    result = coll.insert_one(new_doc)

    return str(result.inserted_id)


def groups_put(body, group_id):  # noqa: E501
    """groups_put

    test :
    curl -v -H "Content-Type: application/json" -X PUT -d '{"semester":"2020A"}' 'http://vm-webtools.keck:50001/v0/groups?group_id=1'
    curl -v -H "Content-Type: application/json" -X PUT -d '{"semester":"2024A","observation_blocks":["2","3"]}' 'http://vm-webtools.keck:50001/v0/groups?group_id=19'

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

    coll = config_collection('groupCollect', 'dev', config='./config.live.yaml')

    new_vals = {}
    for key, val in group_dict.items():
        if val and key != 'group_id':
            new_vals[key] = val

    coll.update_one({"group_id": int_id(group_id)}, {"$set": new_vals})


def groups_delete(group_id):  # noqa: E501
    """groups_delete

    Delete group by id # noqa: E501

    :param group_id: group identifier
    :type group_id: str

    :rtype: None
    """
    coll = config_collection('groupCollect', 'dev', config='./config.live.yaml')

    group_id = int_id(group_id)
    query = {"group_id": group_id}
    coll.delete_one(query)


def groups_append_put(body, group_id):  # noqa: E501
    """groups_append_put

    Appends a list of observation blocks to a group by id.  It can be a
    single element array to add only one.

    test:
    curl -v -H "Content-Type: application/json" -X PUT -d '["1","4"]' 'http://vm-webtools.keck:50001/v0/groups/append?group_id=19'

    :param body:
    :type body: list | bytes
    :param group_id: group identifier
    :type group_id: str

    :rtype: None
    """
    coll = config_collection('groupCollect', 'dev', config='./config.live.yaml')
    query = {"group_id": int_id(group_id)}
    add_vals(coll, query, "observation_blocks", body)


def groups_execution_times_get(group_id):  # noqa: E501
    """groups_execution_times_get

    Calculate the total execution time of a group # noqa: E501

    :param group_id: group identifier
    :type group_id: str

    :rtype: float
    """
    return 'do some magic!'


def groups_export_get(group_id):  # noqa: E501
    """groups_export_get

    Retrieves a specific group information in a file format (default .json) # noqa: E501

    :param group_id: group identifier
    :type group_id: str

    :rtype: Group
    """
    return 'do some magic!'


def groups_items_get(group_id):  # noqa: E501
    """groups_items_get

    Retrieves the ordered list of observing blocks in a group.

    :param group_id: group identifier
    :type group_id: str

    :rtype: List[Group]
    """
    #TODO get ob_blocks from the ob_block

    return 'do some magic!'


#TODO not needed,  use groups/append

# def groups_items_put(body, group_id):  # noqa: E501
#     """groups_items_put
#
#     Puts a a list of Observation Blocks into a group # noqa: E501
#
#     :param body:
#     :type body: list | bytes
#     :param group_id: group identifier
#     :type group_id: str
#
#     :rtype: None
#     """
#     if connexion.request.is_json:
#         body = [ObservationBlock.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
#     # for val in ob_list
#     # db.containers.update({"container_id": "0"}, {$addToSet: {ob_blocks: "4"}} )
#
#     return 'do some magic!'


def groups_items_summary_get(group_id):  # noqa: E501
    """groups_items_summary_get

    Retrieves a summary of group information # noqa: E501

    :param group_id: group identifier
    :type group_id: str

    :rtype: GroupSummary
    """

    return 'do some magic!'


def groups_schedule_too_post(body):  # noqa: E501
    """groups_schedule_too_post

    Submits a group for Target of Opportunity (ToO) (all the elements)

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Group.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def groups_verify_get(group_id):  # noqa: E501
    """groups_verify_get

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


#helpers
def next_id(seq_collection):

    coll = config_collection('sequenceCollect', 'dev',
                             config='./config.live.yaml')
    query = {"_id": seq_collection}
    group_id = int_id(list(coll.find(query))[0]['value'])

    coll.update_one(query, {"$inc": {"value": 1}})

    return group_id


def int_id(group_id):
    try:
        return int(group_id)
    except ValueError:
        return -1


def add_vals(coll, query, col_name, val_list):

    #handle null values
    try:
        coll.update(query,
                    {"$push": {col_name: val_list[0]}})
    except pymongo.errors.WriteError:
        coll.update(query,
                    {"$set": {col_name: [val_list[0]]}})

    for i in range(1, len(val_list)):
        coll.update(query,
                    {"$push": {col_name: val_list[i]}})