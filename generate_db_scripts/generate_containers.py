
import generate_random_utils as random_utils
from papahana import util as papahana_util
from papahana.controllers import controller_helper as helper_utils

import random

def generate_containers(config, coll, ob_blocks):
    nContainers = 20
    container_list = []
    for idx in range(nContainers):
        doc = generate_container(config, ob_blocks)
        result = coll.insert_one(doc)
        container_list.append(str(result.inserted_id))

    return container_list


def generate_container(config, ob_blocks):

    sem_id = random_utils.randSemId()

    coll_ob = papahana_util.config_collection('obCollect', conf=config)

    ob_set = set()
    # n_ob = random.randint(0, 30)
    for indx in range(0, 60):
        ob_val = random.randint(0, len(ob_blocks)-1)
        rand_ob_id = ob_blocks[ob_val]

        query = helper_utils.query_by_id(rand_ob_id)
        rand_ob = list(coll_ob.find(query))
        if not rand_ob:
            continue

        rand_ob = rand_ob[0]

        if not rand_ob:
            continue

        if rand_ob['metadata']['sem_id'] == sem_id:
            ob_set.update({rand_ob_id})

    schema = {
        "sem_id": sem_id,
        "name": random_utils.randContainerName(),
        "observation_blocks": list(ob_set),
        "comment": random_utils.randComment()
    }

    return schema
