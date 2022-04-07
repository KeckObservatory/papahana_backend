import connexion
import six

from flask import g, abort

from papahana.controllers import controller_helper as utils
from papahana.controllers import authorization_utils as auth_utils
from papahana.controllers import observers_controller as obs_cont
# from papahana.controllers import observation_block_controller


from papahana.models.container import Container  
from papahana.models.observation_block import ObservationBlock
from papahana.models.instrument_enum import InstrumentEnum
from papahana.models.ra_schema import RASchema
from papahana.models.sem_id_schema import SemIdSchema  
from papahana.models.target import Target  
from papahana import util


def sem_id_get():
    """
    Retrieves all the sem_ids associated with an observer
    /semesterIds/

    :rtype: List[str]
    """
    # check_obs_id
    obs_id = g.user
    # check the database first
    semester_list = obs_cont.observer_semid()

    semid_list = utils.get_proposal_ids(obs_id)
    if semid_list and type(semid_list) == 'list':
        semester_list['associations'] += semid_list

    return semester_list


@auth_utils.confirm_sem_id_associated
def sem_id_proposal_get(sem_id):
    """
    retrieves the proposal associated with the program.
    /semesterIds/{sem_id}/proposal

    :param sem_id: semester id
    :type sem_id: str

    :rtype: file
    """
    #TODO get the pdf from the proposals API.

    return 'do some magic! sem_id_proposal_get'


def sem_id_semester_get(semester):
    """
     retrieves all the sem_id associated with an observer for the semester.
     /semesterIds/{semester}/semester/

    :param semester: semester id
    :type semester: str

    :rtype: List[str]
    """
    obs_id = g.user

    # check the database first
    full_list = obs_cont.observer_semid()['associations']

    # check the proposals api
    sem_ids = utils.get_proposal_ids(obs_id)
    if sem_ids:
        full_list += sem_ids

    semester_list = []
    for sem_id in full_list:
        if semester in sem_id:
            semester_list.append(sem_id)

    # TODO check the schedule
    semester_list = set(semester_list)

    return {semester: list(semester_list)}


@auth_utils.confirm_sem_id_associated
def sem_id_ob_get(sem_id):
    """
    Retrieves the ob_blocks for a sem_id
        /semesterIds/{sem_id}/ob

    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[ObservationBlock]
    """
    query = {"metadata.sem_id": sem_id}
    ob_blocks = utils.get_by_query(query, 'obCollect')

    return utils.list_with_objectid(ob_blocks)


@auth_utils.confirm_sem_id_associated
def sem_id_containers_get(sem_id):
    """
    Retrieves all containers associated with a program.  The Semester Id
    is a required parameter.
        /semesterIds/{sem_id}/containers

    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Container]
    """
    query = {"sem_id": sem_id}
    containers = utils.get_by_query(query, 'containerCollect')

    return utils.list_with_objectid(containers)


@auth_utils.confirm_sem_id_associated
def sem_id_targets_get(sem_id):
    """
    Retrieves all the targets associated with a program.
        /semesterIds/{sem_id}/targets

    :param sem_id: semester id
    :type sem_id: str

    :rtype: List[Target]
    """

    ob_blocks = sem_id_ob_get(sem_id)

    all_targets = []
    for ob_block in ob_blocks:
        if 'target' in ob_block:
            all_targets.append(ob_block['target'])

    return all_targets


@auth_utils.confirm_sem_id_associated
def sem_id_submit_post(body, sem_id):
    """
    Submits OBs for a program.  Uses the obsid in the authentication
    header and provided semId to retrieve the proposal file
    associated with the program

    :param body:
    :type body: dict | bytes
    :param sem_id: semester id
    :type sem_id: str

    :rtype: None
    """
    return 'do some magic! sem_id_submit_post'


@auth_utils.confirm_sem_id_associated
def sem_id_submit_put(sem_id, body=None):
    """sem_id_submit_put

    updates a program (OBs)

    :param sem_id: semester id
    :type sem_id: str
    :param body:
    :type body: dict | bytes

    :rtype: None
    """
    return 'do some magic! sem_id_submit_put'


# ----- new controllers -----

# @auth_utils.confirm_sem_id_associated
# def sem_id_ob_metadata(sem_id):
#     """
#        /semesterIds/{sem_id}/ob/metadata
#
#     sem_id" : "2019B_U158",
#
#     Retrieves all the observation blocks in their entirety for a given program.
#     Excludes completed observation blocks.
#
#     :param sem_id: semester id
#     :type sem_id: dict | bytes
#
#     :rtype: List
#     """
#     if connexion.request.is_json:
#         sem_id = SemIdSchema.from_dict(connexion.request.get_json())
#
#     query = {"metadata.sem_id": sem_id}
#     containers = utils.get_by_query(query, 'obCollect')
#
#     return utils.list_with_objectid(containers)


