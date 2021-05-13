# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Status(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, state: str=None, executions: List[str]=None):  # noqa: E501
        """Status - a model defined in Swagger

        :param state: The state of this Status.  # noqa: E501
        :type state: str
        :param executions: The executions of this Status.  # noqa: E501
        :type executions: List[str]
        """
        self.swagger_types = {
            'state': str,
            'executions': List[str]
        }

        self.attribute_map = {
            'state': 'state',
            'executions': 'executions'
        }
        self._state = state
        self._executions = executions

    @classmethod
    def from_dict(cls, dikt) -> 'Status':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Status of this Status.  # noqa: E501
        :rtype: Status
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self) -> str:
        """Gets the state of this Status.


        :return: The state of this Status.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this Status.


        :param state: The state of this Status.
        :type state: str
        """

        self._state = state

    @property
    def executions(self) -> List[str]:
        """Gets the executions of this Status.


        :return: The executions of this Status.
        :rtype: List[str]
        """
        return self._executions

    @executions.setter
    def executions(self, executions: List[str]):
        """Sets the executions of this Status.


        :param executions: The executions of this Status.
        :type executions: List[str]
        """

        self._executions = executions