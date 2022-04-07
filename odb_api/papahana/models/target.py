# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana.models.target_metadata import TargetMetadata  # noqa: F401,E501
from papahana.models.target_parameters import TargetParameters  # noqa: F401,E501
from papahana import util


class Target(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, metadata: TargetMetadata=None, parameters: TargetParameters=None):  # noqa: E501
        """Target - a model defined in Swagger

        :param metadata: The metadata of this Target.  # noqa: E501
        :type metadata: TargetMetadata
        :param parameters: The parameters of this Target.  # noqa: E501
        :type parameters: TargetParameters
        """
        self.swagger_types = {
            'metadata': TargetMetadata,
            'parameters': TargetParameters
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'parameters': 'parameters'
        }
        self._metadata = metadata
        self._parameters = parameters

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
    def metadata(self) -> TargetMetadata:
        """Gets the metadata of this Target.


        :return: The metadata of this Target.
        :rtype: TargetMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: TargetMetadata):
        """Sets the metadata of this Target.


        :param metadata: The metadata of this Target.
        :type metadata: TargetMetadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def parameters(self) -> TargetParameters:
        """Gets the parameters of this Target.


        :return: The parameters of this Target.
        :rtype: TargetParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: TargetParameters):
        """Sets the parameters of this Target.


        :param parameters: The parameters of this Target.
        :type parameters: TargetParameters
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters
