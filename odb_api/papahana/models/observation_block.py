# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana.models.acquisition import Acquisition  # noqa: F401,E501
from papahana.models.common_parameters import CommonParameters  # noqa: F401,E501
from papahana.models.date_schema import DateSchema  # noqa: F401,E501
from papahana.models.obs_block_metadata import ObsBlockMetadata  # noqa: F401,E501
from papahana.models.status import Status  # noqa: F401,E501
from papahana.models.target import Target  # noqa: F401,E501
from papahana.models.template_schema import TemplateSchema  # noqa: F401,E501
from papahana import util


class ObservationBlock(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, metadata: ObsBlockMetadata=None, target: Target=None, acquisition: Acquisition=None, common_parameters: CommonParameters=None, observations: List[TemplateSchema]=None, associations: List[str]=None, status: Status=None, time_constraints: List[DateSchema]=None, comment: str=''):  # noqa: E501
        """ObservationBlock - a model defined in Swagger

        :param metadata: The metadata of this ObservationBlock.  # noqa: E501
        :type metadata: ObsBlockMetadata
        :param target: The target of this ObservationBlock.  # noqa: E501
        :type target: Target
        :param acquisition: The acquisition of this ObservationBlock.  # noqa: E501
        :type acquisition: Acquisition
        :param common_parameters: The common_parameters of this ObservationBlock.  # noqa: E501
        :type common_parameters: CommonParameters
        :param observations: The observations of this ObservationBlock.  # noqa: E501
        :type observations: List[TemplateSchema]
        :param associations: The associations of this ObservationBlock.  # noqa: E501
        :type associations: List[str]
        :param status: The status of this ObservationBlock.  # noqa: E501
        :type status: Status
        :param time_constraints: The time_constraints of this ObservationBlock.  # noqa: E501
        :type time_constraints: List[DateSchema]
        :param comment: The comment of this ObservationBlock.  # noqa: E501
        :type comment: str
        """
        self.swagger_types = {
            'metadata': ObsBlockMetadata,
            'target': Target,
            'acquisition': Acquisition,
            'common_parameters': CommonParameters,
            'observations': List[TemplateSchema],
            'associations': List[str],
            'status': Status,
            'time_constraints': List[DateSchema],
            'comment': str
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'target': 'target',
            'acquisition': 'acquisition',
            'common_parameters': 'common_parameters',
            'observations': 'observations',
            'associations': 'associations',
            'status': 'status',
            'time_constraints': 'time_constraints',
            'comment': 'comment'
        }
        self._metadata = metadata
        self._target = target
        self._acquisition = acquisition
        self._common_parameters = common_parameters
        self._observations = observations
        self._associations = associations
        self._status = status
        self._time_constraints = time_constraints
        self._comment = comment

    @classmethod
    def from_dict(cls, dikt) -> 'ObservationBlock':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ObservationBlock of this ObservationBlock.  # noqa: E501
        :rtype: ObservationBlock
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> ObsBlockMetadata:
        """Gets the metadata of this ObservationBlock.


        :return: The metadata of this ObservationBlock.
        :rtype: ObsBlockMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: ObsBlockMetadata):
        """Sets the metadata of this ObservationBlock.


        :param metadata: The metadata of this ObservationBlock.
        :type metadata: ObsBlockMetadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def target(self) -> Target:
        """Gets the target of this ObservationBlock.


        :return: The target of this ObservationBlock.
        :rtype: Target
        """
        return self._target

    @target.setter
    def target(self, target: Target):
        """Sets the target of this ObservationBlock.


        :param target: The target of this ObservationBlock.
        :type target: Target
        """

        self._target = target

    @property
    def acquisition(self) -> Acquisition:
        """Gets the acquisition of this ObservationBlock.


        :return: The acquisition of this ObservationBlock.
        :rtype: Acquisition
        """
        return self._acquisition

    @acquisition.setter
    def acquisition(self, acquisition: Acquisition):
        """Sets the acquisition of this ObservationBlock.


        :param acquisition: The acquisition of this ObservationBlock.
        :type acquisition: Acquisition
        """

        self._acquisition = acquisition

    @property
    def common_parameters(self) -> CommonParameters:
        """Gets the common_parameters of this ObservationBlock.


        :return: The common_parameters of this ObservationBlock.
        :rtype: CommonParameters
        """
        return self._common_parameters

    @common_parameters.setter
    def common_parameters(self, common_parameters: CommonParameters):
        """Sets the common_parameters of this ObservationBlock.


        :param common_parameters: The common_parameters of this ObservationBlock.
        :type common_parameters: CommonParameters
        """

        self._common_parameters = common_parameters

    @property
    def observations(self) -> List[TemplateSchema]:
        """Gets the observations of this ObservationBlock.


        :return: The observations of this ObservationBlock.
        :rtype: List[TemplateSchema]
        """
        return self._observations

    @observations.setter
    def observations(self, observations: List[TemplateSchema]):
        """Sets the observations of this ObservationBlock.


        :param observations: The observations of this ObservationBlock.
        :type observations: List[TemplateSchema]
        """

        self._observations = observations

    @property
    def associations(self) -> List[str]:
        """Gets the associations of this ObservationBlock.


        :return: The associations of this ObservationBlock.
        :rtype: List[str]
        """
        return self._associations

    @associations.setter
    def associations(self, associations: List[str]):
        """Sets the associations of this ObservationBlock.


        :param associations: The associations of this ObservationBlock.
        :type associations: List[str]
        """

        self._associations = associations

    @property
    def status(self) -> Status:
        """Gets the status of this ObservationBlock.


        :return: The status of this ObservationBlock.
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status: Status):
        """Sets the status of this ObservationBlock.


        :param status: The status of this ObservationBlock.
        :type status: Status
        """

        self._status = status

    @property
    def time_constraints(self) -> List[DateSchema]:
        """Gets the time_constraints of this ObservationBlock.


        :return: The time_constraints of this ObservationBlock.
        :rtype: List[DateSchema]
        """
        return self._time_constraints

    @time_constraints.setter
    def time_constraints(self, time_constraints: List[DateSchema]):
        """Sets the time_constraints of this ObservationBlock.


        :param time_constraints: The time_constraints of this ObservationBlock.
        :type time_constraints: List[DateSchema]
        """

        self._time_constraints = time_constraints

    @property
    def comment(self) -> str:
        """Gets the comment of this ObservationBlock.


        :return: The comment of this ObservationBlock.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment: str):
        """Sets the comment of this ObservationBlock.


        :param comment: The comment of this ObservationBlock.
        :type comment: str
        """

        self._comment = comment
