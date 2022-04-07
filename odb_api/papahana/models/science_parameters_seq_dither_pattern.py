# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana import util


class ScienceParametersSeqDitherPattern(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, seq_dither_slitoffset: float=None, seq_dither_ra_offset: float=None, seq_dither_dec_offset: float=None, seq_dither_position: str=None, seq_dither_guided: bool=None):  # noqa: E501
        """ScienceParametersSeqDitherPattern - a model defined in Swagger

        :param seq_dither_slitoffset: The seq_dither_slitoffset of this ScienceParametersSeqDitherPattern.  # noqa: E501
        :type seq_dither_slitoffset: float
        :param seq_dither_ra_offset: The seq_dither_ra_offset of this ScienceParametersSeqDitherPattern.  # noqa: E501
        :type seq_dither_ra_offset: float
        :param seq_dither_dec_offset: The seq_dither_dec_offset of this ScienceParametersSeqDitherPattern.  # noqa: E501
        :type seq_dither_dec_offset: float
        :param seq_dither_position: The seq_dither_position of this ScienceParametersSeqDitherPattern.  # noqa: E501
        :type seq_dither_position: str
        :param seq_dither_guided: The seq_dither_guided of this ScienceParametersSeqDitherPattern.  # noqa: E501
        :type seq_dither_guided: bool
        """
        self.swagger_types = {
            'seq_dither_slitoffset': float,
            'seq_dither_ra_offset': float,
            'seq_dither_dec_offset': float,
            'seq_dither_position': str,
            'seq_dither_guided': bool
        }

        self.attribute_map = {
            'seq_dither_slitoffset': 'seq_dither_slitoffset',
            'seq_dither_ra_offset': 'seq_dither_ra_offset',
            'seq_dither_dec_offset': 'seq_dither_dec_offset',
            'seq_dither_position': 'seq_dither_position',
            'seq_dither_guided': 'seq_dither_guided'
        }
        self._seq_dither_slitoffset = seq_dither_slitoffset
        self._seq_dither_ra_offset = seq_dither_ra_offset
        self._seq_dither_dec_offset = seq_dither_dec_offset
        self._seq_dither_position = seq_dither_position
        self._seq_dither_guided = seq_dither_guided

    @classmethod
    def from_dict(cls, dikt) -> 'ScienceParametersSeqDitherPattern':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScienceParameters_seq_dither_pattern of this ScienceParametersSeqDitherPattern.  # noqa: E501
        :rtype: ScienceParametersSeqDitherPattern
        """
        return util.deserialize_model(dikt, cls)

    @property
    def seq_dither_slitoffset(self) -> float:
        """Gets the seq_dither_slitoffset of this ScienceParametersSeqDitherPattern.


        :return: The seq_dither_slitoffset of this ScienceParametersSeqDitherPattern.
        :rtype: float
        """
        return self._seq_dither_slitoffset

    @seq_dither_slitoffset.setter
    def seq_dither_slitoffset(self, seq_dither_slitoffset: float):
        """Sets the seq_dither_slitoffset of this ScienceParametersSeqDitherPattern.


        :param seq_dither_slitoffset: The seq_dither_slitoffset of this ScienceParametersSeqDitherPattern.
        :type seq_dither_slitoffset: float
        """

        self._seq_dither_slitoffset = seq_dither_slitoffset

    @property
    def seq_dither_ra_offset(self) -> float:
        """Gets the seq_dither_ra_offset of this ScienceParametersSeqDitherPattern.


        :return: The seq_dither_ra_offset of this ScienceParametersSeqDitherPattern.
        :rtype: float
        """
        return self._seq_dither_ra_offset

    @seq_dither_ra_offset.setter
    def seq_dither_ra_offset(self, seq_dither_ra_offset: float):
        """Sets the seq_dither_ra_offset of this ScienceParametersSeqDitherPattern.


        :param seq_dither_ra_offset: The seq_dither_ra_offset of this ScienceParametersSeqDitherPattern.
        :type seq_dither_ra_offset: float
        """

        self._seq_dither_ra_offset = seq_dither_ra_offset

    @property
    def seq_dither_dec_offset(self) -> float:
        """Gets the seq_dither_dec_offset of this ScienceParametersSeqDitherPattern.


        :return: The seq_dither_dec_offset of this ScienceParametersSeqDitherPattern.
        :rtype: float
        """
        return self._seq_dither_dec_offset

    @seq_dither_dec_offset.setter
    def seq_dither_dec_offset(self, seq_dither_dec_offset: float):
        """Sets the seq_dither_dec_offset of this ScienceParametersSeqDitherPattern.


        :param seq_dither_dec_offset: The seq_dither_dec_offset of this ScienceParametersSeqDitherPattern.
        :type seq_dither_dec_offset: float
        """

        self._seq_dither_dec_offset = seq_dither_dec_offset

    @property
    def seq_dither_position(self) -> str:
        """Gets the seq_dither_position of this ScienceParametersSeqDitherPattern.


        :return: The seq_dither_position of this ScienceParametersSeqDitherPattern.
        :rtype: str
        """
        return self._seq_dither_position

    @seq_dither_position.setter
    def seq_dither_position(self, seq_dither_position: str):
        """Sets the seq_dither_position of this ScienceParametersSeqDitherPattern.


        :param seq_dither_position: The seq_dither_position of this ScienceParametersSeqDitherPattern.
        :type seq_dither_position: str
        """
        allowed_values = ["T", "S", "O"]  # noqa: E501
        if seq_dither_position not in allowed_values:
            raise ValueError(
                "Invalid value for `seq_dither_position` ({0}), must be one of {1}"
                .format(seq_dither_position, allowed_values)
            )

        self._seq_dither_position = seq_dither_position

    @property
    def seq_dither_guided(self) -> bool:
        """Gets the seq_dither_guided of this ScienceParametersSeqDitherPattern.


        :return: The seq_dither_guided of this ScienceParametersSeqDitherPattern.
        :rtype: bool
        """
        return self._seq_dither_guided

    @seq_dither_guided.setter
    def seq_dither_guided(self, seq_dither_guided: bool):
        """Sets the seq_dither_guided of this ScienceParametersSeqDitherPattern.


        :param seq_dither_guided: The seq_dither_guided of this ScienceParametersSeqDitherPattern.
        :type seq_dither_guided: bool
        """

        self._seq_dither_guided = seq_dither_guided
