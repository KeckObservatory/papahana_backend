import connexion
import six

from papahana.models.instrument_enum import InstrumentEnum  
from papahana.models.ra_schema import RASchema  
from papahana.models.dec_schema import DecSchema  
from papahana.models.sem_id_schema import SemIdSchema  
from papahana import util
from papahana.controllers import controller_helper as utils

COMPLETED = 3


def search_ob(**kwargs):
    """search_ob

    Retrieves all the OBs associated with the search parameters. 

    :param tag_name: a tag to search on
    :type tag_name: str
    :param sem_id: program id including semester
    :type sem_id: dict | bytes
    :param min_ra: the minimum right ascension
    :type min_ra: dict | bytes
    :param max_ra: the maximum right ascension
    :param min_dec: the minimum declination
    :type min_dec: dict | bytes
    :param max_dec: the maximum declination
    :type max_dec: dict | bytes
    :type max_dec: dict | bytes
    :param instrument: restrict results to a specific Instrument
    :type instrument: dict | bytes
    :param ob_priority: return results with a given priority.
    :type ob_priority: int
    :param min_priority: only return results with priority greater than or
                         equal to minimum.
    :type min_priority: int
    :param max_priority: only return results with priority less than to max.
    :type max_priority: int
    :param min_duration: only return results that have a duration greater than
                         or equal to the min_duration. The duration unit is minutes.
    :type min_duration: float
    :param max_duration: only return results that have a duration less than
                         or equal to the max_duration.  The duration unit is minutes.
    :type max_duration: float
    :param state: return OBs of a certain state,  the possible states are
                defined in ‘Defined Types’.
    :type state: str
    :param observable: only return results that are observable for current
                       UT to sunrise.  The duration is not taken into consideration.
                       Default is false (0),  use observable&#x3D;1 for only OBs that are observable.
    :type observable: bool
    :param completed: return results that are completed.  The default is false (0),
                      use completedfor only OBs that are observable.
    :type completed: bool
    :param container_id: ObjectId of the container identifier.
    :type container_id: str

    :rtype: json
    """
    kwargs = base_kwargs(kwargs)

    coll, pipeline = base_search_pipeline(kwargs)

    result = list(coll.aggregate(pipeline))

    return utils.list_with_objectid(result)


def search_ob_component(**kwargs):
    """

    Retrieves all the OBs associated with the search parameters. 

    :param ob_component_name: a tag to search on
    :type ob_component_name: str
    :param tag_name: a tag to search on
    :type tag_name: str
    :param sem_id: program id including semester
    :type sem_id: dict | bytes
    :param min_ra: the minimum right ascension
    :type min_ra: dict | bytes
    :param max_ra: the maximum right ascension
    :param min_dec: the minimum declination
    :type min_dec: dict | bytes
    :param max_dec: the maximum declination
    :type max_dec: dict | bytes
    :type max_dec: dict | bytes
    :param instrument: restrict results to a specific Instrument
    :type instrument: dict | bytes
    :param ob_priority: return results with a given priority.
    :type ob_priority: int
    :param min_priority: only return results with priority greater than or
                         equal to minimum.
    :type min_priority: int
    :param max_priority: only return results with priority less than to max.
    :type max_priority: int
    :param min_duration: only return results that have a duration greater than
                         or equal to the min_duration. The duration unit is minutes.
    :type min_duration: float
    :param max_duration: only return results that have a duration less than
                         or equal to the max_duration.  The duration unit is minutes.
    :type max_duration: float
    :param state: return OBs of a certain state,  the possible states are
                defined in ‘Defined Types’.
    :type state: str
    :param observable: only return results that are observable for current
                       UT to sunrise.  The duration is not taken into consideration.
                       Default is false (0),  use observable&#x3D;1 for only OBs that are observable.
    :type observable: bool
    :param completed: return results that are completed.  The default is false (0),
                      use completedfor only OBs that are observable.
    :type completed: bool
    :param container_id: ObjectId of the container identifier.
    :type container_id: str
    :param return_id: return a string of the Object ID if False (0),  default is True (1)
    :type return_id: bool

    :rtype: json
    """
    kwargs = base_kwargs(kwargs)

    coll, pipeline = base_search_pipeline(kwargs)

    if 'return_id' in kwargs and kwargs['return_id']:
        send_id = 0
    else:
        send_id = 1

    pipeline += [{'$project': {kwargs['ob_component_name']: 1, '_id': send_id}}]
    # pipeline += [{'$project': {kwargs['ob_component_name']: 1, '_id': 1}}]

    result = list(coll.aggregate(pipeline))

    return utils.list_with_objectid(result)


