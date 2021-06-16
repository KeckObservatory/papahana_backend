# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana.models.sem_id_schema import SemIdSchema  # noqa: F401,E501
from papahana import util


class Container(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, sem_id: SemIdSchema=None, observation_blocks: List[str]=None, comment: str=None):  # noqa: E501
        """Container - a model defined in Swagger

        :param name: The name of this Container.  # noqa: E501
        :type name: str
        :param sem_id: The sem_id of this Container.  # noqa: E501
        :type sem_id: SemIdSchema
        :param observation_blocks: The observation_blocks of this Container.  # noqa: E501
        :type observation_blocks: List[str]
        :param comment: The comment of this Container.  # noqa: E501
        :type comment: str
        """
        self.swagger_types = {
            'name': str,
            'sem_id': SemIdSchema,
            'observation_blocks': List[str],
            'comment': str
        }

        self.attribute_map = {
            'name': 'name',
            'sem_id': 'sem_id',
            'observation_blocks': 'observation_blocks',
            'comment': 'comment'
        }
        self._name = name
        self._sem_id = sem_id
        self._observation_blocks = observation_blocks
        self._comment = comment

    @classmethod
    def from_dict(cls, dikt) -> 'Container':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Container of this Container.  # noqa: E501
        :rtype: Container
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Container.


        :return: The name of this Container.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Container.


        :param name: The name of this Container.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def sem_id(self) -> SemIdSchema:
        """Gets the sem_id of this Container.


        :return: The sem_id of this Container.
        :rtype: SemIdSchema
        """
        return self._sem_id

    @sem_id.setter
    def sem_id(self, sem_id: SemIdSchema):
        """Sets the sem_id of this Container.


        :param sem_id: The sem_id of this Container.
        :type sem_id: SemIdSchema
        """
        if sem_id is None:
            raise ValueError("Invalid value for `sem_id`, must not be `None`")  # noqa: E501

        self._sem_id = sem_id

    @property
    def observation_blocks(self) -> List[str]:
        """Gets the observation_blocks of this Container.


        :return: The observation_blocks of this Container.
        :rtype: List[str]
        """
        return self._observation_blocks

    @observation_blocks.setter
    def observation_blocks(self, observation_blocks: List[str]):
        """Sets the observation_blocks of this Container.


        :param observation_blocks: The observation_blocks of this Container.
        :type observation_blocks: List[str]
        """
        if observation_blocks is None:
            raise ValueError("Invalid value for `observation_blocks`, must not be `None`")  # noqa: E501

        self._observation_blocks = observation_blocks

    @property
    def comment(self) -> str:
        """Gets the comment of this Container.


        :return: The comment of this Container.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment: str):
        """Sets the comment of this Container.


        :param comment: The comment of this Container.
        :type comment: str
        """

        self._comment = comment
