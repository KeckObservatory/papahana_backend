# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.magnitude import Magnitude  # noqa: F401,E501
from swagger_server import util


class Target(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, ra: str=None, dec: str=None, equinox: float=None, pa: float=None, frame: str=None, ra_offset: float=None, dec_offset: float=None, pm_ra: float=None, pm_dec: float=None, epoch: float=None, obstime: float=None, mag: List[Magnitude]=None, wrap: str=None, d_ra: float=None, d_dec: float=None, comment: str=None):  # noqa: E501
        """Target - a model defined in Swagger

        :param name: The name of this Target.  # noqa: E501
        :type name: str
        :param ra: The ra of this Target.  # noqa: E501
        :type ra: str
        :param dec: The dec of this Target.  # noqa: E501
        :type dec: str
        :param equinox: The equinox of this Target.  # noqa: E501
        :type equinox: float
        :param pa: The pa of this Target.  # noqa: E501
        :type pa: float
        :param frame: The frame of this Target.  # noqa: E501
        :type frame: str
        :param ra_offset: The ra_offset of this Target.  # noqa: E501
        :type ra_offset: float
        :param dec_offset: The dec_offset of this Target.  # noqa: E501
        :type dec_offset: float
        :param pm_ra: The pm_ra of this Target.  # noqa: E501
        :type pm_ra: float
        :param pm_dec: The pm_dec of this Target.  # noqa: E501
        :type pm_dec: float
        :param epoch: The epoch of this Target.  # noqa: E501
        :type epoch: float
        :param obstime: The obstime of this Target.  # noqa: E501
        :type obstime: float
        :param mag: The mag of this Target.  # noqa: E501
        :type mag: List[Magnitude]
        :param wrap: The wrap of this Target.  # noqa: E501
        :type wrap: str
        :param d_ra: The d_ra of this Target.  # noqa: E501
        :type d_ra: float
        :param d_dec: The d_dec of this Target.  # noqa: E501
        :type d_dec: float
        :param comment: The comment of this Target.  # noqa: E501
        :type comment: str
        """
        self.swagger_types = {
            'name': str,
            'ra': str,
            'dec': str,
            'equinox': float,
            'pa': float,
            'frame': str,
            'ra_offset': float,
            'dec_offset': float,
            'pm_ra': float,
            'pm_dec': float,
            'epoch': float,
            'obstime': float,
            'mag': List[Magnitude],
            'wrap': str,
            'd_ra': float,
            'd_dec': float,
            'comment': str
        }

        self.attribute_map = {
            'name': 'name',
            'ra': 'ra',
            'dec': 'dec',
            'equinox': 'equinox',
            'pa': 'pa',
            'frame': 'frame',
            'ra_offset': 'ra_offset',
            'dec_offset': 'dec_offset',
            'pm_ra': 'pm_ra',
            'pm_dec': 'pm_dec',
            'epoch': 'epoch',
            'obstime': 'obstime',
            'mag': 'mag',
            'wrap': 'wrap?',
            'd_ra': 'd_ra',
            'd_dec': 'd_dec',
            'comment': 'comment?'
        }
        self._name = name
        self._ra = ra
        self._dec = dec
        self._equinox = equinox
        self._pa = pa
        self._frame = frame
        self._ra_offset = ra_offset
        self._dec_offset = dec_offset
        self._pm_ra = pm_ra
        self._pm_dec = pm_dec
        self._epoch = epoch
        self._obstime = obstime
        self._mag = mag
        self._wrap = wrap
        self._d_ra = d_ra
        self._d_dec = d_dec
        self._comment = comment

    @classmethod
    def from_dict(cls, dikt) -> 'Target':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Target of this Target.  # noqa: E501
        :rtype: Target
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Target.


        :return: The name of this Target.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Target.


        :param name: The name of this Target.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ra(self) -> str:
        """Gets the ra of this Target.


        :return: The ra of this Target.
        :rtype: str
        """
        return self._ra

    @ra.setter
    def ra(self, ra: str):
        """Sets the ra of this Target.


        :param ra: The ra of this Target.
        :type ra: str
        """
        if ra is None:
            raise ValueError("Invalid value for `ra`, must not be `None`")  # noqa: E501

        self._ra = ra

    @property
    def dec(self) -> str:
        """Gets the dec of this Target.


        :return: The dec of this Target.
        :rtype: str
        """
        return self._dec

    @dec.setter
    def dec(self, dec: str):
        """Sets the dec of this Target.


        :param dec: The dec of this Target.
        :type dec: str
        """
        if dec is None:
            raise ValueError("Invalid value for `dec`, must not be `None`")  # noqa: E501

        self._dec = dec

    @property
    def equinox(self) -> float:
        """Gets the equinox of this Target.


        :return: The equinox of this Target.
        :rtype: float
        """
        return self._equinox

    @equinox.setter
    def equinox(self, equinox: float):
        """Sets the equinox of this Target.


        :param equinox: The equinox of this Target.
        :type equinox: float
        """
        if equinox is None:
            raise ValueError("Invalid value for `equinox`, must not be `None`")  # noqa: E501

        self._equinox = equinox

    @property
    def pa(self) -> float:
        """Gets the pa of this Target.


        :return: The pa of this Target.
        :rtype: float
        """
        return self._pa

    @pa.setter
    def pa(self, pa: float):
        """Sets the pa of this Target.


        :param pa: The pa of this Target.
        :type pa: float
        """
        if pa is None:
            raise ValueError("Invalid value for `pa`, must not be `None`")  # noqa: E501

        self._pa = pa

    @property
    def frame(self) -> str:
        """Gets the frame of this Target.


        :return: The frame of this Target.
        :rtype: str
        """
        return self._frame

    @frame.setter
    def frame(self, frame: str):
        """Sets the frame of this Target.


        :param frame: The frame of this Target.
        :type frame: str
        """
        if frame is None:
            raise ValueError("Invalid value for `frame`, must not be `None`")  # noqa: E501

        self._frame = frame

    @property
    def ra_offset(self) -> float:
        """Gets the ra_offset of this Target.


        :return: The ra_offset of this Target.
        :rtype: float
        """
        return self._ra_offset

    @ra_offset.setter
    def ra_offset(self, ra_offset: float):
        """Sets the ra_offset of this Target.


        :param ra_offset: The ra_offset of this Target.
        :type ra_offset: float
        """
        if ra_offset is None:
            raise ValueError("Invalid value for `ra_offset`, must not be `None`")  # noqa: E501

        self._ra_offset = ra_offset

    @property
    def dec_offset(self) -> float:
        """Gets the dec_offset of this Target.


        :return: The dec_offset of this Target.
        :rtype: float
        """
        return self._dec_offset

    @dec_offset.setter
    def dec_offset(self, dec_offset: float):
        """Sets the dec_offset of this Target.


        :param dec_offset: The dec_offset of this Target.
        :type dec_offset: float
        """
        if dec_offset is None:
            raise ValueError("Invalid value for `dec_offset`, must not be `None`")  # noqa: E501

        self._dec_offset = dec_offset

    @property
    def pm_ra(self) -> float:
        """Gets the pm_ra of this Target.


        :return: The pm_ra of this Target.
        :rtype: float
        """
        return self._pm_ra

    @pm_ra.setter
    def pm_ra(self, pm_ra: float):
        """Sets the pm_ra of this Target.


        :param pm_ra: The pm_ra of this Target.
        :type pm_ra: float
        """
        if pm_ra is None:
            raise ValueError("Invalid value for `pm_ra`, must not be `None`")  # noqa: E501

        self._pm_ra = pm_ra

    @property
    def pm_dec(self) -> float:
        """Gets the pm_dec of this Target.


        :return: The pm_dec of this Target.
        :rtype: float
        """
        return self._pm_dec

    @pm_dec.setter
    def pm_dec(self, pm_dec: float):
        """Sets the pm_dec of this Target.


        :param pm_dec: The pm_dec of this Target.
        :type pm_dec: float
        """
        if pm_dec is None:
            raise ValueError("Invalid value for `pm_dec`, must not be `None`")  # noqa: E501

        self._pm_dec = pm_dec

    @property
    def epoch(self) -> float:
        """Gets the epoch of this Target.


        :return: The epoch of this Target.
        :rtype: float
        """
        return self._epoch

    @epoch.setter
    def epoch(self, epoch: float):
        """Sets the epoch of this Target.


        :param epoch: The epoch of this Target.
        :type epoch: float
        """
        if epoch is None:
            raise ValueError("Invalid value for `epoch`, must not be `None`")  # noqa: E501

        self._epoch = epoch

    @property
    def obstime(self) -> float:
        """Gets the obstime of this Target.


        :return: The obstime of this Target.
        :rtype: float
        """
        return self._obstime

    @obstime.setter
    def obstime(self, obstime: float):
        """Sets the obstime of this Target.


        :param obstime: The obstime of this Target.
        :type obstime: float
        """
        if obstime is None:
            raise ValueError("Invalid value for `obstime`, must not be `None`")  # noqa: E501

        self._obstime = obstime

    @property
    def mag(self) -> List[Magnitude]:
        """Gets the mag of this Target.


        :return: The mag of this Target.
        :rtype: List[Magnitude]
        """
        return self._mag

    @mag.setter
    def mag(self, mag: List[Magnitude]):
        """Sets the mag of this Target.


        :param mag: The mag of this Target.
        :type mag: List[Magnitude]
        """
        if mag is None:
            raise ValueError("Invalid value for `mag`, must not be `None`")  # noqa: E501

        self._mag = mag

    @property
    def wrap(self) -> str:
        """Gets the wrap of this Target.


        :return: The wrap of this Target.
        :rtype: str
        """
        return self._wrap

    @wrap.setter
    def wrap(self, wrap: str):
        """Sets the wrap of this Target.


        :param wrap: The wrap of this Target.
        :type wrap: str
        """

        self._wrap = wrap

    @property
    def d_ra(self) -> float:
        """Gets the d_ra of this Target.


        :return: The d_ra of this Target.
        :rtype: float
        """
        return self._d_ra

    @d_ra.setter
    def d_ra(self, d_ra: float):
        """Sets the d_ra of this Target.


        :param d_ra: The d_ra of this Target.
        :type d_ra: float
        """
        if d_ra is None:
            raise ValueError("Invalid value for `d_ra`, must not be `None`")  # noqa: E501

        self._d_ra = d_ra

    @property
    def d_dec(self) -> float:
        """Gets the d_dec of this Target.


        :return: The d_dec of this Target.
        :rtype: float
        """
        return self._d_dec

    @d_dec.setter
    def d_dec(self, d_dec: float):
        """Sets the d_dec of this Target.


        :param d_dec: The d_dec of this Target.
        :type d_dec: float
        """
        if d_dec is None:
            raise ValueError("Invalid value for `d_dec`, must not be `None`")  # noqa: E501

        self._d_dec = d_dec

    @property
    def comment(self) -> str:
        """Gets the comment of this Target.


        :return: The comment of this Target.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment: str):
        """Sets the comment of this Target.


        :param comment: The comment of this Target.
        :type comment: str
        """

        self._comment = comment
