# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana import util


class InstrumentPackage(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """InstrumentPackage - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'InstrumentPackage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InstrumentPackage of this InstrumentPackage.  # noqa: E501
        :rtype: InstrumentPackage
        """
        return util.deserialize_model(dikt, cls)
