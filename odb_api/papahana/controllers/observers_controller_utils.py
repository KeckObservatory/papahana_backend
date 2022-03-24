from papahana.util import config_collection
from papahana.controllers import controller_helper as utils


def add_association(keck_id, sem_id):
    coll = config_collection('observerCollect')
    _ = coll.update_one({"keck_id": keck_id}, {"$addToSet": {"associations": sem_id}})


def is_associated(keck_id, sem_id):
    query = {'keck_id': keck_id}
    fields = {'keck_id': 1, '_id': 0, 'associations': 1}

    results = utils.get_fields_by_query(query, fields, 'observerCollect')
    if results:
        for assoc_sem_id in results[0]['associations']:
            if assoc_sem_id == sem_id:
                return True

    proposal_sem_ids = utils.get_proposal_ids(keck_id)

    if type(proposal_sem_ids) is not list:
        return False

    for assoc_sem_id in proposal_sem_ids:
        if assoc_sem_id == sem_id:
            return True

    return False