@auth_utils.confirm_sem_id_associated
def sem_id_ob_cal(sem_id, instrument=None):
    """
        /semesterIds/{sem_id}/ob/calibration

    Retrieves all the calibration observation blocks in their entirety for a
    given program.  Excludes completed observation blocks.

    :param sem_id: semester id
    :type sem_id: dict | bytes
    :param instrument: instrument used to make observation
    :type instrument: dict | bytes

    :rtype: List
    """
    if connexion.request.is_json:
        sem_id = SemIdSchema.from_dict(connexion.request.get_json())  
    if connexion.request.is_json:
        instrument = InstrumentEnum.from_dict(connexion.request.get_json())

    query = {'metadata.sem_id': sem_id, 'metadata.ob_type': 'calibration'}
    matching_ob = utils.get_by_query(query, 'obCollect')

    return utils.list_with_objectid(matching_ob)


@auth_utils.confirm_sem_id_associated
def sem_id_ob_sci(sem_id, instrument=None, min_ra=None, max_ra=None,
                       ob_priority=None, min_priority=None, max_priority=None,
                       min_duration=None, max_duration=None, state=None,
                       observable=None, completed=None):
    """

        /semesterIds/{sem_id}/ob/science

    Retrieves all the science observation blocks in their entirety for a given 
    program that are observable for the night.  Excludes completed observation 
    blocks. 

    :param sem_id: semester id
    :type sem_id: dict | bytes
    :param instrument: instrument used to make observation
    :type instrument: dict | bytes
    :param min_ra: the minimum right ascension
    :type min_ra: dict | bytes
    :param max_ra: the maximum right ascension
    :type max_ra: dict | bytes
    :param ob_priority:: return results with a given priority.
    :type ob_priority:: int
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

    :rtype: List
    """
    if connexion.request.is_json:
        sem_id = SemIdSchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        instrument = InstrumentEnum.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        min_ra = RASchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        max_ra = RASchema.from_dict(connexion.request.get_json())

    query = {'metadata.sem_id': sem_id, 'metadata.ob_type': 'science'}
    result = {}

    matching_ob = utils.odt_ob_query(query, result, instrument, min_ra, max_ra,
                                     ob_priority, min_priority, max_priority,
                                     min_duration, max_duration, state,
                                     observable, completed)

    return utils.list_with_objectid(matching_ob)


@auth_utils.confirm_sem_id_associated
def sem_id_ob_metadata(sem_id, instrument=None,  min_ra=None, max_ra=None,
                       ob_priority=None, min_priority=None, max_priority=None,
                       min_duration=None, max_duration=None, state=None,
                       observable=None, completed=None):

    """sem_id_ob_metadata
       /semesterIds/{sem_id}/ob/metadata

    Retrieves all the observation blocks metadata for a given program.  The
    default is to exclude completed observation blocks.

    :param sem_id: semester id
    :type sem_id: dict | bytes
    :param instrument: instrument used to make observation
    :type instrument: dict | bytes
    :param min_ra: the minimum right ascension
    :type min_ra: dict | bytes
    :param max_ra: the maximum right ascension
    :type max_ra: dict | bytes
    :param ob_priority:: return results with a given priority.
    :type ob_priority:: int
    :param min_priority: only return results with priority greater than or
                         equal to minimum.
    :type min_priority: int
    :param max_priority: only return results with priority less than to max.
    :type max_priority: int
    :param min_duration: only return results that have a duration greater than
                         or equal to the min_duration.  The duration unit
                         is minutes.
    :type min_duration: float
    :param max_duration: only return results that have a duration less than
                         or equal to the max_duration.  The duration unit
                         is minutes.
    :type max_duration: float
    :param state: return OBs of a certain state,  the possible states are
                  defined in ‘Defined Types’.
    :type state: str
    :param observable: only return results that are observable for current
                       UT to sunrise.  The duration is not taken into
                       consideration. Default is false (0),  use
                       observable&#x3D;1 for only OBs that are observable.
    :type observable: bool
    :param completed: return results that are completed.  The default is
                      false (0),  use completed&#x3D;1 for only OBs that
                      are observable.
    :type completed: bool

    :rtype: List
    """
    if connexion.request.is_json:
        sem_id = SemIdSchema.from_dict(connexion.request.get_json())  
    if connexion.request.is_json:
        instrument = InstrumentEnum.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        min_ra = RASchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        max_ra = RASchema.from_dict(connexion.request.get_json())

    query = {'metadata.sem_id': sem_id}
    result = {'metadata': 1}

    matching_ob = utils.odt_ob_query(query, result, instrument, min_ra, max_ra,
                                     ob_priority, min_priority, max_priority,
                                     min_duration, max_duration, state,
                                     observable, completed)

    return utils.list_with_objectid(matching_ob)


