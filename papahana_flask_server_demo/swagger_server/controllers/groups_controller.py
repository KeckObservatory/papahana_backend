import connexion
import six

from swagger_server.models.group import Group  # noqa: E501
from swagger_server import util


def groups_delete(group_id):  # noqa: E501
    """groups_delete

    Delete group by id # noqa: E501

    :param group_id: group identifier
    :type group_id: str

    :rtype: None
    """
    return 'do some magic!'


def groups_get(group_id):  # noqa: E501
    """groups_get

    Retrieves a specific group&#x27;s information # noqa: E501

    :param group_id: group identifier
    :type group_id: str

    :rtype: Group
    """
    return 'do some magic!'


def groups_post(body):  # noqa: E501
    """groups_post

    Creates a group # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Group.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def groups_put(body, group_id):  # noqa: E501
    """groups_put

    Overwrites a group # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param group_id: group identifier
    :type group_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Group.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
