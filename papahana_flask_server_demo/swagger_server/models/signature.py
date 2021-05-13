# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Signature(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, pi_id: str=None, sem_id: str=None, instrument: str=None):  # noqa: E501
        """Signature - a model defined in Swagger

        :param name: The name of this Signature.  # noqa: E501
        :type name: str
        :param pi_id: The pi_id of this Signature.  # noqa: E501
        :type pi_id: str
        :param sem_id: The sem_id of this Signature.  # noqa: E501
        :type sem_id: str
        :param instrument: The instrument of this Signature.  # noqa: E501
        :type instrument: str
        """
        self.swagger_types = {
            'name': str,
            'pi_id': str,
            'sem_id': str,
            'instrument': str
        }

        self.attribute_map = {
            'name': 'name',
            'pi_id': 'pi_id',
            'sem_id': 'sem_id',
            'instrument': 'instrument'
        }
        self._name = name
        self._pi_id = pi_id
        self._sem_id = sem_id
        self._instrument = instrument

    @classmethod
    def from_dict(cls, dikt) -> 'Signature':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Signature of this Signature.  # noqa: E501
        :rtype: Signature
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Signature.


        :return: The name of this Signature.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Signature.


        :param name: The name of this Signature.
        :type name: str
        """

        self._name = name

    @property
    def pi_id(self) -> str:
        """Gets the pi_id of this Signature.


        :return: The pi_id of this Signature.
        :rtype: str
        """
        return self._pi_id

    @pi_id.setter
    def pi_id(self, pi_id: str):
        """Sets the pi_id of this Signature.


        :param pi_id: The pi_id of this Signature.
        :type pi_id: str
        """

        self._pi_id = pi_id

    @property
    def sem_id(self) -> str:
        """Gets the sem_id of this Signature.


        :return: The sem_id of this Signature.
        :rtype: str
        """
        return self._sem_id

    @sem_id.setter
    def sem_id(self, sem_id: str):
        """Sets the sem_id of this Signature.


        :param sem_id: The sem_id of this Signature.
        :type sem_id: str
        """

        self._sem_id = sem_id

    @property
    def instrument(self) -> str:
        """Gets the instrument of this Signature.


        :return: The instrument of this Signature.
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument: str):
        """Sets the instrument of this Signature.


        :param instrument: The instrument of this Signature.
        :type instrument: str
        """

        self._instrument = instrument
