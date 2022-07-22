import connexion
import six

from papahana.controllers import controller_helper as utils
from papahana.util import config_collection


def get_tag_oid(sem_id, tag_name, db_name=None):
    coll = config_collection('tagsCollect', db_name=db_name)
    query = {'tag_str': tag_name, 'sem_id': sem_id}
    fields = {'_id': 1}

    result = list(coll.find(query, fields))
    if not result:
        return None

    return str(result[0]['_id'])


def add_tag(sem_id, tag_name, db_name=None):

    tag_schema = {'sem_id': sem_id, 'tag_str': tag_name}

    coll = config_collection('tagsCollect', db_name=db_name)
    result = coll.insert_one(tag_schema)

    return str(result.inserted_id)


def get_tag_name(tag_id, db_name=None):

    fields = {'tag_str': 1, '_id': 0}
    results = utils.get_fields_by_id(tag_id, fields, 'tagsCollect', db_name=db_name)

    if not results:
        return None

    return results['tag_str']


def tag_is_in_ob(obj_id, tag_id):
    """
    Check if the tag is already in the OB tag_list.

    @param obj_id: <ObjectId> ObjectId of OB
    @param tag_id: <str> the tag object ID as string
    @return: <bool> True it the tag is already in the OB's tag list
    """
    query = {'_id': obj_id, 'metadata.tags': tag_id}
    fields = {'metadata.tags': 1, '_id': 0}

    results = utils.get_fields_by_query(query, fields, 'obCollect')
    if results:
        return True

    return False


def get_tag_list(ob_id):
    """
    get the tag list from the OB.

    @param ob_id: <str> the ObjectId string

    @return: <dict> the tag_list from the OB,  {"tags": [...]}
    """
    query = {'_id': utils.get_object_id(ob_id)}
    fields = {'metadata.tags': 1, '_id': 0}

    results = utils.get_fields_by_query(query, fields, 'obCollect')
    if not results:
        return None

    return results[0]['metadata']


def get_ob_sem_id(obj_id):
    """

    @param obj_id: <ObjectId> ObjectId of OB
    @return:
    """
    query = {'_id': utils.get_object_id(obj_id)}
    fields = {'metadata.sem_id': 1, '_id': 0}
    results = utils.get_fields_by_query(query, fields, 'obCollect')

    if not results:
        return None

    # {"metadata": {"sem_id": "2022B_U160"}}
    return results[0]['metadata']['sem_id']
