import pymongo

def create_collection(dbName, collName, port=27017):
    dbUrl = f'mongodb://localhost:{port}/'
    client = pymongo.MongoClient(dbUrl)
    db = client[dbName]
    coll = db[collName]
    return coll    

def get_semesters(obsName, coll):
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
