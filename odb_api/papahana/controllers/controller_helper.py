import pymongo
import bson
import json
import requests
from flask import current_app, abort
from bson import json_util

from papahana.util import config_collection

# Generalized
def list_with_objectid(results):
    """
    unwrap a list of dictionaries that include ObjectIds
    :param results: the results
    :type results: dict
    :rtype : List[Dict{Query Result}]
    """
    if not results:
        return []

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


def query_by_id(obj_id, add_delete=True):
    """
    query by string container_id
    :param obj_id: object id string
    :type obj_id: str
    :param cln_oid: restrict results to exclude status=deleted.
    :type cln_oid: bool
    :rtype: Dict{Query}
    """
    obj_id = get_object_id(obj_id)

    if add_delete:
        return {"_id": obj_id, "status.deleted": False}
    else:
        return {"_id": obj_id}


def get_by_id(id, collect_name, db_name=None, cln_oid=True):
    """
    query by string container_id
    :param id: object id string
    :type id: str
    :param collect_name: the database collection.
    :type collect_name: str
    :param cln_oid: set to True to change object id to string in results.
    :type cln_oid: bool
    :rtype: Dict{Query Result}
    """
    if collect_name == 'obCollect':
        query = query_by_id(id)
    else:
        query = query_by_id(id, add_delete=False)

    coll = config_collection(collect_name, db_name=None)

    results = list(coll.find(query))
    if not results:
        abort(404, f'No results in: {collect_name} for id: {id}')

    if cln_oid:
        return json_with_objectid(results[0])

    return results[0]


def get_by_query(query, collect_name, db_name=None):
    """
    query the database by input query pararmeters for all fields in a document.
    :param query: json query parameter
    :type query: dict
    :param collect_name: the database collection.
    :type collect_name: str
    :rtype: List[Dict{Query Result}]
    """
    coll = config_collection(collect_name, db_name=None)
    if "status.deleted" not in query and collect_name == 'obCollect':
        query["status.deleted"] = False

    return list(coll.find(query))


def get_fields_by_query(query, fields, collect_name, db_name=None):
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
    coll = config_collection(collect_name, db_name=db_name)
    if "status.deleted" not in query and collect_name == 'obCollect':
        query["status.deleted"] = False

    return list(coll.find(query, fields))


def get_fields_by_id(ob_id, fields, collect_name, db_name=None):
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
    coll = config_collection(collect_name, db_name=db_name)
    if collect_name == 'obCollect':
        query = query_by_id(ob_id)
    else:
        query = query_by_id(ob_id, add_delete=False)

    results = list(coll.find(query, fields))
    if not results:
        return None

    return results[0]


def insert_into_collection(doc, collect_name, db_name=None):
    """
    Add a new document to a collection.
    :param doc: the document to insert
    :type doc: dict
    :param collect_name: the database collection.
    :type collect_name: str
    rtype: document id
    """
    coll = config_collection(collect_name, db_name=None)

    if "_id" in doc:
        del doc["_id"]
    try:
        result = coll.insert_one(doc)
    except Exception as err:
        return err

    if isinstance(result, pymongo.results.InsertOneResult):
        return result.inserted_id

    return result


def delete_from_collection(query, collect_name, db_name=None):
    """
    Delete document from a database collection.
    :param query: the query used to find the document
    :type query: dict
    :param collect_name: the database collection.
    :type collect_name: str
    """
    coll = config_collection(collect_name, db_name=None)

    try:
        coll.delete_one(query)
        return 0
    except Exception as err:
        print(err)
        return 1


def delete_by_id(obj_id, collect_name, db_name=None):
    """
    Delete a document in a database collection.
    :param id: the document id
    :type query: str / ObjectId
    :param collect_name: the database collection.
    :type collect_name: str
    :rtype (int) 1 on error,  0 on success
    """
    obj_id = get_object_id(obj_id)

    coll = config_collection(collect_name, db_name=None)

    try:
        coll.delete_one({'_id': obj_id})
        return 0
    except Exception as err:
        abort(400, f'Error while deleting by id,  error: {err}.')


