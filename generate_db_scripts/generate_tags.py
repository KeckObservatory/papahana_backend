import generate_random_utils as random_utils
from papahana import util as papahana_util
import random
from bson.objectid import ObjectId

TAG_NAMES = ["Favorite OBs", "Standard Stars", "Bright", "Faint", "Library"]


# each sem_id has a set of tags
def generate_tag_list(coll):
    keck_id_obj_id = {}
    for keck_id in random_utils.keck_ids:
        keck_id_obj_id[keck_id] = []
        for tag_name in TAG_NAMES:
            tag_schema = {'keck_id': keck_id, 'tag_str': tag_name}
            result = coll.insert_one(tag_schema)
            keck_id_obj_id[keck_id].append(str(result.inserted_id))

    return keck_id_obj_id


def add_tags_to_ob(config, ob, keck_id_obj_id):
    tag_list = []

    coll = papahana_util.config_collection('obCollect', conf=config)
    fields = {'metadata.sem_id': 1}

    # ob_info = list(coll.find({"_id": ObjectId(ob)}, fields))
    keck_id = random_utils.randKeckId()
    for i in range(0, random_utils.randInt(0, len(TAG_NAMES)-1)):
        tag_id = random.choice(keck_id_obj_id[keck_id])
        if tag_id not in tag_list:
            tag_list.append(tag_id)

    coll = papahana_util.config_collection('obCollect', conf=config)
    coll.update_one({'_id': ObjectId(ob)}, {'$set': {'metadata.tags': tag_list}})


