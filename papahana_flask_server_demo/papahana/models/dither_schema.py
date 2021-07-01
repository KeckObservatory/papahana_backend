# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana import util


class DitherSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ra: float=None, dec: float=None, position: str=None, guided: bool=None):  # noqa: E501
        """DitherSchema - a model defined in Swagger

        :param ra: The ra of this DitherSchema.  # noqa: E501
        :type ra: float
        :param dec: The dec of this DitherSchema.  # noqa: E501
        :type dec: float
        :param position: The position of this DitherSchema.  # noqa: E501
        :type position: str
        :param guided: The guided of this DitherSchema.  # noqa: E501
        :type guided: bool
        """
        self.swagger_types = {
            'ra': float,
            'dec': float,
            'position': str,
            'guided': bool
        }

        self.attribute_map = {
            'ra': 'ra',
            'dec': 'dec',
            'position': 'position',
            'guided': 'guided'
        }
        self._ra = ra
        self._dec = dec
        self._position = position
        self._guided = guided

    @classmethod
    def from_dict(cls, dikt) -> 'DitherSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DitherSchema of this DitherSchema.  # noqa: E501
        :rtype: DitherSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ra(self) -> float:
        """Gets the ra of this DitherSchema.


        :return: The ra of this DitherSchema.
        :rtype: float
        """
        return self._ra

    @ra.setter
    def ra(self, ra: float):
        """Sets the ra of this DitherSchema.


        :param ra: The ra of this DitherSchema.
        :type ra: float
        """
        if ra is None:
            raise ValueError("Invalid value for `ra`, must not be `None`")  # noqa: E501

        self._ra = ra

    @property
    def dec(self) -> float:
        """Gets the dec of this DitherSchema.


        :return: The dec of this DitherSchema.
        :rtype: float
        """
        return self._dec

    @dec.setter
    def dec(self, dec: float):
        """Sets the dec of this DitherSchema.


        :param dec: The dec of this DitherSchema.
        :type dec: float
        """
        if dec is None:
            raise ValueError("Invalid value for `dec`, must not be `None`")  # noqa: E501

        self._dec = dec

    @property
    def position(self) -> str:
        """Gets the position of this DitherSchema.


        :return: The position of this DitherSchema.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position: str):
        """Sets the position of this DitherSchema.


        :param position: The position of this DitherSchema.
        :type position: str
        """
        allowed_values = ["T", "S", "O"]  # noqa: E501
        if position not in allowed_values:
            raise ValueError(
                "Invalid value for `position` ({0}), must be one of {1}"
                .format(position, allowed_values)
            )

        self._position = position

    @property
    def guided(self) -> bool:
        """Gets the guided of this DitherSchema.


        :return: The guided of this DitherSchema.
        :rtype: bool
        """
        return self._guided

    @guided.setter
    def guided(self, guided: bool):
        """Sets the guided of this DitherSchema.


        :param guided: The guided of this DitherSchema.
        :type guided: bool
        """
        if guided is None:
            raise ValueError("Invalid value for `guided`, must not be `None`")  # noqa: E501

        self._guided = guided