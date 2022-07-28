import connexion
import six

from papahana.models.instrument_enum import InstrumentEnum  
from papahana.models.ra_schema import RASchema  
from papahana.models.dec_schema import DecSchema  
from papahana.models.sem_id_schema import SemIdSchema  
from papahana import util
from papahana.controllers import controller_helper as utils


# def search_ob(tag_name=None, sem_id=None, min_ra=None, max_ra=None,
#               instrument=None, ob_priority=None, min_priority=None,
#               max_priority=None, min_duration=None, max_duration=None,
#               state=None, observable=None, completed=None, container_id=None):
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
    if connexion.request.is_json:
        kwargs['sem_id'] = SemIdSchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['min_ra'] = RASchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['max_ra'] = RASchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['min_dec'] = DecSchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['max_dec'] = DecSchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['instrument'] = InstrumentEnum.from_dict(connexion.request.get_json())

    coll, pipeline = base_search_pipeline(kwargs)

    result = list(coll.aggregate(pipeline))

    print(f'pipe {pipeline}')

    return utils.json_with_objectid(result)


# def search_ob_inst_config(tag_name=None, sem_id=None, min_ra=None, max_ra=None, instrument=None, ob_priority=None, min_priority=None, max_priority=None, min_duration=None, max_duration=None, state=None, observable=None, completed=None, container_id=None):
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

    :rtype: json
    """
    if connexion.request.is_json:
        kwargs['sem_id'] = SemIdSchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['min_ra'] = RASchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['max_ra'] = RASchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['min_dec'] = DecSchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['max_dec'] = DecSchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['instrument'] = InstrumentEnum.from_dict(connexion.request.get_json())

    coll, pipeline = base_search_pipeline(kwargs)

    # pipeline += [{'$replaceRoot': {'newRoot': '$common_parameters'}}]
    pipeline += [{'$project': {kwargs['ob_component_name']: 1, '_id': 0}}]

    result = list(coll.aggregate(pipeline))

    print(f'pipe {pipeline}')

    return utils.json_with_objectid(result)


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
    if connexion.request.is_json:
        kwargs['sem_id'] = SemIdSchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['min_ra'] = RASchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['max_ra'] = RASchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['min_dec'] = DecSchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['max_dec'] = DecSchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        kwargs['instrument'] = InstrumentEnum.from_dict(connexion.request.get_json())

    coll, pipeline = base_search_pipeline(kwargs)

    pipeline += [{
        '$project': {
            '_id': 0, 'ob_name': '$metadata.name', 'sem_id': '$metadata.sem_id',
            'instrument': '$metadata.instrument', 'ob_type': '$metadata.ob_type',
            'acquisition': '$acquisition.metadata.name',
            'common_parameters': '$common_parameters.metadata.name',
            'tags': '$metadata.tags',
            'number_sequences': {'$size': '$observations'}}
        }]

    result = list(coll.aggregate(pipeline))

    print(f'pipe {pipeline}')

    return utils.json_with_objectid(result)


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
        arg_dict['completed'] = 3

    # Documnets = tags, containers,  observation_blocks
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

    min_priority = make_int(arg_dict, 'min_priority')
    max_priority = make_int(arg_dict, 'max_priority')

    queries['ob'] = add_min_max(queries['ob'], f'{prefix}metadata.priority',
                                min_priority, max_priority)

    queries['ob'] = add_min_max(queries['ob'], f'{prefix}target.parameters.target_coord_ra',
                                arg_dict.get('min_ra'), arg_dict.get('max_ra'))

    queries['ob'] = add_min_max(queries['ob'], f'{prefix}target.parameters.target_coord_dec',
                                arg_dict.get('min_dec'), arg_dict.get('max_dec'))

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
    pipeline += [
        {'$addFields': {
            'tag_id': {
                '$map': {
                    'input': f"{prefix}metadata.tags",
                    'as': 'str_id',
                    'in': {'$toObjectId': '$$str_id'}
                }}}},
        {'$lookup': {
            'from': 'tag_info',
            'localField': 'tag_id',
            'foreignField': '_id',
            'as': 'tag_list'}},
        {'$addFields': {'tag_str_list': '$tag_list.tag_str'}},
        {'$set': {f"{prefix.strip('$')}metadata.tags": '$tag_str_list'}}
    ]

    # only get ob (output) from pipeline if it is nested
    if pipe_out in prefix:
        pipeline += [
            {'$project': {prefix.strip('$').strip('.'): 1, '_id': 0}},
            {'$replaceRoot': {'newRoot': '$output'}}
        ]
    else:
        # remove extra fields if wasn't filtered through 'output'
        pipeline += [{"$unset": ["tag_list", "tag_str_list", "tag_id"]}]

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
