import datetime
import six
import yaml
import pymongo
from collections import OrderedDict

from flask import current_app

# for history
from papahana.historical import HistoricalCollection

CONFIG_FILE = './config.live.yaml'

class observation_blocks(HistoricalCollection):
    # define the primary key for the Historical Collection
    PK_FIELDS = ['_ob_id', ]


def read_mode():
    with open(CONFIG_FILE) as file:
        mode_dict = yaml.load(file, Loader=yaml.FullLoader)['mode']

    if 'config' in mode_dict:
        return mode_dict['config']
    else:
        return 'production'


def read_config(mode):
    with open(CONFIG_FILE) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)[mode]

    return config


def config_file_section(section_name):
    with open(CONFIG_FILE) as file:
        section_dict = yaml.load(file, Loader=yaml.FullLoader)[section_name]

    return section_dict


def read_urls():
    with open(CONFIG_FILE) as file:
        urls = yaml.load(file, Loader=yaml.FullLoader)['apis']

    return urls


def config_collection(collection, db_name=None, conf=None):
    if not conf:
        with current_app.app_context():
            conf = current_app.config_params

    if not db_name:
        db_name = 'ob_db'

    db = conf[db_name]
    mongo_port = conf['mongo_port']

    if collection == 'obCollect':
        CLIENT_URL = f"mongodb://{conf['ip']}:{mongo_port}"
        mongo = pymongo.MongoClient(CLIENT_URL, document_class=OrderedDict)
        db = mongo[db]
        coll = observation_blocks(database=db)
    else:
        coll = create_collection(db, conf[collection], port=conf['mongo_port'],
                                 ip=conf['ip'])

    return coll



def create_collection(db_name, collect_name, port=27017, ip='127.0.0.1'):
    """ create_collection

    Creates and returns a mongodb collection object

    :param db_name: database name
    :type db_name: str
    :param collect_name: collection name
    :type collect_name: str
    :port: port name
    :type port: int
    :dbURL: url of database (use for databases)
    :dbURL: str
    :rtype: pymongo.collection.Collection
    """
    db_url = f'mongodb://{ip}:{port}'

    client = pymongo.MongoClient(db_url, document_class=OrderedDict)
    db = client[db_name]
    coll = db[collect_name]

    return coll


def drop_db(db_name, port=27017, ip='127.0.0.1'):
    db_url = f'mongodb://{ip}:{port}'
    client = pymongo.MongoClient(db_url, document_class=OrderedDict)
    client.drop_database(db_name)


# -----------------------------
# swagger generated below here
# -----------------------------


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
    elif hasattr(klass, '__origin__'):
        if klass.__origin__ == list:
            return _deserialize_list(data, klass.__args__[0])
        if klass.__origin__ == dict:
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
