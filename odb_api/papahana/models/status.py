# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana.models.date_schema import DateSchema  # noqa: F401,E501
from papahana import util


class Status(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, state: int=0, current_seq: int=0, current_step: int=0, current_exp_det1: int=0, current_exp_det2: int=0, executions: List[DateSchema]=None, deleted: bool=False):  # noqa: E501
        """Status - a model defined in Swagger

        :param state: The state of this Status.  # noqa: E501
        :type state: int
        :param current_seq: The current_seq of this Status.  # noqa: E501
        :type current_seq: int
        :param current_step: The current_step of this Status.  # noqa: E501
        :type current_step: int
        :param current_exp_det1: The current_exp_det1 of this Status.  # noqa: E501
        :type current_exp_det1: int
        :param current_exp_det2: The current_exp_det2 of this Status.  # noqa: E501
        :type current_exp_det2: int
        :param executions: The executions of this Status.  # noqa: E501
        :type executions: List[DateSchema]
        :param deleted: The deleted of this Status.  # noqa: E501
        :type deleted: bool
        """
        self.swagger_types = {
            'state': int,
            'current_seq': int,
            'current_step': int,
            'current_exp_det1': int,
            'current_exp_det2': int,
            'executions': List[DateSchema],
            'deleted': bool
        }

        self.attribute_map = {
            'state': 'state',
            'current_seq': 'current_seq',
            'current_step': 'current_step',
            'current_exp_det1': 'current_exp_det1',
            'current_exp_det2': 'current_exp_det2',
            'executions': 'executions',
            'deleted': 'deleted'
        }
        self._state = state
        self._current_seq = current_seq
        self._current_step = current_step
        self._current_exp_det1 = current_exp_det1
        self._current_exp_det2 = current_exp_det2
        self._executions = executions
        self._deleted = deleted

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
    def state(self) -> int:
        """Gets the state of this Status.


        :return: The state of this Status.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state: int):
        """Sets the state of this Status.


        :param state: The state of this Status.
        :type state: int
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def current_seq(self) -> int:
        """Gets the current_seq of this Status.


        :return: The current_seq of this Status.
        :rtype: int
        """
        return self._current_seq

    @current_seq.setter
    def current_seq(self, current_seq: int):
        """Sets the current_seq of this Status.


        :param current_seq: The current_seq of this Status.
        :type current_seq: int
        """
        if current_seq is None:
            raise ValueError("Invalid value for `current_seq`, must not be `None`")  # noqa: E501

        self._current_seq = current_seq

    @property
    def current_step(self) -> int:
        """Gets the current_step of this Status.


        :return: The current_step of this Status.
        :rtype: int
        """
        return self._current_step

    @current_step.setter
    def current_step(self, current_step: int):
        """Sets the current_step of this Status.


        :param current_step: The current_step of this Status.
        :type current_step: int
        """
        if current_step is None:
            raise ValueError("Invalid value for `current_step`, must not be `None`")  # noqa: E501

        self._current_step = current_step

    @property
    def current_exp_det1(self) -> int:
        """Gets the current_exp_det1 of this Status.


        :return: The current_exp_det1 of this Status.
        :rtype: int
        """
        return self._current_exp_det1

    @current_exp_det1.setter
    def current_exp_det1(self, current_exp_det1: int):
        """Sets the current_exp_det1 of this Status.


        :param current_exp_det1: The current_exp_det1 of this Status.
        :type current_exp_det1: int
        """
        if current_exp_det1 is None:
            raise ValueError("Invalid value for `current_exp_det1`, must not be `None`")  # noqa: E501

        self._current_exp_det1 = current_exp_det1

    @property
    def current_exp_det2(self) -> int:
        """Gets the current_exp_det2 of this Status.


        :return: The current_exp_det2 of this Status.
        :rtype: int
        """
        return self._current_exp_det2

    @current_exp_det2.setter
    def current_exp_det2(self, current_exp_det2: int):
        """Sets the current_exp_det2 of this Status.


        :param current_exp_det2: The current_exp_det2 of this Status.
        :type current_exp_det2: int
        """
        if current_exp_det2 is None:
            raise ValueError("Invalid value for `current_exp_det2`, must not be `None`")  # noqa: E501

        self._current_exp_det2 = current_exp_det2

    @property
    def executions(self) -> List[DateSchema]:
        """Gets the executions of this Status.


        :return: The executions of this Status.
        :rtype: List[DateSchema]
        """
        return self._executions

    @executions.setter
    def executions(self, executions: List[DateSchema]):
        """Sets the executions of this Status.


        :param executions: The executions of this Status.
        :type executions: List[DateSchema]
        """
        if executions is None:
            raise ValueError("Invalid value for `executions`, must not be `None`")  # noqa: E501

        self._executions = executions

    @property
    def deleted(self) -> bool:
        """Gets the deleted of this Status.


        :return: The deleted of this Status.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted: bool):
        """Sets the deleted of this Status.


        :param deleted: The deleted of this Status.
        :type deleted: bool
        """
        if deleted is None:
            raise ValueError("Invalid value for `deleted`, must not be `None`")  # noqa: E501

        self._deleted = deleted
