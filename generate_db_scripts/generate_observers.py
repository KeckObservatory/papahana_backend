import generate_random_utils as random_utils
from papahana import util as papahana_util
from papahana.controllers import authorization_utils as auth_utils


def generate_observer_collection(config, coll):
    n_obs = 15
    # percy = 4000, Josh = 4012, Marc = 2495, Carlos = 3928, Jem = 2205,
    # Greg = 2983, Sherry = 4098, randy = 2883, Chien-Hsiu = 3986, Mike = 4927
    # John = 1883 Jeff = 2204 Matt = 4224

    staff = [4000, 4012, 2495, 3928, 2205, 2983, 4098, 2883,
             3986, 4927, 1883, 2204, 4224]

    keck_admin = config['admin']

    keck_id_list = set()
    for obs in range(0, n_obs):
        keck_id_list.add(random_utils.randKeckId())

    for obs_id in keck_id_list:
        sem_id_list = []
        for indx in range(0,random_utils.randInt(2,10)):
            sem_id_list.append(random_utils.randSemId())

        akey = auth_utils.generate_new_api_key()

        doc = {'keck_id': obs_id, "api_key": akey, "associations": sem_id_list,
               'admin': 0}
        _ = coll.insert_one(doc)

    # create staff
    for obs_id in staff:
        akey = auth_utils.generate_new_api_key()
        doc = {'keck_id': obs_id, "api_key": akey, "associations": [],
               'admin': 0}
        _ = coll.insert_one(doc)

    assoc_list = []

    # create admin observer
    coll = papahana_util.config_collection('obCollect', conf=config)

    fields = {'metadata.sem_id': 1, '_id': 0}
    sem_ids = list(coll.find({}, fields))
    for result in sem_ids:
        assoc_list.append(result['metadata']['sem_id'])

    coll = papahana_util.config_collection('observerCollect', db_name='obs_db',
                                           conf=config)

    for admin_id in keck_admin:
        akey = auth_utils.generate_new_api_key()
        assoc_unique = list(set(assoc_list))
        doc = {'keck_id': admin_id, "api_key": akey,
               "associations": assoc_unique, "admin": 1}
        _ = coll.insert_one(doc)

    return
