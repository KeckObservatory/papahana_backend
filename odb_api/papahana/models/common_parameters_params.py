# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana import util


class CommonParametersParams(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, instrument_parameters: str=None, detector_parameters: str=None, tcs_config: str=None):  # noqa: E501
        """CommonParametersParams - a model defined in Swagger

        :param instrument_parameters: The instrument_parameters of this CommonParametersParams.  # noqa: E501
        :type instrument_parameters: str
        :param detector_parameters: The detector_parameters of this CommonParametersParams.  # noqa: E501
        :type detector_parameters: str
        :param tcs_config: The tcs_config of this CommonParametersParams.  # noqa: E501
        :type tcs_config: str
        """
        self.swagger_types = {
            'instrument_parameters': str,
            'detector_parameters': str,
            'tcs_config': str
        }

        self.attribute_map = {
            'instrument_parameters': 'instrument_parameters',
            'detector_parameters': 'detector_parameters',
            'tcs_config': 'tcs_config'
        }
        self._instrument_parameters = instrument_parameters
        self._detector_parameters = detector_parameters
        self._tcs_config = tcs_config

    @classmethod
    def from_dict(cls, dikt) -> 'CommonParametersParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CommonParametersParams of this CommonParametersParams.  # noqa: E501
        :rtype: CommonParametersParams
        """
        return util.deserialize_model(dikt, cls)

    @property
    def instrument_parameters(self) -> str:
        """Gets the instrument_parameters of this CommonParametersParams.


        :return: The instrument_parameters of this CommonParametersParams.
        :rtype: str
        """
        return self._instrument_parameters

    @instrument_parameters.setter
    def instrument_parameters(self, instrument_parameters: str):
        """Sets the instrument_parameters of this CommonParametersParams.


        :param instrument_parameters: The instrument_parameters of this CommonParametersParams.
        :type instrument_parameters: str
        """
        if instrument_parameters is None:
            raise ValueError("Invalid value for `instrument_parameters`, must not be `None`")  # noqa: E501

        self._instrument_parameters = instrument_parameters

    @property
    def detector_parameters(self) -> str:
        """Gets the detector_parameters of this CommonParametersParams.


        :return: The detector_parameters of this CommonParametersParams.
        :rtype: str
        """
        return self._detector_parameters

    @detector_parameters.setter
    def detector_parameters(self, detector_parameters: str):
        """Sets the detector_parameters of this CommonParametersParams.


        :param detector_parameters: The detector_parameters of this CommonParametersParams.
        :type detector_parameters: str
        """
        if detector_parameters is None:
            raise ValueError("Invalid value for `detector_parameters`, must not be `None`")  # noqa: E501

        self._detector_parameters = detector_parameters

    @property
    def tcs_config(self) -> str:
        """Gets the tcs_config of this CommonParametersParams.


        :return: The tcs_config of this CommonParametersParams.
        :rtype: str
        """
        return self._tcs_config

    @tcs_config.setter
    def tcs_config(self, tcs_config: str):
        """Sets the tcs_config of this CommonParametersParams.


        :param tcs_config: The tcs_config of this CommonParametersParams.
        :type tcs_config: str
        """
        if tcs_config is None:
            raise ValueError("Invalid value for `tcs_config`, must not be `None`")  # noqa: E501

        self._tcs_config = tcs_config