@auth_utils.confirm_sem_id_associated
def sem_id_ob_targets(sem_id, instrument=None,  min_ra=None, max_ra=None,
                      ob_priority=None, min_priority=None, max_priority=None,
                      min_duration=None, max_duration=None, state=None,
                      observable=None, completed=None):
    """sem_id_ob_targets
        /semesterIds/{sem_id}/ob/targets

    Retrieves all the target components associated with a program. 

    :param sem_id: semester id
    :type sem_id: dict | bytes
    :param instrument: instrument used to make observation
    :type instrument: dict | bytes
    :param min_ra: the minimum right ascension
    :type min_ra: dict | bytes
    :param max_ra: the maximum right ascension
    :type max_ra: dict | bytes
    :param ob_priority: return results with a given priority.
    :type ob_priority: int
    :param min_priority: only return results with priority greater than or equal to minimum.
    :type min_priority: int
    :param max_priority: only return results with priority less than to max.
    :type max_priority: int
    :param min_duration: only return results that have a duration greater than or equal to the min_duration.  The duration unit is minutes.
    :type min_duration: float
    :param max_duration: only return results that have a duration less than or equal to the max_duration.  The duration unit is minutes.
    :type max_duration: float
    :param state: return OBs of a certain state,  the possible states are defined in ‘Defined Types’.
    :type state: str
    :param observable: only return results that are observable for current UT to sunrise.  The duration is not taken into consideration. Default is false (0),  use observable&#x3D;1 for only OBs that are observable.
    :type observable: bool
    :param completed: return results that are completed.  The default is false (0),  use completed&#x3D;1 for only OBs that are observable.
    :type completed: bool

    :rtype: List
    """
    if connexion.request.is_json:
        sem_id = SemIdSchema.from_dict(connexion.request.get_json())  
    if connexion.request.is_json:
        instrument = InstrumentEnum.from_dict(connexion.request.get_json())  
    if connexion.request.is_json:
        min_ra = RASchema.from_dict(connexion.request.get_json())  
    if connexion.request.is_json:
        max_ra = RASchema.from_dict(connexion.request.get_json())  

    query = {'metadata.sem_id': sem_id}
    result = {'target': 1}

    matching_ob = utils.odt_ob_query(query, result, instrument, min_ra, max_ra,
                                     ob_priority, min_priority, max_priority,
                                     min_duration, max_duration, state,
                                     observable, completed)

    return utils.list_with_objectid(matching_ob)

def sem_id_ob_observations(sem_id, min_ra=None, max_ra=None, instrument=None, ob_priority=None, min_priority=None, max_priority=None, min_duration=None, max_duration=None, state=None, observable=None, completed=None):  # noqa: E501
    """
    Retrieves all the target components associated with a program. # noqa: E501
        /semesterIds/{sem_id}/ob/observations

    :param sem_id: semester id
    :type sem_id: dict | bytes
    :param min_ra: the minimum right ascension
    :type min_ra: dict | bytes
    :param max_ra: the maximum right ascension
    :type max_ra: dict | bytes
    :param instrument: restrict results to a specific Instrument
    :type instrument: dict | bytes
    :param ob_priority: return results with a given priority.
    :type ob_priority: int
    :param min_priority: only return results with priority greater than or equal to minimum.
    :type min_priority: int
    :param max_priority: only return results with priority less than to max.
    :type max_priority: int
    :param min_duration: only return results that have a duration greater than or equal to the min_duration.  The duration unit is minutes.
    :type min_duration: float
    :param max_duration: only return results that have a duration less than or equal to the max_duration.  The duration unit is minutes.
    :type max_duration: float
    :param state: return OBs of a certain state,  the possible states are defined in ‘Defined Types’.
    :type state: str
    :param observable: only return results that are observable for current UT to sunrise.  The duration is not taken into consideration. Default is false (0),  use observable&#x3D;1 for only OBs that are observable.
    :type observable: bool
    :param completed: return results that are completed.  The default is false (0),  use completed&#x3D;1 for only OBs that are observable.
    :type completed: bool

    :rtype: List
    """
    if connexion.request.is_json:
        sem_id = SemIdSchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        min_ra = RASchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        max_ra = RASchema.from_dict(connexion.request.get_json())
    if connexion.request.is_json:
        instrument = InstrumentEnum.from_dict(connexion.request.get_json())

    query = {'metadata.sem_id': sem_id}
    result = {'observations': 1}

    matching_ob = utils.odt_ob_query(query, result, instrument, min_ra, max_ra,
                                     ob_priority, min_priority, max_priority,
                                     min_duration, max_duration, state,
                                     observable, completed)

    return utils.list_with_objectid(matching_ob)














