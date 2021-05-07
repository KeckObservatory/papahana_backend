def create_match(key, item):
    if key == 'observers':
        mItem = { 
            f"signature.observers": {
            "$exists": "true", "$in": [ f"{item}"]
        }}
    else:
        mItem = {
            f"signature.{key}": item
        }
    return mItem

def create_signature_match(coll, qdict):
    '''note matching flattens nested fields'''
    matchItems = [ create_match(key, item) for key, item in qdict.items() ]        
    return {
        "$match": {
            "$and": matchItems
        }
    }
    
def group_distinct_signature(key):
    '''group by one field in aggreate pipeline'''
    return {
            "$group":{
                "_id": { key: f"$signature.{key}" }
            }
        }

def project_fields(*signatureKeys):
    return {"$project": { f"{key}": 1 for key in signatureKeys } }

def project_signature_fields(*signatureKeys):
    return {"$project": { f"signature.{key}": 1 for key in signatureKeys } }
    
def get_distinct_semesters(obsName, coll):
    match = create_signature_match(coll, {'observers': obsName})
    group = group_distinct_signature('semesters')
    pipeline = [
        match,
        group
    ]
    return coll.aggregate(pipeline)

def get_semesters_by_pi(piName, coll):
    match = create_signature_match(coll, {'pi': piName})
    project = project_signature_fields('semesters')
    pipeline = [ match, project ]
    return coll.aggregate(pipeline)

def get_ob_by_semester(semid, coll):
    match = create_signature_match(coll, {'semesters': semid})
    pipeline = [ match ]
    return coll.aggregate(pipeline)

def get_ob_by_semester_observer(semid, observer, coll):
    match = create_signature_match(coll, {'semesters': semid, 'observers': observer})
    pipeline = [ match ]
    return coll.aggregate(pipeline)

def find_by_pi(name, coll):
    query = {
        "signature.pi": name
    }
    return coll.find(query)

def find_by_semester_program(semester, program, coll):
    query = {
        "signature.semesters": {
            "$in": [semester]
        },
        "signature.program": program
    }
    return coll.find(query)

def find_by_observer(observer, coll):
    query = {
        "signature.observers": {
            "$in": [observer]
        }
    }
    return coll.find(query)

def find_by_observer_semester(observer, semester, coll):
    query = {
        "signature.observers": {
            "$in": [observer]
        },
        "signature.semesters": {
            "$in": [semester]
        },
    }
    return coll.find(query)

def get_ob_by_id(_id, coll):
    query = {
        "_id": _id
    }
    return coll.find(query)

def insert_observation_block(ob, coll):
    try:
        result = coll.insert_one(ob)
    except Exception as err:
        return err
    return result
        
def delete_observation_block(_id, coll):
    try:
        coll.delete_one({'_id': _id})
    except Exception as err:
        print(err)

def replace_observation_block(_id, ob, coll):
    try:
        query = {'_id': _id}
        result = coll.replace_one(query, ob)
    except Exception as err:
        print(err)
    return result
        
def update_observation_block(_id, newValues, coll):
    query = {
        "_id": _id
    }
    coll.update_one(query, newValues)
