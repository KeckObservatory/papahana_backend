# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana.models.acquisition_parameters import AcquisitionParameters  # noqa: F401,E501
from papahana.models.observation_metadata import ObservationMetadata  # noqa: F401,E501
from papahana import util


class Acquisition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, metadata: ObservationMetadata=None, parameters: AcquisitionParameters=None):  # noqa: E501
        """Acquisition - a model defined in Swagger

        :param metadata: The metadata of this Acquisition.  # noqa: E501
        :type metadata: ObservationMetadata
        :param parameters: The parameters of this Acquisition.  # noqa: E501
        :type parameters: AcquisitionParameters
        """
        self.swagger_types = {
            'metadata': ObservationMetadata,
            'parameters': AcquisitionParameters
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'parameters': 'parameters'
        }
        self._metadata = metadata
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt) -> 'Acquisition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Acquisition of this Acquisition.  # noqa: E501
        :rtype: Acquisition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> ObservationMetadata:
        """Gets the metadata of this Acquisition.


        :return: The metadata of this Acquisition.
        :rtype: ObservationMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: ObservationMetadata):
        """Sets the metadata of this Acquisition.


        :param metadata: The metadata of this Acquisition.
        :type metadata: ObservationMetadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def parameters(self) -> AcquisitionParameters:
        """Gets the parameters of this Acquisition.


        :return: The parameters of this Acquisition.
        :rtype: AcquisitionParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: AcquisitionParameters):
        """Sets the parameters of this Acquisition.


        :param parameters: The parameters of this Acquisition.
        :type parameters: AcquisitionParameters
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters