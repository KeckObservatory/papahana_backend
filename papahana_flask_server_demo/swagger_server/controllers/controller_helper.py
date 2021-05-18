from config import config_collection
import pymongo
import bson
import json
import requests
from flask import current_app


# Generalized
def get_by_id(id, collect_name):
    """
    query by string container_id

    :param container_id: container identifier
    :type container_id: str

    :rtype: Dict{Query}
    """
    try:
        id = get_object_id(id)
    except ValueError as msg:
        return [msg]

    query = {"_id": id}
    coll = config_collection(collect_name)

    return list(coll.find(query))


def get_by_query(query, collect_name):
    coll = config_collection(collect_name)

    return list(coll.find(query))


def get_fields_by_query(query, fields, collect_name):
    coll = config_collection(collect_name)

    return list(coll.find(query, fields))


def insert_into_collection(doc, collect_name):
    """
    Add a new document to a collection.

    :param doc: the document to insert
    :type doc: dict
    :param collect_name: the database collection to update.
    :type collect_name: str

    rtype: A document containing:
            A boolean acknowledged as true if the operation ran with
                write concern or false if write concern was disabled.
            A field insertedId with the _id value of the inserted document.

    """
    coll = config_collection(collect_name)

    try:
        result = coll.insert_one(doc)
    except Exception as err:
        return err

    if isinstance(result, pymongo.results.InsertOneResult):
        return result.inserted_id

    return result


def delete_by_id(id, collect_name):
    """
    Delete a document in a database collection.

    :param id: the document id
    :type query: str / ObjectId
    :param collect_name: the database collection to update.
    :type collect_name: str

    :rtype (int) 1 on error,  0 on success
    """
    try:
        id = get_object_id(id)
    except ValueError:
        return 1

    coll = config_collection(collect_name)

    try:
        coll.delete_one({'_id': id})
        return 0
    except Exception as err:
        print(err)
        return 1



#TODO check the type.
def replace_doc(id, doc, collect_name):
    """
    Replace a document in a database collection.

    :param id: the document id
    :type query: str / ObjectId
    :param doc: the document used as a replacement.
    :type doc: dict
    :param collect_name: the database collection to update.
    :type collect_name: str

    :rtype
    """
    try:
        id = get_object_id(id)
    except ValueError as err:
        return err

    coll = config_collection(collect_name)
    

    try:
        result = coll.replace_one({'_id': id}, doc)
    except Exception as err:
        return err

    return result


def update_doc(query, new_vals, collect_name):
    """
    Update a database collection document.

    :param query: the query used to find the document
    :type query: dict
    :param new_vals: the key/val pair of new values to update.
    :type new_vals: dict
    :param collect_name: the database collection to update.
    :type collect_name: str
    """
    coll = config_collection(collect_name)
    if '_id' in new_vals.keys():
        del new_vals['_id']

    coll.update_one(query, {"$set": new_vals})


def delete_from_collection(query, collect_name):
    """
    Delete document from a database collection.

    :param query: the query used to find the document
    :type query: dict
    :param collect_name: the database collection to update.
    :type collect_name: str
    """
    coll = config_collection(collect_name)

    try:
        coll.delete_one(query)
        return 0
    except Exception as err:
        print(err)
        return 1


def query_by_id(id):
    """
    query by string container_id

    :param container_id: container identifier
    :type container_id: str

    :rtype: Dict{Query}
    """
    try:
        id = get_object_id(id)
    except ValueError as err:
        return {"_id": None}

    return {"_id": id}


def get_object_id(obj_id):
    try:
        id = bson.objectid.ObjectId(obj_id)
    except bson.errors.InvalidId:
        raise ValueError("Invalid Object Id")
    except Exception as err:
        raise ValueError(err)

    return id


def clean_objectid(results):
    cln_results = []
    for result in results:
        result['_id'] = str(result['_id'])
        cln_results.append(result)

    return cln_results


# Container specific helpers
def get_ob_list(container_id):
    results = get_by_id(container_id, 'containerCollect')

    if results:
        ob_list = results[0]['observation_blocks']
    else:
        ob_list = []

    return ob_list
# semesters_and_program specific
def get_proposal_ids(obs_id):
    with current_app.app_context():
        urls = current_app.urls

# https://www.keck.hawaii.edu/software/db_api/proposalsAPI.php?cmd=getAllProposals&obsid=2003
#     url = f'https://www.keck.hawaii.edu/software/db_api/proposalsAPI.php?cmd=getAllProposals&obsid={obs_id}&json=True'
    url_cmd = f'cmd=getAllProposals&obsid={obs_id}&json=True'

    if 'proposalApi' not in urls:
        return None

    url = urls['proposalApi'] + url_cmd

    response = requests.get(url)
    try:
        result = json.loads(response.content)
    except Exception as err:
        return err

    if not result['success'] or 'data' not in result:
        return result['msg']

    prop_ids = []
    all_props = result['data']['AllProposals']
    for prop in all_props:
        if "KTN" not in prop:
            continue
        prop_ids.append(prop["KTN"])

    return prop_ids