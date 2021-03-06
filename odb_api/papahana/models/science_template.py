# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana.models.observation_metadata import ObservationMetadata  # noqa: F401,E501
from papahana.models.science_parameters import ScienceParameters  # noqa: F401,E501
from papahana import util


class ScienceTemplate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, metadata: ObservationMetadata=None, parameters: ScienceParameters=None):  # noqa: E501
        """ScienceTemplate - a model defined in Swagger

        :param metadata: The metadata of this ScienceTemplate.  # noqa: E501
        :type metadata: ObservationMetadata
        :param parameters: The parameters of this ScienceTemplate.  # noqa: E501
        :type parameters: ScienceParameters
        """
        self.swagger_types = {
            'metadata': ObservationMetadata,
            'parameters': ScienceParameters
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'parameters': 'parameters'
        }
        self._metadata = metadata
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt) -> 'ScienceTemplate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScienceTemplate of this ScienceTemplate.  # noqa: E501
        :rtype: ScienceTemplate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> ObservationMetadata:
        """Gets the metadata of this ScienceTemplate.


        :return: The metadata of this ScienceTemplate.
        :rtype: ObservationMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: ObservationMetadata):
        """Sets the metadata of this ScienceTemplate.


        :param metadata: The metadata of this ScienceTemplate.
        :type metadata: ObservationMetadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def parameters(self) -> ScienceParameters:
        """Gets the parameters of this ScienceTemplate.


        :return: The parameters of this ScienceTemplate.
        :rtype: ScienceParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: ScienceParameters):
        """Sets the parameters of this ScienceTemplate.


        :param parameters: The parameters of this ScienceTemplate.
        :type parameters: ScienceParameters
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters
