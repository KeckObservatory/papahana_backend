# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana import util


class StatusField(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, state: int=0, current_seq: int=0, current_step: int=0, current_exp_det1: int=0, current_exp_det2: int=0):  # noqa: E501
        """StatusField - a model defined in Swagger

        :param state: The state of this StatusField.  # noqa: E501
        :type state: int
        :param current_seq: The current_seq of this StatusField.  # noqa: E501
        :type current_seq: int
        :param current_step: The current_step of this StatusField.  # noqa: E501
        :type current_step: int
        :param current_exp_det1: The current_exp_det1 of this StatusField.  # noqa: E501
        :type current_exp_det1: int
        :param current_exp_det2: The current_exp_det2 of this StatusField.  # noqa: E501
        :type current_exp_det2: int
        """
        self.swagger_types = {
            'state': int,
            'current_seq': int,
            'current_step': int,
            'current_exp_det1': int,
            'current_exp_det2': int
        }

        self.attribute_map = {
            'state': 'state',
            'current_seq': 'current_seq',
            'current_step': 'current_step',
            'current_exp_det1': 'current_exp_det1',
            'current_exp_det2': 'current_exp_det2'
        }
        self._state = state
        self._current_seq = current_seq
        self._current_step = current_step
        self._current_exp_det1 = current_exp_det1
        self._current_exp_det2 = current_exp_det2

    @classmethod
    def from_dict(cls, dikt) -> 'StatusField':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StatusField of this StatusField.  # noqa: E501
        :rtype: StatusField
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self) -> int:
        """Gets the state of this StatusField.


        :return: The state of this StatusField.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state: int):
        """Sets the state of this StatusField.


        :param state: The state of this StatusField.
        :type state: int
        """

        self._state = state

    @property
    def current_seq(self) -> int:
        """Gets the current_seq of this StatusField.


        :return: The current_seq of this StatusField.
        :rtype: int
        """
        return self._current_seq

    @current_seq.setter
    def current_seq(self, current_seq: int):
        """Sets the current_seq of this StatusField.


        :param current_seq: The current_seq of this StatusField.
        :type current_seq: int
        """

        self._current_seq = current_seq

    @property
    def current_step(self) -> int:
        """Gets the current_step of this StatusField.


        :return: The current_step of this StatusField.
        :rtype: int
        """
        return self._current_step

    @current_step.setter
    def current_step(self, current_step: int):
        """Sets the current_step of this StatusField.


        :param current_step: The current_step of this StatusField.
        :type current_step: int
        """

        self._current_step = current_step

    @property
    def current_exp_det1(self) -> int:
        """Gets the current_exp_det1 of this StatusField.


        :return: The current_exp_det1 of this StatusField.
        :rtype: int
        """
        return self._current_exp_det1

    @current_exp_det1.setter
    def current_exp_det1(self, current_exp_det1: int):
        """Sets the current_exp_det1 of this StatusField.


        :param current_exp_det1: The current_exp_det1 of this StatusField.
        :type current_exp_det1: int
        """

        self._current_exp_det1 = current_exp_det1

    @property
    def current_exp_det2(self) -> int:
        """Gets the current_exp_det2 of this StatusField.


        :return: The current_exp_det2 of this StatusField.
        :rtype: int
        """
        return self._current_exp_det2

    @current_exp_det2.setter
    def current_exp_det2(self, current_exp_det2: int):
        """Sets the current_exp_det2 of this StatusField.


        :param current_exp_det2: The current_exp_det2 of this StatusField.
        :type current_exp_det2: int
        """

        self._current_exp_det2 = current_exp_det2
