import pymongo
import urllib
from getpass import getpass
import yaml
import os

def config_collection(mode='dev', config='config.live.yaml'):
    with open('config.live.yaml') as file:
        conf = yaml.load(file, Loader=yaml.FullLoader)[mode]
    if mode == 'dev':
        coll = create_collection(conf['dbName'], conf['obCollectionName'], conf['port'])
    elif mode == 'demo':
        coll = create_collection(conf['dbName'], conf['obCollectionName'], remote=True, username=conf['username'], password=conf['password'])
    else:
        raise ValueError('collection mode not known')
    return coll
    
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
    elif os.environ['DOCKER_DATABASE_CONNECTION']:
        dbURL = f'mongodb://database:{port}'
    else:
        dbURL = f'mongodb://127.0.0.1:{port}'
    client = pymongo.MongoClient(dbURL)
    db = client[dbName]
    coll = db[collName]
    return coll

coll = config_collection('dev', config='./config.live.yaml')