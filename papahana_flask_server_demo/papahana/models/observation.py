# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Observation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, instrument: str=None, index: int=None, name: str=None):  # noqa: E501
        """Observation - a model defined in Swagger

        :param instrument: The instrument of this Observation.  # noqa: E501
        :type instrument: str
        :param index: The index of this Observation.  # noqa: E501
        :type index: int
        :param name: The name of this Observation.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'instrument': str,
            'index': int,
            'name': str
        }

        self.attribute_map = {
            'instrument': 'instrument',
            'index': 'index',
            'name': 'name'
        }
        self._instrument = instrument
        self._index = index
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'Observation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Observation of this Observation.  # noqa: E501
        :rtype: Observation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def instrument(self) -> str:
        """Gets the instrument of this Observation.


        :return: The instrument of this Observation.
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument: str):
        """Sets the instrument of this Observation.


        :param instrument: The instrument of this Observation.
        :type instrument: str
        """
        if instrument is None:
            raise ValueError("Invalid value for `instrument`, must not be `None`")  # noqa: E501

        self._instrument = instrument

    @property
    def index(self) -> int:
        """Gets the index of this Observation.


        :return: The index of this Observation.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index: int):
        """Sets the index of this Observation.


        :param index: The index of this Observation.
        :type index: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def name(self) -> str:
        """Gets the name of this Observation.


        :return: The name of this Observation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Observation.


        :param name: The name of this Observation.
        :type name: str
        """

        self._name = name
