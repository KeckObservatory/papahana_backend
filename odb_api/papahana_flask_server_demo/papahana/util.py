import datetime
import six
import typing
import yaml
import pymongo
import urllib
from getpass import getpass
import os
from flask import current_app


def read_mode(config='./config.live.yaml'):
    with open(config) as file:
        mode_dict = yaml.load(file, Loader=yaml.FullLoader)['mode']

    if 'config' in mode_dict:
        return mode_dict['config']
    else:
        return 'production'


def read_config(mode, config='./config.live.yaml'):
    with open(config) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)[mode]

    return config


def read_urls(config='./config.live.yaml'):
    with open(config) as file:
        urls = yaml.load(file, Loader=yaml.FullLoader)['apis']

    return urls


def config_collection(collection, conf=None):
    if not conf:
        with current_app.app_context():
            conf = current_app.config_params

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

# swagger generated below here

def _deserialize(data, klass):
    """Deserializes dict, list, str into an object.

    :param data: dict, list or str.
    :param klass: class literal, or string of class name.

    :return: object.
    """
    if data is None:
        return None

    if klass in six.integer_types or klass in (float, str, bool):
        return _deserialize_primitive(data, klass)
    elif klass == object:
        return _deserialize_object(data)
    elif klass == datetime.date:
        return deserialize_date(data)
    elif klass == datetime.datetime:
        return deserialize_datetime(data)
    elif type(klass) == typing.GenericMeta:
        if klass.__extra__ == list:
            return _deserialize_list(data, klass.__args__[0])
        if klass.__extra__ == dict:
            return _deserialize_dict(data, klass.__args__[1])
    else:
        return deserialize_model(data, klass)


def _deserialize_primitive(data, klass):
    """Deserializes to primitive type.

    :param data: data to deserialize.
    :param klass: class literal.

    :return: int, long, float, str, bool.
    :rtype: int | long | float | str | bool
    """
    try:
        value = klass(data)
    except UnicodeEncodeError:
        value = six.u(data)
    except TypeError:
        value = data
    return value


def _deserialize_object(value):
    """Return a original value.

    :return: object.
    """
    return value


def deserialize_date(string):
    """Deserializes string to date.

    :param string: str.
    :type string: str
    :return: date.
    :rtype: date
    """
    try:
        from dateutil.parser import parse
        return parse(string).date()
    except ImportError:
        return string


def deserialize_datetime(string):
    """Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :type string: str
    :return: datetime.
    :rtype: datetime
    """
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
        return string


def deserialize_model(data, klass):
    """Deserializes list or dict to model.

    :param data: dict, list.
    :type data: dict | list
    :param klass: class literal.
    :return: model object.
    """
    instance = klass()

    if not instance.swagger_types:
        return data

    for attr, attr_type in six.iteritems(instance.swagger_types):
        if data is not None \
                and instance.attribute_map[attr] in data \
                and isinstance(data, (list, dict)):
            value = data[instance.attribute_map[attr]]
            setattr(instance, attr, _deserialize(value, attr_type))

    return instance


def _deserialize_list(data, boxed_type):
    """Deserializes a list and its elements.

    :param data: list to deserialize.
    :type data: list
    :param boxed_type: class literal.

    :return: deserialized list.
    :rtype: list
    """
    return [_deserialize(sub_data, boxed_type)
            for sub_data in data]


def _deserialize_dict(data, boxed_type):
    """Deserializes a dict and its elements.

    :param data: dict to deserialize.
    :type data: dict
    :param boxed_type: class literal.

    :return: deserialized dict.
    :rtype: dict
    """
    return {k: _deserialize(v, boxed_type)
            for k, v in six.iteritems(data)}
