import pymongo
import urllib
from getpass import getpass
import os
from flask import current_app


def config_collection(collection, mode=None, conf=None):
    if not mode and not conf:
        with current_app.app_context():
            conf = current_app.config_params
            mode = current_app.mode

    coll = create_collection(conf['dbName'], conf[collection],
                             port=conf['port'], ip=conf['ip'])
    return coll


def create_collection(dbName, collName, port=27017, ip='127.0.0.1',
                      remote=False, username='papahanauser', password=None):
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
    else:
        dbURL = f'mongodb://{ip}:{port}'

    client = pymongo.MongoClient(dbURL)
    db = client[dbName]
    coll = db[collName]

    return coll