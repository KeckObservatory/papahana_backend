import pymongo

def create_collection(dbName, collName):
    dbUrl = 'mongodb://localhost:27017/'
    client = pymongo.MongoClient(dbUrl)
    db = client[dbName]
    coll = db[collName]
    return coll    

def get_semesters(obsName):
    pipeline = [
        {
            "$match": {
                "$and" : [{
                    'obs_id' : {
                        "$exists": "true", "$in": [ f"{obsName}"]
                    }
                }]
            }
        },
        {
        "$project": {
            "semester": 1,
            }
        }
    ]
    return semColl.aggregate(pipeline)

def find_by_pi(name):
    query = {
        "signature.pi": name
    }
    return coll.find(query)

def find_by_semester_program(semester, program):
    query = {
        "signature.semester": semester,
        "signature.program": program
    }
    return coll.find(query)

def find_by_observer(observer):
    query = {
        "signature.observers": {
            "$in": [observer]
        }
    }
    return coll.find(query)

def find_by_observer_container(observer, container):
    query = {
        "signature.observers": {
            "$in": [observer]
        },
        "signature.container": container
    }
    return coll.find(query)
