# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana.models.dec_schema import DecSchema  # noqa: F401,E501
from papahana.models.ra_schema import RASchema  # noqa: F401,E501
from papahana import util


class AcquisitionParameters(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, wrap: str='auto', rotmode: str=None, guider_po: str=None, ra_offset: float=None, dec_offset: float=None, guider_gs_ra: RASchema=None, guider_gs_dec: DecSchema=None, guider_gs_mode: str=None):  # noqa: E501
        """AcquisitionParameters - a model defined in Swagger

        :param wrap: The wrap of this AcquisitionParameters.  # noqa: E501
        :type wrap: str
        :param rotmode: The rotmode of this AcquisitionParameters.  # noqa: E501
        :type rotmode: str
        :param guider_po: The guider_po of this AcquisitionParameters.  # noqa: E501
        :type guider_po: str
        :param ra_offset: The ra_offset of this AcquisitionParameters.  # noqa: E501
        :type ra_offset: float
        :param dec_offset: The dec_offset of this AcquisitionParameters.  # noqa: E501
        :type dec_offset: float
        :param guider_gs_ra: The guider_gs_ra of this AcquisitionParameters.  # noqa: E501
        :type guider_gs_ra: RASchema
        :param guider_gs_dec: The guider_gs_dec of this AcquisitionParameters.  # noqa: E501
        :type guider_gs_dec: DecSchema
        :param guider_gs_mode: The guider_gs_mode of this AcquisitionParameters.  # noqa: E501
        :type guider_gs_mode: str
        """
        self.swagger_types = {
            'wrap': str,
            'rotmode': str,
            'guider_po': str,
            'ra_offset': float,
            'dec_offset': float,
            'guider_gs_ra': RASchema,
            'guider_gs_dec': DecSchema,
            'guider_gs_mode': str
        }

        self.attribute_map = {
            'wrap': 'wrap',
            'rotmode': 'rotmode',
            'guider_po': 'guider_po',
            'ra_offset': 'ra_offset',
            'dec_offset': 'dec_offset',
            'guider_gs_ra': 'guider_gs_ra',
            'guider_gs_dec': 'guider_gs_dec',
            'guider_gs_mode': 'guider_gs_mode'
        }
        self._wrap = wrap
        self._rotmode = rotmode
        self._guider_po = guider_po
        self._ra_offset = ra_offset
        self._dec_offset = dec_offset
        self._guider_gs_ra = guider_gs_ra
        self._guider_gs_dec = guider_gs_dec
        self._guider_gs_mode = guider_gs_mode

    @classmethod
    def from_dict(cls, dikt) -> 'AcquisitionParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AcquisitionParameters of this AcquisitionParameters.  # noqa: E501
        :rtype: AcquisitionParameters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def wrap(self) -> str:
        """Gets the wrap of this AcquisitionParameters.


        :return: The wrap of this AcquisitionParameters.
        :rtype: str
        """
        return self._wrap

    @wrap.setter
    def wrap(self, wrap: str):
        """Sets the wrap of this AcquisitionParameters.


        :param wrap: The wrap of this AcquisitionParameters.
        :type wrap: str
        """
        allowed_values = ["south", "north", "auto"]  # noqa: E501
        if wrap not in allowed_values:
            raise ValueError(
                "Invalid value for `wrap` ({0}), must be one of {1}"
                .format(wrap, allowed_values)
            )

        self._wrap = wrap

    @property
    def rotmode(self) -> str:
        """Gets the rotmode of this AcquisitionParameters.


        :return: The rotmode of this AcquisitionParameters.
        :rtype: str
        """
        return self._rotmode

    @rotmode.setter
    def rotmode(self, rotmode: str):
        """Sets the rotmode of this AcquisitionParameters.


        :param rotmode: The rotmode of this AcquisitionParameters.
        :type rotmode: str
        """
        allowed_values = ["PA", "stationary", "vertical_angle"]  # noqa: E501
        if rotmode not in allowed_values:
            raise ValueError(
                "Invalid value for `rotmode` ({0}), must be one of {1}"
                .format(rotmode, allowed_values)
            )

        self._rotmode = rotmode

    @property
    def guider_po(self) -> str:
        """Gets the guider_po of this AcquisitionParameters.


        :return: The guider_po of this AcquisitionParameters.
        :rtype: str
        """
        return self._guider_po

    @guider_po.setter
    def guider_po(self, guider_po: str):
        """Sets the guider_po of this AcquisitionParameters.


        :param guider_po: The guider_po of this AcquisitionParameters.
        :type guider_po: str
        """
        allowed_values = ["REF", "IFU"]  # noqa: E501
        if guider_po not in allowed_values:
            raise ValueError(
                "Invalid value for `guider_po` ({0}), must be one of {1}"
                .format(guider_po, allowed_values)
            )

        self._guider_po = guider_po

    @property
    def ra_offset(self) -> float:
        """Gets the ra_offset of this AcquisitionParameters.


        :return: The ra_offset of this AcquisitionParameters.
        :rtype: float
        """
        return self._ra_offset

    @ra_offset.setter
    def ra_offset(self, ra_offset: float):
        """Sets the ra_offset of this AcquisitionParameters.


        :param ra_offset: The ra_offset of this AcquisitionParameters.
        :type ra_offset: float
        """

        self._ra_offset = ra_offset

    @property
    def dec_offset(self) -> float:
        """Gets the dec_offset of this AcquisitionParameters.


        :return: The dec_offset of this AcquisitionParameters.
        :rtype: float
        """
        return self._dec_offset

    @dec_offset.setter
    def dec_offset(self, dec_offset: float):
        """Sets the dec_offset of this AcquisitionParameters.


        :param dec_offset: The dec_offset of this AcquisitionParameters.
        :type dec_offset: float
        """

        self._dec_offset = dec_offset

    @property
    def guider_gs_ra(self) -> RASchema:
        """Gets the guider_gs_ra of this AcquisitionParameters.


        :return: The guider_gs_ra of this AcquisitionParameters.
        :rtype: RASchema
        """
        return self._guider_gs_ra

    @guider_gs_ra.setter
    def guider_gs_ra(self, guider_gs_ra: RASchema):
        """Sets the guider_gs_ra of this AcquisitionParameters.


        :param guider_gs_ra: The guider_gs_ra of this AcquisitionParameters.
        :type guider_gs_ra: RASchema
        """

        self._guider_gs_ra = guider_gs_ra

    @property
    def guider_gs_dec(self) -> DecSchema:
        """Gets the guider_gs_dec of this AcquisitionParameters.


        :return: The guider_gs_dec of this AcquisitionParameters.
        :rtype: DecSchema
        """
        return self._guider_gs_dec

    @guider_gs_dec.setter
    def guider_gs_dec(self, guider_gs_dec: DecSchema):
        """Sets the guider_gs_dec of this AcquisitionParameters.


        :param guider_gs_dec: The guider_gs_dec of this AcquisitionParameters.
        :type guider_gs_dec: DecSchema
        """

        self._guider_gs_dec = guider_gs_dec

    @property
    def guider_gs_mode(self) -> str:
        """Gets the guider_gs_mode of this AcquisitionParameters.


        :return: The guider_gs_mode of this AcquisitionParameters.
        :rtype: str
        """
        return self._guider_gs_mode

    @guider_gs_mode.setter
    def guider_gs_mode(self, guider_gs_mode: str):
        """Sets the guider_gs_mode of this AcquisitionParameters.


        :param guider_gs_mode: The guider_gs_mode of this AcquisitionParameters.
        :type guider_gs_mode: str
        """
        allowed_values = ["auto", "operator", "user"]  # noqa: E501
        if guider_gs_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `guider_gs_mode` ({0}), must be one of {1}"
                .format(guider_gs_mode, allowed_values)
            )

        self._guider_gs_mode = guider_gs_mode