def replace_doc(obj_id, doc, collect_name, db_name=None):
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
    obj_id = get_object_id(obj_id)

    coll = config_collection(collect_name, db_name=None)

    try:
        result = coll.replace_one({'_id': obj_id}, doc)
    except Exception as err:
        return err

    return result


def update_doc(query, new_vals, collect_name, db_name=None, clear=False):
    """
    Update a database collection document.
    :param query: the query used to find the document
    :type query: dict
    :param new_vals: the key/val pair of new values to update.
    :type new_vals: dict
    :param collect_name: the database collection.
    :type collect_name: str
    :param clear: remove all fields that are not in new_vals
    :type collect_name: bool
    """
    coll = config_collection(collect_name, db_name=db_name)

    fields_to_update = new_vals.keys()

    if clear:
        doc = list(coll.find(query))
        if doc:
            for field in doc[0].keys():
                if field == '_id' or field in fields_to_update:
                    continue
                coll.update_one(query, {"$unset": {field: 1}})

    if '_id' in fields_to_update:
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


def get_object_id(obj_id):
    """
    transform an ObjectId string to ObjectId
    :param obj_id: ObjectId string
    :type obj_id: str
    :rtype: ObjectId
    """
    try:
        obj_id = bson.objectid.ObjectId(obj_id)
    except bson.errors.InvalidId:
        abort(404, f'Invalid Object Id: {obj_id}')
    except Exception as err:
        abort(404, f'Invalid Object Id: {obj_id}, error: {err}')

    return obj_id


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


# Container specific helpers
def get_ob_list(container_id):
    """
    :param container_id: container identifier
    :type container_id: str
    :rtype: List[str]
    """
    results = get_by_id(container_id, 'containerCollect')

    if results:
        ob_list = results['observation_blocks']
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
    response.close()
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
def check_required_values(parameters, filled):
    """
    This trusts that the template keys have already been checked to exist.
    """

    type_map = {'integer': int, 'float': float, 'string': str, 'array': list,
                'boolean': bool}

    for param in parameters:
        if parameters[param]['optionality'] != 'required':
            continue

        if param not in filled or not filled[param]:
            abort(422, f"Observation Block is missing parameter: {param}")

        ob_value = filled[param]
        parameter_properties = parameters[param]

        if not check_type(ob_value, type_map[parameter_properties['type']]):
            abort(422, f"{ob_value} is not of type: "
                       f"{parameter_properties['type']}.")

        if not check_allowed(ob_value, parameter_properties):
            abort(422, f"{ob_value} is is not within values: "
                       f"{parameter_properties['allowed']}")

        return True


def check_type(val, key_py_type):
    if not isinstance(val, key_py_type):
        if key_py_type == float:
            if isinstance(val, int):
                return True

        return False

    return True

# ---------------------------------
# Observation Block Specific Utils
# ---------------------------------

def check_allowed(ob_value, template_parameters):
    allowed_type = template_parameters['option']
    allowed = template_parameters['allowed']

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


def calc_duration(ob_id):
    """
    Determine the duration of an observation block.
    :param ob_id: observation block ObjectId
    :type: dict
    :rtype: float (minutes)
    """
    query = query_by_id(ob_id)
    fields = {'observations': 1}

    results = get_fields_by_query(query, fields, 'obCollect')
    if not results:
        return 0

    observations = results[0]['observations']

    total_tm = 0
    param_set = ('det1_exptime', 'det1_nexp', 'det2_exptime', 'det2_nexp')
    for obs in observations:
        params = zero_parameters(obs["parameters"], param_set)
        total_tm += (params['det1_exptime'] * params['det1_nexp'] +
                     params['det2_exptime'] * params['det2_nexp'])

    return total_tm / 60.0


