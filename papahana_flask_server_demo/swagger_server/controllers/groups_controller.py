import connexion
import six
import pymongo

from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.group_summary import GroupSummary  # noqa: E501
from swagger_server.models.observation_block import ObservationBlock  # noqa: E501
from swagger_server import util
from config import config_collection
from bson.objectid import ObjectId


def groups_get(group_id):  # noqa: E501
    """groups_get

    Retrieves a specific group&#x27;s information # noqa: E501

    :param group_id: group identifier
    :type group_id: str

    :rtype: Group
    """
    coll = config_collection('groupCollect', 'dev', config='./config.live.yaml')

    query = query_by_id(group_id)
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

    coll = config_collection('groupCollect', 'dev', config='./config.live.yaml')

    new_doc = {"name": body.name, "semester": body.semester,
               "ob_blocks": body.observation_blocks, "comment": body.comment}

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
    query = query_by_id(group_id)

    coll.update_one(query, {"$set": new_vals})

def groups_delete(group_id):  # noqa: E501
    """groups_delete

    Delete group by id # noqa: E501

    :param group_id: group identifier
    :type group_id: str

    :rtype: None
    """

    coll = config_collection('groupCollect', 'dev', config='./config.live.yaml')

    query = query_by_id(group_id)
    coll.delete_one(query)


def groups_append_put(body, group_id):  # noqa: E501
    """groups_append_put

    Appends a list of observation blocks to a group by id.

    test (appends ob_id=9 to group_id=609306745ec7a7825e28af85):
    curl -v -H "Content-Type: application/json" -X PUT -d '["9"]' 'http://vm-webtools.keck:50001/v0/groups/append?group_id=609306745ec7a7825e28af85'

    :param body:
    :type body: list | bytes
    :param group_id: group identifier
    :type group_id: str

    :rtype: None
    """
    grps = config_collection('groupCollect', 'dev', config='./config.live.yaml')
    ob_list = get_ob_list(grps, group_id)

    # update OB -> signature -> group
    ob_blocks = config_collection('obCollectionName', 'dev',
                                  config='./config.live.yaml')

    # update the ob_block with the group id
    for ob_id in body:
        if not add_id_to_ob(ob_blocks, ob_id, group_id):
            ob_list.remove(ob_id)
            #TODO report ob_block doesn't exist

    # update the group collection with new values
    unique_obs = list(set(ob_list + body))
    if not unique_obs:
        return

    grps.update(query_by_id(group_id),
                {"$set": {"observation_blocks": unique_obs}})


def groups_execution_times_get(group_id):  # noqa: E501
    """groups_execution_times_get

    Calculate the total execution time of a group # noqa: E501

    :param group_id: group identifier
    :type group_id: str

    :rtype: float
    """
    #TODO execution times not yet in ob_block.
    query = query_by_id(group_id)

    return 'do some magic!'


def groups_export_get(group_id):  # noqa: E501
    """groups_export_get

    Retrieves a specific group information in a file format (default .json) # noqa: E501

    :param group_id: group identifier
    :type group_id: str

    :rtype: Group
    """
    query = query_by_id(group_id)

    return 'do some magic!'


def groups_items_get(group_id):  # noqa: E501
    """groups_items_get

    Retrieves the ordered list of observing blocks in a group.

    :param group_id: group identifier
    :type group_id: str

    :rtype: List[Group]
    """
    grps = config_collection('groupCollect', 'dev', config='./config.live.yaml')
    ob_list = get_ob_list(grps, group_id)
    ob_list.sort()

    return str(ob_list)


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
def query_by_id(group_id):
    """
    query by string group_id

    :param group_id: group identifier
    :type group_id: str

    :rtype: Dict{Query}
    """
    obj_id = ObjectId(group_id)
    return {"_id": obj_id}


def add_id_to_ob(coll, ob_id, group_id):
    """
    Add the group id to the ob_block

    :param coll: database cursor
    :param ob_id: The id of the ob_block
    :type group_id: str
    :param group_id: group identifier
    :type group_id: str

    :rtype: int - 1 on success, 0 when ob_block not found.
    """
    query = {"_id": ob_id}
    results = list(coll.find(query))
    if not results:
        return 0

    groups = results[0]['signature']['group']
    if not groups:
        groups = []
    elif type(groups) != list:
        groups = [groups]

    groups.append(group_id)
    unique_grps = list(set(groups))

    coll.update(query, {"$set": {"signature.group": unique_grps}})

    return 1


def get_ob_list(coll, group_id):
    query = query_by_id(group_id)
    results = list(coll.find(query))
    if results:
        ob_list = results[0]['observation_blocks']
    else:
        ob_list = []

    return ob_list
