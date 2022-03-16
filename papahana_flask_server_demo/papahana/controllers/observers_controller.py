import connexion
import six

from papahana.models.apikey import Apikey
from papahana.models.observer_list import ObserverList  
from papahana.models.sem_id_schema import SemIdSchema  
from papahana import util

from papahana.controllers import controller_helper as utils


def observer_apikey():
    """observer_apikey

    Get the apikey for the autheticated observer. 

    :rtype: Apikey
    """
    return 'do some magic!'


def observer_view(sem_id):
    """observer_view
        /observers/{sem_id}/view

    view the list of observers associated with the sem_id (program).  The list
    will include user’s name,  Keck ID,  and institute.

    :param sem_id: semester id
    :type sem_id: dict | bytes

    :rtype: ObserverList
    """
    if connexion.request.is_json:
        sem_id = SemIdSchema.from_dict(connexion.request.get_json())

    query = {'associations': sem_id}
    fields = {'keck_id': 1, '_id': 0}
    results = utils.get_fields_by_query(query, fields, 'observerCollect')
    if not results:
        return {}

    id_list = []
    for result in results:
        id_list.append(result['keck_id'])

    return {sem_id: id_list}


# def observer_remove(sem_id, keck_id):
#     """observer_remove
#         /observers/{sem_id}/remove/{keck_id}
#
#     remove access to a program for an observer by Keck ID.
#
#     :param sem_id: semester id
#     :type sem_id: dict | bytes
#     :param keck_id: semester id
#     :type keck_id: int
#
#     :rtype: ObserverList
#     """
#     if connexion.request.is_json:
#         sem_id = SemIdSchema.from_dict(connexion.request.get_json())
#
#     return 'do some magic!'

# def observer_add(sem_id, keck_id):
#     """observer_add
#         /observers/{sem_id}/add/{keck_id}
#
#     allow access to a program for an observer by Keck ID.
#
#     :param sem_id: semester id
#     :type sem_id: dict | bytes
#     :param keck_id: semester id
#     :type keck_id: int
#
#     :rtype: ObserverList
#     """
#     if connexion.request.is_json:
#         sem_id = SemIdSchema.from_dict(connexion.request.get_json())
#
#     return 'do some magic!'
