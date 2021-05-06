# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Group(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, semester: str=None, group_id: str=None, observation_blocks: List[str]=None, comment: str=None):  # noqa: E501
        """Group - a model defined in Swagger

        :param id: The id of this Group.  # noqa: E501
        :type id: str
        :param name: The name of this Group.  # noqa: E501
        :type name: str
        :param semester: The semester of this Group.  # noqa: E501
        :type semester: str
        :param group_id: The group_id of this Group.  # noqa: E501
        :type group_id: str
        :param observation_blocks: The observation_blocks of this Group.  # noqa: E501
        :type observation_blocks: List[str]
        :param comment: The comment of this Group.  # noqa: E501
        :type comment: str
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'semester': str,
            'group_id': str,
            'observation_blocks': List[str],
            'comment': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'semester': 'semester',
            'group_id': 'group_id',
            'observation_blocks': 'observation_blocks',
            'comment': 'comment'
        }
        self._id = id
        self._name = name
        self._semester = semester
        self._group_id = group_id
        self._observation_blocks = observation_blocks
        self._comment = comment

    @classmethod
    def from_dict(cls, dikt) -> 'Group':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Group of this Group.  # noqa: E501
        :rtype: Group
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Group.


        :return: The id of this Group.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Group.


        :param id: The id of this Group.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Group.


        :return: The name of this Group.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Group.


        :param name: The name of this Group.
        :type name: str
        """

        self._name = name

    @property
    def semester(self) -> str:
        """Gets the semester of this Group.


        :return: The semester of this Group.
        :rtype: str
        """
        return self._semester

    @semester.setter
    def semester(self, semester: str):
        """Sets the semester of this Group.


        :param semester: The semester of this Group.
        :type semester: str
        """

        self._semester = semester

    @property
    def group_id(self) -> str:
        """Gets the group_id of this Group.


        :return: The group_id of this Group.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id: str):
        """Sets the group_id of this Group.


        :param group_id: The group_id of this Group.
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def observation_blocks(self) -> List[str]:
        """Gets the observation_blocks of this Group.


        :return: The observation_blocks of this Group.
        :rtype: List[str]
        """
        return self._observation_blocks

    @observation_blocks.setter
    def observation_blocks(self, observation_blocks: List[str]):
        """Sets the observation_blocks of this Group.


        :param observation_blocks: The observation_blocks of this Group.
        :type observation_blocks: List[str]
        """

        self._observation_blocks = observation_blocks

    @property
    def comment(self) -> str:
        """Gets the comment of this Group.


        :return: The comment of this Group.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment: str):
        """Sets the comment of this Group.


        :param comment: The comment of this Group.
        :type comment: str
        """

        self._comment = comment
