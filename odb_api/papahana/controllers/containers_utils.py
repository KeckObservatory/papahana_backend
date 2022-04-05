
from papahana.controllers import controller_helper as utils
from papahana.controllers import authorization_utils as auth_utils

from papahana.models.container import Container


def get_ob_list(container_id):
    """
    :param container_id: container identifier
    :type container_id: str
    :rtype: List[str]
    """
    container = utils.get_by_id(container_id, 'containerCollect')
    container_obj = is_associated(container)

    if container:
        ob_list = container_obj.observation_blocks
    else:
        ob_list = []

    return ob_list


def is_associated(container):
    """
    Determine if user (keck_id) is associated with sem_id in container

    It will abort with 401 if not associated.
    """
    container_obj = Container.from_dict(container)
    auth_utils.check_sem_id_associated(container_obj.sem_id)

    return container_obj

