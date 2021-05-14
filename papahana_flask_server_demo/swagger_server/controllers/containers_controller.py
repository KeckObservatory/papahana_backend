import connexion
import six
import pymongo

from swagger_server.models.container import Container  # noqa: E501
from swagger_server.models.container_summary import ContainerSummary  # noqa: E501
from swagger_server.models.observation_block import ObservationBlock  # noqa: E501
from swagger_server.controllers import observation_block_controller as ob_control
from swagger_server.controllers import controller_helper as utils

# from swagger_server import util
from config import config_collection
from bson.objectid import ObjectId


def containers_get(container_id):  # noqa: E501
    """
    Retrieves a specific container's information # noqa: E501

    error:
    http://vm-webtools.keck.hawaii.edu:50000/v0/containers?container_id=09ad6fc4062bf346f1b0437
    result:
    http://vm-webtools.keck.hawaii.edu:50000/v0/containers?container_id=609ad6fc4062bf346f1b0437

    :param container_id: container identifier
    :type container_id: str

    :rtype: Container
    """
    result = utils.get_by_id(container_id, 'containerCollect')

    if result:
        result = str(result[0])
    else:
        result = ""

    return result


def containers_post(body):  # noqa: E501
    """
    Creates a container # noqa: E501

    test:
    curl -v -H "Content-Type: application/json" -X POST -d '{"semester":"2030A"}' http://vm-webtools.keck:50000/v0/containers
        db.containers.find({"semester": "2030A"})

    :param body:
    :type body: dict | bytes

    :rtype: str: the ObjectID of the inserted document
    """
    if connexion.request.is_json:
        body = Container.from_dict(connexion.request.get_json())  # noqa: E501

    new_doc = {"name": body.name, "semester": body.semester,
               "ob_blocks": body.observation_blocks, "comment": body.comment}

    result = utils.insert_into_collection(new_doc, 'containerCollect')

    return str(result.inserted_id)


def containers_put(body, container_id):  # noqa: E501
    """containers_put

    test :
    curl -v -H "Content-Type: application/json" -X PUT -d '{"semester":"2024A","observation_blocks":["2","3"]}' 'http://vm-webtools.keck:50000/v0/containers?container_id=609ad6fc4062bf346f1b0437'

    Overwrites a container # noqa: E501

    :param body:
    :type body: dict | bytes
    :param container_id: container identifier
    :type container_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Container.from_dict(connexion.request.get_json())  # noqa: E501

    container_dict = body.to_dict()

    new_vals = {}
    for key, val in container_dict.items():
        if val and key != 'container_id':
            new_vals[key] = val

    query = utils.query_by_id(container_id)
    utils.update_doc(query, new_vals, 'containerCollect')


def containers_delete(container_id):  # noqa: E501
    """containers_delete

    Delete container by id # noqa: E501

    :param container_id: container identifier
    :type container_id: str

    :rtype: None
    """
    query = utils.query_by_id(container_id)
    utils.delete_from_collection(query, 'containerCollect')


def containers_append_put(body, container_id):  # noqa: E501
    """containers_append_put

    Appends a list of observation blocks to a container by id.

    test (appends ob_id=9 to container_id=609306745ec7a7825e28af85):
    curl -v -H "Content-Type: application/json" -X PUT -d '["9"]' 'http://vm-webtools.keck:50000/v0/containers/append?container_id=609306745ec7a7825e28af85'

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
    utils.update_doc(utils.query_by_id(container_id), new_vals, 'containerCollect')


def containers_execution_times_get(container_id):  # noqa: E501
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
        total_time += ob_control.ob_execution_time(str(ob))

    return total_time


def containers_export_get(container_id):  # noqa: E501
    """
    Retrieves a specific container information in a file format (default .json)

    :param container_id: container identifier
    :type container_id: str

    :rtype: Container
    """
    query = utils.query_by_id(container_id)

    return 'do some magic!'


def containers_items_get(container_id):  # noqa: E501
    """containers_items_get

    Retrieves the ordered list of observing blocks in a container.

    :param container_id: container identifier
    :type container_id: str

    :rtype: List[Container]
    """
    ob_list = utils.get_ob_list(container_id)
    ob_list.sort()

    return str(ob_list)


# TODO this seems like it is the same as /containers_get
def containers_items_summary_get(container_id):  # noqa: E501
    """
    Retrieves a summary of container information # noqa: E501

    :param container_id: container identifier
    :type container_id: str

    :rtype: ContainerSummary
    """

    return 'do some magic!'


def containers_schedule_too_post(body):  # noqa: E501
    """
    Submits a container for Target of Opportunity (ToO) (all the elements)

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Container.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def containers_verify_get(container_id):  # noqa: E501
    """
    Request verification of the elements of a container. Sends container summary
    as a successful response

    :param container_id: container identifier
    :type container_id: str

    :rtype: ContainerSummary
    """
    #TODO get summary from the ob_block

    return 'do some magic!'


def sem_id_containers_get(sem_id):  # noqa: E501
    """sem_id_containers_get
    /semesters/containers

    Retrieves all containers associated with a program.

    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Container]
    """
    #TODO get sem_id from the ob_block
    return 'do some magic!'

