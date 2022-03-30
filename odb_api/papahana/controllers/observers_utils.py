from flask import g

from papahana.util import config_collection
from papahana.controllers import controller_helper as utils


def add_association(keck_id, sem_id):
    coll = config_collection('observerCollect')
    _ = coll.update_one({"keck_id": keck_id}, {"$addToSet": {"associations": sem_id}})


def is_associated(sem_id):
    keck_id = g.user

    query = {'keck_id': keck_id, 'associations': sem_id}
    fields = {'associations': 1, '_id': 0}
    results = utils.get_fields_by_query(query, fields, 'observerCollect')
    if results:
        try:
            if sem_id in results[0]['associations']:
                return True
        except (KeyError, IndexError):
            return False

    proposal_sem_ids = utils.get_proposal_ids(keck_id)

    if type(proposal_sem_ids) is not list:
        return False

    if proposal_sem_ids and sem_id in proposal_sem_ids:
        add_sem_id_db(sem_id)
        return True

    return False


def add_sem_id_db(sem_id):
    keck_id = g.user

    query = {'keck_id': keck_id}
    fields = {'associations': 1, '_id': 0}
    results = utils.get_fields_by_query(query, fields, 'observerCollect')

    assoc_list = []
    if results:
        try:
            assoc_list = results[0]['associations']
        except (KeyError, IndexError):
            pass

    assoc_list.append(sem_id)

    fields = {'associations': assoc_list}
    utils.update_doc(query, fields, 'observerCollect')

    return



