# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Metadata(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, sem_id: str=None, instrument: str=None, pi_id: int=None, observer_ids: List[int]=None):  # noqa: E501
        """Metadata - a model defined in Swagger

        :param name: The name of this Metadata.  # noqa: E501
        :type name: str
        :param sem_id: The sem_id of this Metadata.  # noqa: E501
        :type sem_id: str
        :param instrument: The instrument of this Metadata.  # noqa: E501
        :type instrument: str
        :param pi_id: The pi_id of this Metadata.  # noqa: E501
        :type pi_id: int
        :param observer_ids: The observer_ids of this Metadata.  # noqa: E501
        :type observer_ids: List[int]
        """
        self.swagger_types = {
            'name': str,
            'sem_id': str,
            'instrument': str,
            'pi_id': int,
            'observer_ids': List[int]
        }

        self.attribute_map = {
            'name': 'name',
            'sem_id': 'sem_id',
            'instrument': 'instrument',
            'pi_id': 'pi_id',
            'observer_ids': 'observer_ids'
        }
        self._name = name
        self._sem_id = sem_id
        self._instrument = instrument
        self._pi_id = pi_id
        self._observer_ids = observer_ids

    @classmethod
    def from_dict(cls, dikt) -> 'Metadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Metadata of this Metadata.  # noqa: E501
        :rtype: Metadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Metadata.


        :return: The name of this Metadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Metadata.


        :param name: The name of this Metadata.
        :type name: str
        """

        self._name = name

    @property
    def sem_id(self) -> str:
        """Gets the sem_id of this Metadata.


        :return: The sem_id of this Metadata.
        :rtype: str
        """
        return self._sem_id

    @sem_id.setter
    def sem_id(self, sem_id: str):
        """Sets the sem_id of this Metadata.


        :param sem_id: The sem_id of this Metadata.
        :type sem_id: str
        """

        self._sem_id = sem_id

    @property
    def instrument(self) -> str:
        """Gets the instrument of this Metadata.


        :return: The instrument of this Metadata.
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument: str):
        """Sets the instrument of this Metadata.


        :param instrument: The instrument of this Metadata.
        :type instrument: str
        """

        self._instrument = instrument

    @property
    def pi_id(self) -> int:
        """Gets the pi_id of this Metadata.


        :return: The pi_id of this Metadata.
        :rtype: int
        """
        return self._pi_id

    @pi_id.setter
    def pi_id(self, pi_id: int):
        """Sets the pi_id of this Metadata.


        :param pi_id: The pi_id of this Metadata.
        :type pi_id: int
        """

        self._pi_id = pi_id

    @property
    def observer_ids(self) -> List[int]:
        """Gets the observer_ids of this Metadata.


        :return: The observer_ids of this Metadata.
        :rtype: List[int]
        """
        return self._observer_ids

    @observer_ids.setter
    def observer_ids(self, observer_ids: List[int]):
        """Sets the observer_ids of this Metadata.


        :param observer_ids: The observer_ids of this Metadata.
        :type observer_ids: List[int]
        """

        self._observer_ids = observer_ids
