import pymongo
import urllib
from getpass import getpass
import yaml
import os


def read_mode(config='config.live.yaml'):
    with open(config) as file:
        mode = yaml.load(file, Loader=yaml.FullLoader)['mode']

    return mode['config']


def config_collection(collection, config='config.live.yaml'):
    mode = read_mode()

    with open(config) as file:
        conf = yaml.load(file, Loader=yaml.FullLoader)[mode]
    if mode == 'dev':
        coll = create_collection(conf['dbName'], conf[collection], mode, port=conf['port'])
    elif mode == 'demo':
        coll = create_collection(conf['dbName'], conf[collection], mode, remote=True,
                                 username=conf['username'], password=conf['password'])
    if mode == 'local':
        coll = create_collection(conf['dbName'], conf[collection], mode, port=conf['port'])
    else:
        raise ValueError('collection mode not known')
    return coll


def create_collection(dbName, collName, mode, port=27017, remote=False, 
                      username='papahanauser', password=None):
    """ create_collection
    
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
        dbURL = f'mongodb+srv://{urllib.parse.quote(username)}:' \
                f'{urllib.parse.quote(password)}@cluster0.gw51m.mongodb.net/' \
                f'{dbName}'
    elif os.environ.get('DOCKER_DATABASE_CONNECTION', False):
        dbURL = f'mongodb://database:{port}'
    elif mode == 'dev':
        dbURL = f'mongodb://10.96.0.228:{port}'
    elif mode == 'local':
        dbURL = f'mongodb://127.0.0.1:{port}'
    else:
        dbURL = f'mongodb://127.0.0.1:{port}'

    client = pymongo.MongoClient(dbURL)
    db = client[dbName]
    coll = db[collName]

    return coll


# coll = config_collection('obCollectionName', 'dev', config='./config.live.yaml')
