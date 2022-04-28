import ast

from papahana.controllers import controller_helper as utils
from papahana.controllers import authorization_utils as auth_utils

from papahana.models.container import Container


def container2dict(container_obj):
    return ast.literal_eval(str(container_obj).replace("\n", ""))


def get_ob_list(container_id):
    """
    :param container_id: container identifier
    :type container_id: str
    :rtype: List[str]
    """
    container = utils.get_by_id(container_id, 'containerCollect')
    container_obj = is_associated(container)

    if not container:
        return []

    ob_list = container_obj.observation_blocks

    return clean_ob_list(ob_list)


def clean_deleted_ob(container_obj, container_id=None):
    ob_list = container_obj.observation_blocks
    ob_list = clean_ob_list(ob_list)
    container_obj.observation_blocks = ob_list

    container = container2dict(container_obj)

    # update the container document removing deleted OBs
    if container_id:
        new_vals = {"observation_blocks": ob_list}
        query = utils.query_by_id(container_id, add_delete=False)

        utils.update_doc(query, new_vals, 'containerCollect')
        container['_id'] = container_id

    return container


def clean_ob_list(ob_list):
    fields = {'status': 1, '_id': 0}

    clean_list = []
    for ob_id in ob_list:

        # includes check for deleted status
        query = utils.query_by_id(ob_id)

        # get status
        status = utils.get_fields_by_query(query, fields, 'obCollect')

        if status:
            clean_list.append(ob_id)

    return clean_list


def is_associated(container):
    """
    Determine if user (keck_id) is associated with sem_id in container

    It will abort with 401 if not associated.
    """
    container_obj = Container.from_dict(container)
    auth_utils.check_sem_id_associated(container_obj.sem_id)

    return container_obj