def search_ob_tableview(**kwargs):
    """

    Retrieves all the OBs associated with the search parameters.

    :param ob_component_name: a tag to search on
    :type ob_component_name: str
    :param tag_name: a tag to search on
    :type tag_name: str
    :param sem_id: program id including semester
    :type sem_id: dict | bytes
    :param min_ra: the minimum right ascension
    :type min_ra: dict | bytes
    :param max_ra: the maximum right ascension
    :param min_dec: the minimum declination
    :type min_dec: dict | bytes
    :param max_dec: the maximum declination
    :type max_dec: dict | bytes
    :type max_dec: dict | bytes
    :param instrument: restrict results to a specific Instrument
    :type instrument: dict | bytes
    :param ob_priority: return results with a given priority.
    :type ob_priority: int
    :param min_priority: only return results with priority greater than or
                         equal to minimum.
    :type min_priority: int
    :param max_priority: only return results with priority less than to max.
    :type max_priority: int
    :param min_duration: only return results that have a duration greater than
                         or equal to the min_duration. The duration unit is minutes.
    :type min_duration: float
    :param max_duration: only return results that have a duration less than
                         or equal to the max_duration.  The duration unit is minutes.
    :type max_duration: float
    :param state: return OBs of a certain state,  the possible states are
                defined in ‘Defined Types’.
    :type state: str
    :param observable: only return results that are observable for current
                       UT to sunrise.  The duration is not taken into consideration.
                       Default is false (0),  use observable&#x3D;1 for only OBs that are observable.
    :type observable: bool
    :param completed: return results that are completed.  The default is false (0),
                      use completedfor only OBs that are observable.
    :type completed: bool
    :param container_id: ObjectId of the container identifier.
    :type container_id: str

    :rtype: json
    """
    kwargs = base_kwargs(kwargs)

    coll, pipeline = base_search_pipeline(kwargs)

    pipeline += [{
        '$project': {
            '_id': '$_id', 'ob_name': '$metadata.name', 'sem_id': '$metadata.sem_id',
            'instrument': '$metadata.instrument', 'ob_type': '$metadata.ob_type',
            'acquisition': '$acquisition.metadata.name',
            'common_parameters': '$common_parameters.metadata.name',
            'tags': '$metadata.tags', 'target_name': '$target.metadata.name',
            'number_sequences': {'$cond': {'if': {
                '$ne':  [{'$type': '$observations'}, 'missing']},
                'then': {'$size': '$observations'}, 'else': '0'}
            }
        }
    }]

    result = list(coll.aggregate(pipeline))

    return utils.list_with_objectid(result)


def base_kwargs(kwargs):
    if not connexion.request.is_json:
        return kwargs

    kwargs['sem_id'] = SemIdSchema.from_dict(connexion.request.get_json())
    kwargs['min_ra'] = RASchema.from_dict(connexion.request.get_json())
    kwargs['max_ra'] = RASchema.from_dict(connexion.request.get_json())
    kwargs['min_dec'] = DecSchema.from_dict(connexion.request.get_json())
    kwargs['max_dec'] = DecSchema.from_dict(connexion.request.get_json())
    kwargs['instrument'] = InstrumentEnum.from_dict(connexion.request.get_json())
    # kwargs['duration'] = duration.from_dict(connexion.request.get_json())

    return kwargs


