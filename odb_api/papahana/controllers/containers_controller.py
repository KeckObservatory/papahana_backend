import connexion

from papahana.controllers import controller_helper as utils
from papahana.controllers import observation_block_controller

from papahana.models.container import Container  
from papahana.models.observation_block import ObservationBlock



def containers_get(container_id):  
    """
    Retrieves a specific container's information

    error:
    http://vm-webtools.keck.hawaii.edu:50000/v0/containers?container_id=09ad6fc4062bf346f1b0437
    result:
    http://vm-webtools.keck.hawaii.edu:50000/v0/containers?container_id=60a6b4057c25cc6791b5fb02

    :param container_id: container identifier
    :type container_id: str

    :rtype: Container
    """
    try:
        return utils.get_by_id(container_id, 'containerCollect')
    except ValueError as err:
        return err


def containers_post(body):
    """
    Creates a container 

    test:
    curl -v -H "Content-Type: application/json" -X POST -d '{"semester":"2030A"}' http://vm-webtools.keck:50000/v0/containers
        db.containers.find({"semester": "2030A"})

    :param body:
    :type body: dict | bytes

    :rtype: str: the ObjectID of the inserted document
    """
    result = utils.insert_into_collection(body, 'containerCollect')

    return str(result)


def containers_put(body, container_id):  
    """containers_put

    test :
    curl -v -H "Content-Type: application/json" -X PUT -d '{"semester":"2024A","observation_blocks":["2","3"]}' 'http://vm-webtools.keck:50000/v0/containers?container_id=609ad6fc4062bf346f1b0437'

    Overwrites a container

    :param body:
    :type body: dict | bytes
    :param container_id: container identifier
    :type container_id: str

    :rtype: None
    """
    if type(body) is not dict:
        container_dict = body.to_dict()
    else:
        container_dict = body

    new_vals = {}
    for key, val in container_dict.items():
        if val and key != 'container_id':
            new_vals[key] = val

    query = utils.query_by_id(container_id, add_delete=False)
    utils.update_doc(query, new_vals, 'containerCollect')


def containers_delete(container_id):
    """containers_delete

    Delete container by id

    :param container_id: container identifier
    :type container_id: str

    :rtype: None
    """
    query = utils.query_by_id(container_id, add_delete=False)
    utils.delete_from_collection(query, 'containerCollect')


def containers_append_put(body, container_id):
    """containers_append_put

    Appends a list of observation blocks to a container by id.

    :param body:
    :type body: list | bytes
    :param container_id: container identifier
    :type container_id: str

    :rtype: None
    """
    ob_list = utils.get_ob_list(container_id)

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

    http://vm-webtools.keck.hawaii.edu:50000/v0/containers/executionTimes?container_id=609306745ec7a7825e28af85

    :param container_id: container identifier
    :type container_id: str

    :rtype: float
    """
    ob_list = utils.get_ob_list(container_id)
    total_time = 0
    for ob in ob_list:
        total_time += observation_block_controller.ob_execution_time(str(ob))

    return total_time


def containers_export_get(container_id):  
    """
    Retrieves a specific container information in a file format (default .json)

    :param container_id: container identifier
    :type container_id: str

    :rtype: Container
    """
    query = utils.query_by_id(container_id, add_delete=False)

    return 'do some magic!'


def containers_items_get(container_id):  
    """containers_items_get

    Retrieves the ordered list of observing blocks in a container.

    :param container_id: container identifier
    :type container_id: str

    :rtype: List[ObservationBlock]
    """
    ob_list = utils.get_ob_list(container_id)
    ob_list.sort()

    ob_block_list = []
    for ob in ob_list:
        ob_block_list.append(observation_block_controller.ob_get(ob))

    return ob_block_list


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

def containers_schedule_too_post(body):  
    """
    Submits a container for Target of Opportunity (ToO) (all the elements)

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Container.from_dict(d) for d in connexion.request.get_json()]

    return 'do some magic!'


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

