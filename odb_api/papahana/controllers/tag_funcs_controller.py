import connexion
import six

from papahana import util
from papahana.controllers import controller_helper as utils
from papahana.controllers import tag_funcs_utils as tags_utils


def tags_add(tag_name, ob_id):  
    """tags_add

    Add a Tag to an Observation Block. 

    :param tag_name: a tag to search on
    :type tag_name: str
    :param ob_id: observation block ObjectId
    :type ob_id: str

    :rtype: List
    """
    obj_id = utils.get_object_id(ob_id)

    # get the sem_id from the OB
    sem_id = tags_utils.get_ob_sem_id(obj_id)

    # get tag obj_id
    tag_id = tags_utils.get_tag_oid(sem_id, tag_name)

    # add tag if it doesn't exist,  or already in the list
    if not tag_id:
        tag_id = tags_utils.add_tag(sem_id, tag_name)
    elif tags_utils.tag_is_in_ob(obj_id, tag_id):
        return tags_all(ob_id)

    # update the tag_list in the OB
    query = {'_id': obj_id}
    new_vals = {'metadata.tags': tag_id}
    utils.update_add_doc(query, new_vals, 'obCollect')

    return tags_all(ob_id)


def tags_all(ob_id):
    """tags_all

    Retrieve all Tag Names for an Observation Block.

    :param ob_id: observation block ObjectId
    :type ob_id: str

    :rtype: List
    """
    tag_dict = tags_utils.get_tag_list(ob_id)
    if not tag_dict:
        return {"tags": []}

    tag_name_list = []
    for tag_id in tag_dict['tags']:
        tag_name_list.append(tags_utils.get_tag_name(tag_id))

    return {"tags": tag_name_list}


def tags_delete(tag_name, ob_id):  
    """tags_delete

    Delete a Tag to an Observation Block. 

    :param tag_name: a tag to search on
    :type tag_name: str
    :param ob_id: observation block ObjectId
    :type ob_id: str

    :rtype: List
    """
    obj_id = utils.get_object_id(ob_id)

    # get the sem_id from the OB
    sem_id = tags_utils.get_ob_sem_id(obj_id)

    # get tag object_id from tag_name
    tag_id = tags_utils.get_tag_oid(sem_id, tag_name)

    # not in list
    if not tags_utils.tag_is_in_ob(obj_id, tag_id):
        return tags_all(ob_id)

    # remove object_id from ob tag obj_id list
    query = {'_id': obj_id, 'metadata.tags': tag_id}
    remove_val = {'metadata.tags': tag_id}
    utils.update_remove_element(query, remove_val, 'obCollect')

    return tags_all(ob_id)

