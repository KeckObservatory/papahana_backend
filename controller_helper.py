import pymongo

def create_collection(dbName, collName, port=27017):
    dbUrl = f'mongodb://localhost:{port}/'
    client = pymongo.MongoClient(dbUrl)
    db = client[dbName]
    coll = db[collName]
    return coll

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
    group = group_distinct_signature('semester')
    pipeline = [
        match,
        group
    ]
    return coll.aggregate(pipeline)

def get_semesters_by_pi(piName, coll):
    match = create_signature_match(coll, {'pi': piName})
    project = project_signature_fields('semester')
    pipeline = [ match, project ]
    return coll.aggregate(pipeline)

def get_ob_by_semester(semid, coll):
    match = create_signature_match(coll, {'semester': semid})
    pipeline = [ match, project ]
    return coll.aggregate(pipeline)

def get_ob_by_semester_observer(semid, observer, coll):
    match = create_signature_match(coll, {'semester': semid, 'observers': observer})
    pipeline = [ match ]
    return coll.aggregate(pipeline)

def find_by_pi(name, coll):
    query = {
        "signature.pi": name
    }
    return coll.find(query)

def find_by_semester_program(semester, program, coll):
    query = {
        "signature.semester": semester,
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

def find_by_observer_container(observer, container, coll):
    query = {
        "signature.observers": {
            "$in": [observer]
        },
        "signature.container": container
    }
    return coll.find(query)
