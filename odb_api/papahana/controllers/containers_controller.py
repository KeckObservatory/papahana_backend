import connexion
from flask import abort

from papahana.controllers import controller_helper as utils
from papahana.controllers import containers_utils as contain_utils
from papahana.controllers import observation_block_controller


def containers_get(container_id):
    """
    Retrieves a specific container.
        /containers

    :param container_id: container identifier
    :type container_id: str

    :rtype: dict (Container)
    """
    container = utils.get_by_id(container_id, 'containerCollect')
    container_obj = contain_utils.is_associated(container)

    container = contain_utils.clean_deleted_ob(container_obj, container_id)

    return container


def containers_post(body):
    """
    Creates a container 
        /containers

    :param body:
    :type body: dict | bytes

    :rtype: str: the ObjectID of the inserted document
    """
    if connexion.request.is_json:
        container_obj = contain_utils.is_associated(body)
    else:
        abort(422, 'Request must be JSON formatted.')

    container = contain_utils.clean_deleted_ob(container_obj)

    result = utils.insert_into_collection(container, 'containerCollect')

    return str(result)


def containers_put(body, container_id):  
    """
    Overwrites a container
        /containers

    :param body:
    :type body: dict | bytes
    :param container_id: container identifier
    :type container_id: str

    :rtype: None
    """
    # check the sem_id in body is associated
    if connexion.request.is_json:
        container_obj = contain_utils.is_associated(body)
    else:
        abort(422, 'Request must be JSON formatted.')

    # get current container and confirm container is associated
    _ = containers_get(container_id)

    # check for deleted OBs
    container = contain_utils.clean_deleted_ob(container_obj)

    new_vals = {}
    for key, val in container.items():
        if val and key != 'container_id':
            new_vals[key] = val

    query = utils.query_by_id(container_id, add_delete=False)
    utils.update_doc(query, new_vals, 'containerCollect')


def containers_delete(container_id):
    """
    Delete container by id
        /containers

    :param container_id: container identifier
    :type container_id: str

    :rtype: None
    """
    # get container and confirm container is associated
    _ = containers_get(container_id)

    query = utils.query_by_id(container_id, add_delete=False)
    utils.delete_from_collection(query, 'containerCollect')


def containers_append_put(body, container_id):
    """
    Appends a list of observation blocks to a container by id.
        /containers/append

    :param body:
    :type body: list | bytes
    :param container_id: container identifier
    :type container_id: str

    :rtype: None
    """
    # get observation list and confirm container is associated
    ob_list = contain_utils.get_ob_list(container_id)

    # update the container collection with new values
    unique_obs = list(set(ob_list + body))
    if not unique_obs:
        return

    new_vals = {"observation_blocks": unique_obs}
    utils.update_doc(utils.query_by_id(container_id, add_delete=False),
                     new_vals, 'containerCollect')


def containers_execution_times_get(container_id):  
    """
    Calculate the total execution time of a container
        /containers/executionTimes

    :param container_id: container identifier
    :type container_id: str

    :rtype: float
    """
    # get observation list and confirm container is associated
    ob_list = contain_utils.get_ob_list(container_id)

    total_time = 0
    for ob in ob_list:
        total_time += observation_block_controller.ob_execution_time(str(ob))

    return total_time


def containers_items_get(container_id):
    """
    Retrieves the ordered list of observing blocks in a container.
        /containers/items

    :param container_id: container identifier
    :type container_id: str

    :rtype: List[ObservationBlock]
    """
    ob_list = contain_utils.get_ob_list(container_id)
    ob_list.sort()

    ob_block_list = []
    for ob_id in ob_list:
        ob_block_list.append(observation_block_controller.ob_get(ob_id))

    return utils.list_with_objectid(ob_block_list)


# TODO this seems like it is the same as /containers_get
def containers_items_summary_get(container_id):  
    """
    Retrieves a summary of container information 

    :param container_id: container identifier
    :type container_id: str

    :rtype: ContainerSummary
    """
    try:
        return utils.get_by_id(container_id, 'containerCollect')
    except ValueError as err:
        return err


def containers_verify_get(container_id):  
    """
    Request verification of the elements of a container. Sends container summary
    as a successful response

    :param container_id: container identifier
    :type container_id: str

    :rtype: ContainerSummary
    """
    #TODO get summary from the ob_block

    return 'do some magic!'


