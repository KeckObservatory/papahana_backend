from config import config_collection
import pymongo
import bson
import json
import requests
from flask import current_app, abort
from bson import json_util


# Generalized
def list_with_objectid(results):
    """
    unwrap a list of dictionaries that include ObjectIds

    :param result: the results
    :type result: dict

    :rtype : List[Dict{Query Result}]
    """
    for indx in range(0, len(results)):
        results[indx] = json_with_objectid(results[indx])

    return results


def json_with_objectid(result):
    """
    work with the ObjectID to make it json serializable.  Also unnest the
    $oid from _id to make the id = result['_id]

    :param result: the results
    :type result: dict

    :rtype : Dict{Query Result}
    """
    cln_result = json.loads(json_util.dumps(result))
    if '_id' in cln_result and '$oid' in cln_result['_id']:
        cln_result['_id'] = cln_result['_id']['$oid']

    return cln_result


def get_by_id(id, collect_name, cln_oid=True):
    """
    query by string container_id

    :param container_id: container identifier
    :type container_id: str
    :param collect_name: the database collection.
    :type collect_name: str

    :rtype: Dict{Query Result}
    """
    id = get_object_id(id)

    query = {"_id": id}
    coll = config_collection(collect_name)

    results = list(coll.find(query))
    if not results:
        abort(404, f'No Observation Block found.')

    if cln_oid:
        return json_with_objectid(results[0])

    return results[0]


def get_by_query(query, collect_name):
    """
    query the database by input query pararmeters for all fields in a document.

    :param query: json query parameter
    :type query: dict
    :param collect_name: the database collection.
    :type collect_name: str

    :rtype: List[Dict{Query Result}]
    """
    coll = config_collection(collect_name)

    return list(coll.find(query))


def get_fields_by_query(query, fields, collect_name):
    """
    query the database by input query parameters for input fields.

    :param query: json query parameters
    :type query: dict
    :param query: json field parameters
    :type query: dict
    :param collect_name: the database collection.
    :type collect_name: str

    :rtype: List[Dict{Query Result}]
    """
    coll = config_collection(collect_name)

    return list(coll.find(query, fields))


def get_fields_by_id(ob_id, fields, collect_name):
    """
    query the database by ObjectId for input fields.

    :param query: json query parameters
    :type query: dict
    :param query: json field parameters
    :type query: dict
    :param collect_name: the database collection.
    :type collect_name: str

    :rtype: List[Dict{Query Result}]
    """
    coll = config_collection(collect_name)
    query = query_by_id(ob_id)

    results = list(coll.find(query, fields))
    if not results:
        return None

    return results[0]


def insert_into_collection(doc, collect_name):
    """
    Add a new document to a collection.

    :param doc: the document to insert
    :type doc: dict
    :param collect_name: the database collection.
    :type collect_name: str

    rtype: document id
    """
    coll = config_collection(collect_name)

    if "_id" in doc:
        del doc["_id"]
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
    :param collect_name: the database collection.
    :type collect_name: str

    :rtype (int) 1 on error,  0 on success
    """
    id = get_object_id(id)

    coll = config_collection(collect_name)

    try:
        coll.delete_one({'_id': id})
        return 0
    except Exception as err:
        print(err)
        return 1


def replace_doc(id, doc, collect_name):
    """
    Replace a document in a database collection.

    :param id: the document id
    :type query: str / ObjectId
    :param doc: the document used as a replacement.
    :type doc: dict
    :param collect_name: the database collection.
    :type collect_name: str

    :rtype
    """
    id = get_object_id(id)

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
    :param collect_name: the database collection.
    :type collect_name: str
    """
    coll = config_collection(collect_name)
    if '_id' in new_vals.keys():
        del new_vals['_id']

    coll.update_one(query, {"$set": new_vals})


def update_add_doc(query, new_vals, collect_name):
    """
    Add to a database collection document.

    :param query: the query used to find the document
    :type query: dict
    :param new_vals: the key/val pair of new values to update.
    :type new_vals: dict
    :param collect_name: the database collection.
    :type collect_name: str
    """
    coll = config_collection(collect_name)
    if '_id' in new_vals.keys():
        del new_vals['_id']

    coll.update_one(query, {"$push": new_vals})


