import pymongo
import urllib
from getpass import getpass
import yaml

def config_collection(mode='dev', config='config.live.yaml'):
    with open('config.live.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    conf = yaml.load(file, Loader=yaml.FullLoader)[mode]
    if mode == 'dev':
        coll = create_collection(conf['dbName'], conf['obCollectionName'], conf['port'])
    elif mode == 'demo':
        coll = create_collection(conf['dbName'], conf['obCollectionName'], remote=True, conf['username'], conf['password'])
    coll = create_collection('')
    
def create_collection(dbName, collName, port=27017, remote=False, username='papahanauser', password=None):
    """create_collection
    
    Creates and returns a mongodb collection object
    
    :param dbName: database name
    :type dbName: str
    :param collName: collection name
    :type collName: str
    :port: port name
    :type port: int
    :dbURL: url of database (use for databases)
    :dbURL: str

    :rtype: pymongo.collection.Collection
    """
    if remote:
        if not password:
            password = getpass()
        dbURL = f'mongodb+srv://{urllib.parse.quote(username)}:{urllib.parse.quote(password)}@cluster0.gw51m.mongodb.net/{dbName}'
    else:
        dbURL = f'mongodb://localhost:{port}/'
    client = pymongo.MongoClient(dbURL)
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
    pipeline = [ match ]
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

def get_ob_by_id(_id, coll):
    query = {
        "_id": _id
    }
    return coll.find(query)

def insert_observation_block(ob, coll):
    try:
        coll.insert_one(ob)
    except Exception as err:
        print(err)
        
def delete_observation_block(_id, coll):
    try:
        coll.delete_one({'_id': _id})
    except Exception as err:
        print(err)
        
def update_observation_block(_id, newValues, coll):
    query = {
        "_id": _id
    }
    coll.update_one(query, newValues)