def base_search_pipeline(arg_dict):
    """
    Create the Mongo pipeline for the base search parameters.

    @param arg_dict: <dict> the keyword arguments.

    @return: Mongo collection,  <list, dict> Mongo pipeline
    """

    coll = None
    pipe_out = 'output'

    # [0 = partial, 1 = ready, 2 = ongoing, 3 = complete, 4 = aborted]
    if arg_dict.get('completed'):
        arg_dict['completed'] = COMPLETED

    # Documents = tags, containers,  observation_blocks
    queries = {}

    # tags
    if arg_dict.get('tag_name'):
        coll = util.config_collection('tagsCollect')
        queries['tag'] = filter_by_tag(arg_dict['tag_name'], pipe_out)

    # containers
    prefix = get_prefix(queries, pipe_out)

    # containers
    if arg_dict.get('container_id'):
        if not coll:
            coll = util.config_collection('containerCollect')

        obj_id = utils.get_object_id(arg_dict['container_id'])

        queries['container'] = [
            {"$match": {"$expr": {"$eq": [f"{prefix}_id", obj_id]}}}
        ]

    # Observation Blocks
    prefix = get_prefix(queries, pipe_out)

    # compose the OB parameter query
    queries['ob'] = [{"$match": {"$expr": {
        "$eq": [False, f"{prefix}status.deleted"]}
    }}]

    ob_id = arg_dict.get('ob_id')
    if ob_id:
        obj_id = utils.get_object_id(ob_id)
        queries['ob'].append({'$match': {'$expr': {'$eq': ['$_id', obj_id]}}})

    # lt = {"$match": {"$expr": {"$lte": [field_name, max_val]}}}
    # pipeline.append(lt)

    min_priority = make_int(arg_dict, 'min_priority')
    max_priority = make_int(arg_dict, 'max_priority')

    queries['ob'] = add_min_max(queries['ob'], f'{prefix}metadata.priority',
                                min_priority, max_priority)

    queries['ob'] = add_min_max(queries['ob'], f'{prefix}target.parameters.target_coord_ra',
                                arg_dict.get('min_ra'), arg_dict.get('max_ra'))

    queries['ob'] = add_min_max(queries['ob'], f'{prefix}target.parameters.target_coord_dec',
                                arg_dict.get('min_dec'), arg_dict.get('max_dec'))

    # duration
    if arg_dict.get('min_duration'):
        queries['ob'] += filter_by_duration(arg_dict.get('min_duration'),
                                            pipe_out, less_than=False)
    if arg_dict.get('max_duration'):
        queries['ob'] += filter_by_duration(arg_dict.get('max_duration'),
                                            pipe_out)

    # observable,  RA range
    ob_params = {
        'ob_priority': 'metadata.priority',
        'sem_id': 'metadata.sem_id', 'instrument': 'metadata.instrument',
        'state': 'status.state', 'completed': 'status.state'
    }

    for arg_name, arg_value in arg_dict.items():
        if arg_name not in ob_params.keys() or not arg_value:
            continue

        queries['ob'].append(
            {"$match": {"$expr": {
                "$eq": [f"{prefix}{ob_params[arg_name]}", arg_value]
            }}}
        )

    pipeline = []
    for pipe_key in queries:
        pipeline += queries[pipe_key]

    # change the tag list object ids to names
    pipeline = utils.convert_tag2name(pipeline, prefix)

    # only get ob (output) from pipeline if it is nested
    if pipe_out in prefix:
        pipeline += [
            {'$project': {prefix.strip('$').strip('.'): 1, '_id': 0}},
            {'$replaceRoot': {'newRoot': '$output'}}
        ]
    else:
        # remove extra fields if wasn't filtered through 'output'
        pipeline = utils.unset_tag2name_fields(pipeline)

    if not coll:
        coll = util.config_collection('obCollect')

    return coll, pipeline


def filter_by_tag(tag_name, pipe_out):
    """
    Filter the results by tag.

    @param tag_name: <str> the name of the tag to filter results by.
    @param pipe_out: <str>  the name of the output results in the pipeline.

    @return: <list, dict> the Mongo pipeline as a list of dictionaries.
    """
    pipe = [
        {"$match": {'tag_str': tag_name}},
        {"$addFields": {"tag_id": {"$toString": "$_id"}}},
        {"$lookup": {
            "from": "observation_blocks",
            "localField": "tag_id",
            "foreignField": "metadata.tags",
            "as": pipe_out}
        },
        {"$unwind": f"${pipe_out}"}]

    return pipe


def filter_by_duration(duration, pipe_out, less_than=True):
    """
    Restrict the results by min and/or max duration

    For Completed and Aborted OBs the total duration == 0

    """
    if less_than:
        cond = "$lte"
    else:
        cond = "$gte"

    pipe = [
        {"$unwind": "$observations"},
        {"$group": {
            "_id": "$_id",
            pipe_out: {"$first": "$$ROOT"},
            "total": {
                "$sum": {
                    "$cond": [
                        {"$lte":
                             ["$status.state", 2]
                         },
                        {"$cond": [
                            {"$gte": [
                                "$observations.metadata.sequence_number",
                                "$status.current_seq"]},
                            {"$multiply": [
                                "$observations.parameters.det1_exp_time",
                                "$observations.parameters.det1_exp_number"]}, 0]
                        }, 0]
                }
            }
        }},
        {"$match": {"total": {cond: duration}}},
    ]

    return pipe


def get_prefix(queries, pipe_out):
    """
    Determine if the pipeline output is coming through a pipe,  or the start.

    @param queries: <dict> the dictionary containing the pipeline results.
    @param pipe_out: <str> the name of the end (output) of the pipeline.

    @return:
    """
    if len(queries) == 0:
        return '$'
    else:
        return f"${pipe_out}."


def add_min_max(pipeline, field_name, min_val, max_val):
    """
    Add min/max/range filter to the pipeline.

    @param pipeline: <list, dict> the Mongo pipeline as a list of dictionaries.
    @param field_name: <str> the field name within the json,  ie metadata.priority
    @param min_val: <any> the value to
    @param max_val:
    @return:
    """
    if max_val:
        lt = {"$match": {"$expr": {"$lte": [field_name, max_val]}}}
        pipeline.append(lt)
    if min_val:
        gt = {"$match": {"$expr": {"$gte": [field_name, min_val]}}}
        pipeline.append(gt)

    return pipeline


def make_int(arg_dict, arg_key):
    arg_value = arg_dict.get(arg_key)
    if arg_value:
        try:
            return int(arg_value)
        except (ValueError, TypeError):
            return None

    return None