def delete_from_collection(query, collect_name):
    """
    Delete document from a database collection.

    :param query: the query used to find the document
    :type query: dict
    :param collect_name: the database collection.
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
    id = get_object_id(id)

    return {"_id": id}


def get_object_id(obj_id):
    """
    transform an ObjectId string to ObjectId
    :param obj_id: ObjectId string
    :type obj_id: str

    :rtype: ObjectId
    """
    try:
        id = bson.objectid.ObjectId(obj_id)
    except bson.errors.InvalidId:
        abort(404, f'Invalid observation block id.')
    except Exception as err:
        abort(404, f'Invalid observation block id. {err}')

    return id


def clean_objectid(docs):
    """
    change ObjectId to string in the result documents so it can be json serialized.

    :param docs: A list of query docs.
    :type docs: List[Dict]

    :rtype: ObjectId
    """
    cln_docs = []
    for result in docs:
        result['_id'] = str(result['_id'])
        cln_docs.append(result)

    return cln_docs


# Observation Block specific
def calc_exec_time(block):
    """
    calculate the total time to execute all observing blocks by exp. time.
    Excludes any read out time and overheads.

    :param block: The observing Block document.
    :type block: Dict

    :rtype: int
    """
    if "properties" not in block:
        return 0

    exp1 = 0
    exp2 = 0
    sci_blk = block["properties"]
    if sci_blk.keys() >= {"det1_exptime", "det1_nexp"}:
        if sci_blk['det1_exptime'] and sci_blk['det1_nexp']:
            exp1 = sci_blk['det1_exptime'] * sci_blk['det1_nexp']

    if sci_blk.keys() >= {"det1_exptime", "det2_exptime",
                          "det1_nexp", "det2_nexp"}:
        if sci_blk['det2_exptime'] and sci_blk['det2_nexp']:
            exp2 = sci_blk['det2_exptime'] * sci_blk['det2_nexp']

    return max(exp1, exp2)


# Container specific helpers
def get_ob_list(container_id):
    """
    :param container_id: container identifier
    :type container_id: str

    :rtype: List[str]
    """
    results = get_by_id(container_id, 'containerCollect')

    if results and type(results) is list:
        ob_list = results[0]['observation_blocks']
    else:
        ob_list = []

    return ob_list


# semesters_and_program specific
def get_proposal_ids(obs_id):
    """
        :param obs_id: observer id
    :type obs_id: int
    """
    cmd_url = f'?cmd=getAllProposals&obsid={obs_id}&json=True'
    result = query_proposals_api(cmd_url)

    if not result['success'] or 'data' not in result:
        return result['msg']

    prop_ids = []
    all_props = result['data']['AllProposals']
    for prop in all_props:
        if "KTN" not in prop:
            continue
        prop_ids.append(prop["KTN"])

    return prop_ids


def get_ids(sem_id):
    cmd_url = f"?cmd=getOBSID&ktn={sem_id}&json=True"
    result = query_proposals_api(cmd_url)

    if not result['success'] or 'data' not in result:
        return result['msg']

    return result['data']


def query_proposals_api(cmd_url):
    with current_app.app_context():
        urls = current_app.urls

    if 'proposalApi' not in urls:
        return None

    url = urls['proposalApi'] + cmd_url

    response = requests.get(url)
    try:
        result = json.loads(response.content)
        return result
    except Exception as err:
        return err


def obs_id_associated(sem_id, obs_id):
    """
    Check that an observer id is associated with a semester id.

    :param sem_id: semester id
    :type sem_id: str
    :param obs_id: observer id
    :type obs_id: int

    """
    sem_ids = get_proposal_ids(obs_id)

    # check that the observer is associated with the sem_id passed in.
    if sem_id not in sem_ids:
        return False

    return True


#validation specific
def check_required(properties, filled):
    """
    This trusts that the template keys have already been checked to exist.
    """

    type_map = {'integer': int, 'float': float, 'string': str, 'array': list,
                'boolean': bool}

    for key in properties:
        if properties[key]['optionality'] != 'required':
            continue

        if key not in filled or not filled[key]:
            abort(422, f"Observation Block is missing key {key}")

        ob_value = filled[key]
        template_properties = properties[key]

        if not check_type(ob_value, template_properties['type'],
                          type_map[template_properties['type']]):
            abort(422, f"{ob_value} is not of type: "
                       f"{template_properties['type']}.")

        if not check_allowed(ob_value, template_properties):
            abort(422, f"{ob_value} is is not within values: "
                       f"{template_properties['allowed']}")

        return True


def check_type(val, key_type, key_py_type):
    if not isinstance(val, key_py_type):
        if key_type == 'float':
            if isinstance(val, int):
                return True

        return False

    return True


def check_allowed(ob_value, template_properties):
    allowed_type = template_properties['option']
    allowed = template_properties['allowed']

    if allowed_type == 'range':
        if ob_value < allowed[0] or ob_value > allowed[1]:
            return False

    if allowed_type == 'list':
        if ob_value not in allowed:
            return False

    if allowed_type == 'boolean':
        if isinstance(ob_value, bool):
            return False

    return True




