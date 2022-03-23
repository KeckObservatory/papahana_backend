import connexion
import six

from papahana.models.apikey import Apikey
from papahana.models.observer_list import ObserverList  
from papahana.models.sem_id_schema import SemIdSchema  
from papahana import util

from papahana.controllers import controller_helper as utils
from papahana.controllers import observers_controller_utils as obs_utils

# TODO use for testing
# TMP_KECKID = 1883 # real PI (for external APIs)
TMP_KECKID = 1883
TMP_APIKEY = 99689645


def observer_apikey():
    """observer_apikey
        /observers/apikey

    Get the apikey for the authenticated observer.   Requires the browser
    to be logged in via the keck login page.

    :rtype: Apikey
    """
    # undefined
    # keck_id = 8899

    # TODO replace with deserialize cookie
    # John
    keck_id = 1883

    query = {"keck_id": keck_id}
    fields = {'api_key': 1, '_id': 0}
    results = utils.get_fields_by_query(query, fields, 'observerCollect')
    if not results:
        return {}

    return results[0]


def observer_keckid(api_key):
    """observer_keckid
        /observers/keckid/{api_key}

    Get the Keck ID associated with the API Key.  The API Key is
    a required parameter.

    :rtype: KeckId
    """
    query = {'api_key': api_key}
    fields = {'keck_id': 1, '_id': 0}
    results = utils.get_fields_by_query(query, fields, 'observerCollect')
    if not results:
        return {}

    return results[0]


def observer_view(sem_id):
    """observer_view
        /observers/{sem_id}/view

    view the list of observers associated with the sem_id (program).  The list
    will include the Keck IDs.

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


def observer_semid():
    """observer_semid
        /observers/semesterIds

    view the list of semester IDs (programs) that the observers is associated.

    :rtype: ObserverList
    """

    #TODO get id from cookie
    # keck_id = 7799
    keck_id = TMP_KECKID

    query = {'keck_id': keck_id}
    fields = {'keck_id': 1, '_id': 0, 'associations': 1}

    results = utils.get_fields_by_query(query, fields, 'observerCollect')
    if results:
        results = results[0]
    else:
        results = {'keck_id': keck_id, 'associations': []}

    proposal_sem_ids = utils.get_proposal_ids(keck_id)

    if type(proposal_sem_ids) is not list:
        proposal_sem_ids = {}
    else:
        for sem_id in proposal_sem_ids:
            obs_utils.add_association(keck_id, sem_id)

    results['associations'] += proposal_sem_ids

    # TODO will also need to go out and check schedule

    return results
#
# def add_association(keck_id, sem_id):
#     from papahana.util import config_collection
#
#     coll = config_collection('observerCollect')
#     _ = coll.update_one({"keck_id": keck_id}, {"$addToSet": {"associations": sem_id}})
#
#
# def is_associated(keck_id, sem_id):
#     query = {'keck_id': keck_id}
#     fields = {'keck_id': 1, '_id': 0, 'associations': 1}
#
#     results = utils.get_fields_by_query(query, fields, 'observerCollect')
#     if results:
#         for assoc_sem_id in results[0]['associations']:
#             if assoc_sem_id == sem_id:
#                 return True
#
#     proposal_sem_ids = utils.get_proposal_ids(keck_id)
#
#     if type(proposal_sem_ids) is not list:
#         return False
#
#     for assoc_sem_id in proposal_sem_ids:
#         if assoc_sem_id == sem_id:
#             return True
#
#     return False
#



# def update_associations(sem_id):


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
