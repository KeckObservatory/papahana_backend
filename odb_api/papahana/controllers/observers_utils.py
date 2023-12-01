from flask import g

from papahana.util import config_collection
from papahana.controllers import controller_helper as utils

def chk_observer_sandbox_association(keck_id, sem_id):

    sandbox_sem_id = f'{keck_id}B_D000'
    coll = config_collection('observerCollect', db_name='obs_db')
    results = coll.find_one({'keck_id': keck_id})
    if not sandbox_sem_id in results['associations']:
        _ = coll.update_one({"keck_id": keck_id},
                            {"$addToSet": {"associations": sandbox_sem_id}})

    if sem_id == sandbox_sem_id:
        return True
    return False
        

def add_association(keck_id, sem_id_list):
    coll = config_collection('observerCollect', db_name='obs_db')

    clean_list = []
    for sem_id in sem_id_list:
        try:
            year = int(sem_id[:4])
        except ValueError:
            continue

        if year < 2022:
            continue

        clean_list.append(sem_id)
        _ = coll.update_one({"keck_id": keck_id},
                            {"$addToSet": {"associations": sem_id}})

    return clean_list


def is_semid_associated_args(*args, **kwargs):

    sem_id = kwargs['sem_id']
    return is_semid_associated(sem_id)


def is_semid_associated(sem_id):
    keck_id = g.user

    query = {'keck_id': keck_id}
    fields = {'associations': 1, '_id': 0, 'admin': 1}

    results = utils.get_fields_by_query(query, fields, 'observerCollect',
                                        db_name='obs_db')

    if results:
        try:
            if results[0]['admin']:
                return True

            if sem_id in results[0]['associations']:
                return True

        except (KeyError, IndexError):
            return False

    # check if sandbox association exists, if not then add it
    if chk_observer_sandbox_association(keck_id, sem_id):
        return True

    # check the schedule
    if chk_add_assoc(keck_id, sem_id, utils.get_sched_sem_ids):
        return True

    # check the proposals database
    if chk_add_assoc(keck_id, sem_id, utils.get_proposal_ids):
        return True

    return False


def chk_add_assoc(keck_id, sem_id, func):
    # check the proposals database
    sem_id_list = func(keck_id)

    if sem_id_list and sem_id in sem_id_list:
        _ = add_association(keck_id, sem_id_list)
        return True

    return False


