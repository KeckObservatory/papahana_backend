from config import config_collection
# from bson.objectid import ObjectId
import bson


# def create_match(key, item):
#     if key == 'observers':
#         mItem = {
#             f"signature.observers": {
#             "$exists": "true", "$in": [ f"{item}"]
#         }}
#     else:
#         mItem = {
#             f"signature.{key}": item
#         }
#     return mItem
#
# def create_signature_match(coll, qdict):
#     '''note matching flattens nested fields'''
#     matchItems = [ create_match(key, item) for key, item in qdict.items() ]
#     return {
#         "$match": {
#             "$and": matchItems
#         }
#     }
#
# def group_distinct_signature(key):
#     '''group by one field in aggreate pipeline'''
#     return {
#             "$group":{
#                 "_id": { key: f"$signature.{key}" }
#             }
#         }
#
# def project_fields(*signatureKeys):
#     return {"$project": { f"{key}": 1 for key in signatureKeys } }
#
# def project_signature_fields(*signatureKeys):
#     return {"$project": { f"signature.{key}": 1 for key in signatureKeys } }
#
# def get_distinct_semesters(obsName, coll):
#     match = create_signature_match(coll, {'observers': obsName})
#     group = group_distinct_signature('semesters')
#     pipeline = [
#         match,
#         group
#     ]
#     return coll.aggregate(pipeline)
#
# def get_semesters_by_pi(piName, coll):
#     match = create_signature_match(coll, {'pi': piName})
#     project = project_signature_fields('semesters')
#     pipeline = [ match, project ]
#     return coll.aggregate(pipeline)
#
# def get_ob_by_semester(semid, coll):
#     match = create_signature_match(coll, {'semesters': semid})
#     pipeline = [ match ]
#     return coll.aggregate(pipeline)
#
# def get_ob_by_semester_observer(semid, observer, coll):
#     match = create_signature_match(coll, {'semesters': semid, 'observers': observer})
#     pipeline = [ match ]
#     return coll.aggregate(pipeline)
#
# def find_by_pi(name, coll):
#     query = {
#         "signature.pi": name
#     }
#     return coll.find(query)
#
# def find_by_semester_program(semester, program, coll):
#     query = {
#         "signature.semesters": {
#             "$in": [semester]
#         },
#         "signature.program": program
#     }
#     return coll.find(query)
#
# def find_by_observer(observer, coll):
#     query = {
#         "signature.observers": {
#             "$in": [observer]
#         }
#     }
#     return coll.find(query)
#
# def find_by_observer_semester(observer, semester, coll):
#     query = {
#         "signature.observers": {
#             "$in": [observer]
#         },
#         "signature.semesters": {
#             "$in": [semester]
#         },
#     }
#     return coll.find(query)
#
#
# def get_ob_by_id(_id, coll):
#     coll = config_collection('obCollect', 'dev')
#
#     query = {
#         "_id": _id
#     }
#     return coll.find(query)
#
#
# def insert_observation_block(ob, coll):
#     try:
#         result = coll.insert_one(ob)
#     except Exception as err:
#         return err
#     return result
#
# def delete_observation_block(_id, coll):
#     try:
#         coll.delete_one({'_id': _id})
#     except Exception as err:
#         print(err)
#
# def replace_observation_block(_id, ob, coll):
#     try:
#         query = {'_id': _id}
#         result = coll.replace_one(query, ob)
#     except Exception as err:
#         print(err)
#     return result
#
# def update_observation_block(_id, newValues, coll):
#     query = {
#         "_id": _id
#     }
#     coll.update_one(query, newValues)

# Generalized


def get_by_id(id, collect_name, object_id=False):
    """
    query by string group_id

    :param group_id: group identifier
    :type group_id: str

    :rtype: Dict{Query}
    """
    coll = config_collection(collect_name)

    if object_id:
        try:
            id = get_object_id(id)
        except ValueError as msg:
            return [msg]

    query = {"_id": id}

    return list(coll.find(query))


def insert_into_collection(doc, collect_name):
    """
    body

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

    return result


def delete_by_id(id, collect_name, object_id=False):
    """
    Delete a document in a database collection.

    :param id: the document id
    :type query: str / ObjectId
    :param collect_name: the database collection to update.
    :type collect_name: str
    :param object_id: True if the id is an ObjectId
    :type object_id: bool

    :rtype (int) 1 on error,  0 on success
    """
    coll = config_collection(collect_name)

    if object_id:
        try:
            id = get_object_id(id)
        except ValueError:
            return 1

    try:
        coll.delete_one({'_id': id})
        return 0
    except Exception as err:
        print(err)
        return 1

#TODO check the type.
def replace_doc(id, doc, collect_name, object_id=False):
    """
    Replace a document in a database collection.

    :param id: the document id
    :type query: str / ObjectId
    :param doc: the document used as a replacement.
    :type doc: dict
    :param collect_name: the database collection to update.
    :type collect_name: str
    :param object_id: True if the id is an ObjectId
    :type object_id: bool

    :rtype
    """
    coll = config_collection(collect_name)

    if object_id:
        try:
            id = get_object_id(id)
        except ValueError as err:
            return err

    try:
        query = {'_id': id}
        result = coll.replace_one(query, doc)
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


def query_by_id(id, object_id=True):
    """
    query by string group_id

    :param group_id: group identifier
    :type group_id: str

    :rtype: Dict{Query}
    """
    if object_id:
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


# Group specific helpers
def get_ob_list(group_id):
    # grps = config_collection('groupCollect')
    print(group_id)
    results = get_by_id(group_id, 'groupCollect', object_id=True)
    # query = query_by_id(group_id)
    # results = list(grps.find(query))
    print("res", results)
    if results:
        ob_list = results[0]['observation_blocks']
    else:
        ob_list = []

    return ob_list
