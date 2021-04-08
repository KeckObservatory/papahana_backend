import connexion
import six

from swagger_server.models.observation_block import ObservationBlock  # noqa: E501
from swagger_server import util


def obs_block_delete(ob_id):  # noqa: E501
    """obs_block_delete

    Removes the observation block) # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: None
    """
    return 'do some magic!'


def obs_block_duplicate(ob_id, sem_id):  # noqa: E501
    """obs_block_duplicate

    Duplicate the OB, default is current semId. # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str
    :param sem_id: program id
    :type sem_id: str

    :rtype: ObservationBlock
    """
    return 'do some magic!'


def obs_block_get(ob_id):  # noqa: E501
    """obs_block_get

    Retrieves the general parameters of an OB (target, exec time, other as needed) # noqa: E501

    :param ob_id: observation block id
    :type ob_id: str

    :rtype: ObservationBlock
    """
    return 'do some magic!'


def obs_block_post(body):  # noqa: E501
    """obs_block_post

    Inserts an observation block. # noqa: E501

    :param body: Observation block to be added.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ObservationBlock.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def obs_block_put(body, ob_id):  # noqa: E501
    """obs_block_put

    Updates the observation block with the new one) # noqa: E501

    :param body: Observation block replacing ob_id.
    :type body: dict | bytes
    :param ob_id: observation block id
    :type ob_id: str

    :rtype: ObservationBlock
    """
    if connexion.request.is_json:
        body = ObservationBlock.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