def zero_parameters(params, param_set):
    """
    Determine the duration of an observation block.
    :param params: the dictionary of parameters
    :rtype: dict
    :param param_set: a set of parameter names (dict keys) to check.
    :rtype: set
    """
    for param_name in param_set:
        if param_name not in params:
            params[param_name] = 0

    return params


def get_observable_range():
    return [None, None]


def odt_ob_query(query, fields, instrument, min_ra, max_ra, ob_priority,
                 min_priority, max_priority, min_duration, max_duration,
                 state, observable, completed):
    """
    :param query: The initial query to add the params to.
    :type query: dict | bytes
    :param fields: The result fields to return,  an empty {} returns all.
    :type fields: dict | bytes
    :param instrument: instrument used to make observation
    :type instrument: dict | bytes
    :param min_ra: the minimum right ascension
    :type min_ra: dict | bytes
    :param max_ra: the maximum right ascension
    :type max_ra: dict | bytes
    :param ob_priority: return results with a given priority.
    :type ob_priority: int
    :param min_priority: only return results with priority greater than or
                         equal to minimum.
    :type min_priority: int
    :param max_priority: only return results with priority less than to max.
    :type max_priority: int
    :param min_duration: only return results that have a duration greater than
                         or equal to the min_duration.  The duration unit is
                         minutes.
    :type min_duration: float
    :param max_duration: only return results that have a duration less than
                        or equal to the max_duration.  The duration unit is
                        minutes.
    :type max_duration: float
    :param state: return OBs of a certain state,  the possible states are
                  defined in ‘Defined Types’.
    :type state: str
    :param observable: only return results that are observable for current UT
                       to sunrise.  The duration is not taken into consideration.
                       Default is false (0),  use observable for only OBs that
                       are observable.
    :type observable: bool
    :param completed: return results that are completed.  The default is false,
                      use completed for only OBs that are observable.
    :type completed: bool
    :rtype: List
    """

    if instrument:
        query['metadata.instrument'] = instrument
    if ob_priority:
        query['metadata.priority'] = int(ob_priority)

    # [0 = partial, 1 = ready, 2 = ongoing, 3 = complete, 4 = aborted]
    if completed:
        query['status.state'] = 3
    elif state:
        query['status.state'] = int(state)

    else:
        if min_priority and max_priority:
            query["status.priority"] = {"$gt": int(min_priority),
                                        "$lt": int(max_priority)}
        elif min_priority:
            query["status.priority"] = {"$gt": int(min_priority)}
        elif max_priority:
            query["status.priority"] = {"$lt": int(max_priority)}

    # TODO need dcs keyword access
    # if observable:
    #     min_ra, max_ra = restrict2observable(min_ra, max_ra)

    if min_ra and max_ra:
        query["target.target_coord_ra"] = {"$gt": min_ra, "$lt": max_ra}
    elif min_ra:
        query["target.target_coord_ra"] = {"$gt": min_ra}
    elif max_ra:
        query["target.target_coord_ra"] = {"$lt": max_ra}

    matching_ob = parse_duration(get_fields_by_query(query, fields, 'obCollect'),
                                 min_duration, max_duration)

    return matching_ob


def parse_duration(matching_ob, min_duration, max_duration):
    if not matching_ob:
        return None

    if min_duration or max_duration:
        parsed_matches = []
        for match in matching_ob:
            min_ok = False
            max_ok = False
            duration = calc_duration(match["_id"])
            if not min_duration or duration >= min_duration:
                min_ok = True
            if not max_duration or duration <= max_duration:
                max_ok = True
            if min_ok and max_ok:
                parsed_matches.append(match)

        matching_ob = parsed_matches

    return matching_ob

# TODO find an API for current RA?
def restrict2observable(min_ra, max_ra):
    """
    [k1obstcs@k1obs data]$ show -s dcs lst
                           lst = 00:33:10.07 h
    """
    observable_range = get_observable_range()

    if not min_ra or observable_range[0] > min_ra:
        min_ra = observable_range[0]
    if not max_ra or observable_range[1] < max_ra:
        max_ra = observable_range[1]

    return min_ra, max_ra
