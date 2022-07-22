import connexion
import six

from papahana.models.instrument_enum import InstrumentEnum  
from papahana.models.ra_schema import RASchema  
from papahana.models.sem_id_schema import SemIdSchema  
from papahana import util


def search_ob(tag_name=None, sem_id=None, min_ra=None, max_ra=None,
              instrument=None, ob_priority=None, min_priority=None,
              max_priority=None, min_duration=None, max_duration=None,
              state=None, observable=None, completed=None, container_id=None):
    """search_ob

    Retrieves all the OBs associated with the search parameters. 

    :param tag_name: a tag to search on
    :type tag_name: str
    :param sem_id: program id including semester
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
    :param min_duration: only return results that have a duration greater than or equal to the min_duration. The duration unit is minutes.
    :type min_duration: float
    :param max_duration: only return results that have a duration less than or equal to the max_duration.  The duration unit is minutes.
    :type max_duration: float
    :param state: return OBs of a certain state,  the possible states are defined in ‘Defined Types’.
    :type state: str
    :param observable: only return results that are observable for current UT to sunrise.  The duration is not taken into consideration. Default is false (0),  use observable&#x3D;1 for only OBs that are observable.
    :type observable: bool
    :param completed: return results that are completed.  The default is false (0), use completed&#x3D;1 for only OBs that are observable.
    :type completed: bool
    :param container_id: ObjectId of the container identifier.
    :type container_id: str

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
    return 'do some magic!'


def search_ob_inst_config(tag_name=None, sem_id=None, min_ra=None, max_ra=None, instrument=None, ob_priority=None, min_priority=None, max_priority=None, min_duration=None, max_duration=None, state=None, observable=None, completed=None, container_id=None):  
    """search_ob_inst_config

    Retrieves all the OB components associated with the search parameters. 

    :param tag_name: a tag to search on
    :type tag_name: str
    :param sem_id: program id including semester
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
    :param min_duration: only return results that have a duration greater than or equal to the min_duration. The duration unit is minutes.
    :type min_duration: float
    :param max_duration: only return results that have a duration less than or equal to the max_duration.  The duration unit is minutes.
    :type max_duration: float
    :param state: return OBs of a certain state,  the possible states are defined in ‘Defined Types’.
    :type state: str
    :param observable: only return results that are observable for current UT to sunrise.  The duration is not taken into consideration. Default is false (0),  use observable&#x3D;1 for only OBs that are observable.
    :type observable: bool
    :param completed: return results that are completed.  The default is false (0), use completed&#x3D;1 for only OBs that are observable.
    :type completed: bool
    :param container_id: ObjectId of the container identifier.
    :type container_id: str

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
    return 'do some magic!'
