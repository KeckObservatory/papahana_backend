# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GroupSummary(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, group_id: str=None, semester: str=None, observation_blocks: List[str]=None, comment: str=None):  # noqa: E501
        """GroupSummary - a model defined in Swagger

        :param id: The id of this GroupSummary.  # noqa: E501
        :type id: str
        :param name: The name of this GroupSummary.  # noqa: E501
        :type name: str
        :param group_id: The group_id of this GroupSummary.  # noqa: E501
        :type group_id: str
        :param semester: The semester of this GroupSummary.  # noqa: E501
        :type semester: str
        :param observation_blocks: The observation_blocks of this GroupSummary.  # noqa: E501
        :type observation_blocks: List[str]
        :param comment: The comment of this GroupSummary.  # noqa: E501
        :type comment: str
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'group_id': str,
            'semester': str,
            'observation_blocks': List[str],
            'comment': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'group_id': 'group_id',
            'semester': 'semester',
            'observation_blocks': 'observation_blocks',
            'comment': 'comment'
        }
        self._id = id
        self._name = name
        self._group_id = group_id
        self._semester = semester
        self._observation_blocks = observation_blocks
        self._comment = comment

    @classmethod
    def from_dict(cls, dikt) -> 'GroupSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GroupSummary of this GroupSummary.  # noqa: E501
        :rtype: GroupSummary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this GroupSummary.


        :return: The id of this GroupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this GroupSummary.


        :param id: The id of this GroupSummary.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this GroupSummary.


        :return: The name of this GroupSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this GroupSummary.


        :param name: The name of this GroupSummary.
        :type name: str
        """

        self._name = name

    @property
    def group_id(self) -> str:
        """Gets the group_id of this GroupSummary.


        :return: The group_id of this GroupSummary.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id: str):
        """Sets the group_id of this GroupSummary.


        :param group_id: The group_id of this GroupSummary.
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def semester(self) -> str:
        """Gets the semester of this GroupSummary.


        :return: The semester of this GroupSummary.
        :rtype: str
        """
        return self._semester

    @semester.setter
    def semester(self, semester: str):
        """Sets the semester of this GroupSummary.


        :param semester: The semester of this GroupSummary.
        :type semester: str
        """

        self._semester = semester

    @property
    def observation_blocks(self) -> List[str]:
        """Gets the observation_blocks of this GroupSummary.


        :return: The observation_blocks of this GroupSummary.
        :rtype: List[str]
        """
        return self._observation_blocks

    @observation_blocks.setter
    def observation_blocks(self, observation_blocks: List[str]):
        """Sets the observation_blocks of this GroupSummary.


        :param observation_blocks: The observation_blocks of this GroupSummary.
        :type observation_blocks: List[str]
        """

        self._observation_blocks = observation_blocks

    @property
    def comment(self) -> str:
        """Gets the comment of this GroupSummary.


        :return: The comment of this GroupSummary.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment: str):
        """Sets the comment of this GroupSummary.


        :param comment: The comment of this GroupSummary.
        :type comment: str
        """

        self._comment = comment
