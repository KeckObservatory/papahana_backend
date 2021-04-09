import pdb
import connexion
import six

from swagger_server.models.observation_block import ObservationBlock  # noqa: E501
from swagger_server import util

from . import controller_helper as helper

coll = helper.config_collection('dev', config='./../../config.live.yaml')


def obs_block_delete(ob_id):  # noqa: E501
    """obs_block_delete

    Removes the observation block) # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    response = helper.delete_observation_block(ob_id, coll)
    return str(response)

def obs_block_duplicate(ob_id, sem_id):  # noqa: E501
    """obs_block_duplicate

    Duplicate the OB, default is current semId. # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str
    :param sem_id: program id
    :type sem_id: str

    :rtype: ObservationBlock
    """
    obs = list(helper.get_ob_by_id(ob_id, coll))
    assert len(docs) == 1, 'not found'
    ob = obs[0] 
    ob.pop('_id')
    result = helper.insert_observation_block(ob, coll)
    return str(result) 


def obs_block_get(ob_id):  # noqa: E501
    """obs_block_get

    Retrieves the general parameters of an OB (target, exec time, other as needed) # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: [ObservationBlock]
    """
    ob = list(helper.get_ob_by_id(ob_id, coll))
    return ob 

def obs_block_post(body):  # noqa: E501
    """obs_block_post

    Inserts an observation block. # noqa: E501

    :param body: Observation block to be added.
    :type body: dict | bytes

    :rtype: str. either return or error message
    """
    if connexion.request.is_json:
        obDict = connexion.request.get_json()
        ob = ObservationBlock.from_dict(obDict).to_dict()  # verify if formatted properly

    result = helper.insert_observation_block(obDict, coll)
    return str(result)


def obs_block_put(body, ob_id):  # noqa: E501
    """obs_block_put

    Updates the observation block with the new one # noqa: E501

    :param body: Observation block replacing ob_id.
    :type body: dict | bytes
    :param ob_id: observation block id
    :type ob_id: str

    :rtype: result
    """
    if connexion.request.is_json:
        obDict = connexion.request.get_json()
        ob = ObservationBlock.from_dict(obDict).to_dict()  # verify if formatted properly
        obDict.pop('id') # mongodb uses _id
    result = helper.replace_observation_block(ob_id, obDict, coll)

    return str(result) 
