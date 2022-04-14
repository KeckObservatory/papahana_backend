from flask import abort

from papahana.controllers import observers_utils as obs_utils
from papahana.controllers import controller_helper as utils
from papahana.controllers import containers_controller

def odt_ob_query(query, fields, instrument, min_ra, max_ra, ob_priority,
                 min_priority, max_priority, min_duration,  max_duration,
                 state, observable, completed, container_id):
    """
    :param query: The initial query to add the params to.
    :type query: dict | bytes
    :param fields: The result fields to return,  an empty {} returns all.
    :type fields: dict | bytes
    :param instrument: instrument used to make observation
    :type instrument: dict | bytes
    :param min_ra: the minimum right ascension
    :type min_ra: dict | bytes
    :param max_ra: the maximum right ascension
    :type max_ra: dict | bytes
    :param ob_priority: return results with a given priority.
    :type ob_priority: int
    :param min_priority: only return results with priority greater than or
                         equal to minimum.
    :type min_priority: int
    :param max_priority: only return results with priority less than to max.
    :type max_priority: int
    :param min_duration: only return results that have a duration greater than
                         or equal to the min_duration.  The duration unit is
                         minutes.
    :type min_duration: float
    :param max_duration: only return results that have a duration less than
                        or equal to the max_duration.  The duration unit is
                        minutes.
    :type max_duration: float
    :param state: return OBs of a certain state,  the possible states are
                  defined in ‘Defined Types’.
    :type state: str
    :param observable: only return results that are observable for current UT
                       to sunrise.  The duration is not taken into consideration.
                       Default is false (0),  use observable for only OBs that
                       are observable.
    :type observable: bool
    :param completed: return results that are completed.  The default is false,
                      use completed for only OBs that are observable.
    :type completed: bool
    :param container_id: ObjectId of the container identifier.
    :type container_id: str

    :rtype: List
    """

    if instrument:
        query['metadata.instrument'] = instrument
    if ob_priority:
        query['metadata.priority'] = int(ob_priority)

    # [0 = partial, 1 = ready, 2 = ongoing, 3 = complete, 4 = aborted]
    if completed:
        query['status.state'] = 3
    elif state:
        query['status.state'] = int(state)

    else:
        if min_priority and max_priority:
            query["status.priority"] = {"$gt": int(min_priority), "$lt": int(max_priority)}
        elif min_priority:
            query["status.priority"] = {"$gt": int(min_priority)}
        elif max_priority:
            query["status.priority"] = {"$lt": int(max_priority)}

    # TODO need dcs keyword access
    # if observable:
    #     min_ra, max_ra = restrict2observable(min_ra, max_ra)

    if min_ra and max_ra:
        query["target.target_coord_ra"] = {"$gt": min_ra, "$lt": max_ra}
    elif min_ra:
        query["target.target_coord_ra"] = {"$gt": min_ra}
    elif max_ra:
        query["target.target_coord_ra"] = {"$lt": max_ra}

    matching_ob = utils.parse_duration(utils.get_fields_by_query(query, fields,
                                                                 'obCollect'),
                                       min_duration, max_duration)

    matching_ob = restrict_by_container(container_id,
                                        utils.list_with_objectid(matching_ob))

    return matching_ob


def restrict_by_container(container_id, ob_list):
    if not container_id:
        return ob_list

    container = containers_controller.containers_get(container_id)
    if not container:
        return []

    try:
        container_ob_list = container["observation_blocks"]
    except KeyError:
        return []

    matched_ob_list = []
    for ob in ob_list:
        try:
            if ob['_id'] in container_ob_list:
                matched_ob_list.append(ob)
        except:
            continue

    return matched_ob_list





