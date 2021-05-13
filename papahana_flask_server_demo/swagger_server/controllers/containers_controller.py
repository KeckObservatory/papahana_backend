import connexion
import six

from swagger_server.models.container import Container 
from swagger_server.models.container_summary import ContainerSummary 
from swagger_server.models.observation_block import ObservationBlock 
from swagger_server import util
from .controller_helper import create_signature_match
from config import coll


def containers_append_put(body, container_id): 
    """containers_append_put

    Appends an observation block to a container by id

    :param body: The ob_id list
    :type body: list
    :param container_id: container identifier
    :type container_id: str

    :rtype: None
    """
    # if connexion.request.is_json:
    #     body = [ObservationBlock.from_dict(d)
    #             for d in connexion.request.get_json()]


    return 'do some magic!'


def containers_delete(container_id): 
    """containers_delete

    Delete container by id

    :param container_id: container identifier
    :type container_id: str

    :rtype: None
    """
    try:
        coll.delete_one({'container_id': container_id})
    except Exception as err:
        print(err)

    return


def containers_execution_times_get(container_id): 
    """containers_execution_times_get

    Calculate the total execution time of a container

    :param container_id: container identifier
    :type container_id: str

    :rtype: float
    """
    # db.orders.explain().aggregate([
    #     {$match: {status: "A"}},
    #     { $group: {_id: "$cust_id",
    #                total: { $sum: "$amount"}}},
    #     { $sort: {total: -1}}])

    return 'do some magic!'


def containers_export_get(container_id): 
    """containers_export_get

    Retrieves a specific container information in a file format (default .json)

    :param container_id: container identifier
    :type container_id: str

    :rtype: Container
    """

    # list of OB IDs.
    # container = coll.find("container_id": container_id)
    # json_data = container.tojson

    # return json_data

    return

def containers_get(container_id):  # noqa: E501
    """containers_get

    Retrieves a specific container's information # noqa: E501

    :param container_id: container identifier
    :type container_id: str

    :rtype: Container
    """
    # db.containers.findOne({"container_id": container_id})
    return 'made it!'


def containers_items_get(container_id): 
    """containers_items_get

    Retrieves the ordered list of observing blocks in a container

    :param container_id: container identifier
    :type container_id: str

    :rtype: List[Container]
    """

    #ob_blocks = db.containers.findOne({"container_id": container_id}).ob_blocks
    # return ob_blocks
    return 'do some magic!'


def containers_items_put(body, container_id): 
    """containers_items_put

    Puts a a list of Observation Blocks into a container

    :param body: 
    :type body: list | bytes
    :param container_id: container identifier
    :type container_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = [ObservationBlock.from_dict(d)
                for d in connexion.request.get_json()]
    # for val in ob_list
    # db.containers.update({"container_id": "0"}, {$addToSet: {ob_blocks: "4"}} )

    return 'do some magic!'


def containers_items_summary_get(container_id): 
    """containers_items_summary_get

    Retrieves a summary of container information

    :param container_id: container identifier
    :type container_id: str

    :rtype: ContainerSummary
    """
    return 'do some magic!'


def containers_post(body):
    """containers_post

    Creates a container # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        body = Container.from_dict(connexion.request.get_json())

    # get value
    # db.sequences.findOne({"_id": "containers"}).value
    # increment by one
    # db.sequences.update({"_id": "containers"}, {"$inc": {"value": 1}})

    # > db.containers.insert(
    #     {"container_id": "3",
    #     ob_blocks: ["33", "88", "99"],
    #     semester: "2021A"})

    return


def containers_put(body, container_id): 
    """containers_put

    Overwrites a container

    :param body: 
    :type body: dict | bytes
    :param container_id: container identifier
    :type container_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Container.from_dict(connexion.request.get_json()) 
    return 'do some magic!'


def containers_schedule_too_post(body):  # noqa: E501
    """containers_schedule_too_post

    Submits a container for Target of Opportunity (ToO) (all the elements) # noqa: E501

    :param body:
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Container.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def containers_verify_get(container_id): 
    """containers_verify_get

    Request verification of the elements of a container. Sends container
    summary as a successful response

    :param container_id: container identifier
    :type container_id: str

    :rtype: ContainerSummary
    """
    return 'do some magic!'


def sem_id_containers_get(sem_id, prog_id):  # noqa: E501
    """sem_id_containers_get

    Retrieves all containers associated with a program # noqa: E501

    :param sem_id: semester id
    :type sem_id: str
    :param prog_id: program id
    :type prog_id: str

    :rtype: List[Container]
    """
    return 'do some magic!'
