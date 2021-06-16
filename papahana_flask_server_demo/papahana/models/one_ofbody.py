# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana import util


class OneOfbody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """OneOfbody - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'OneOfbody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OneOfbody of this OneOfbody.  # noqa: E501
        :rtype: OneOfbody
        """
        return util.deserialize_model(dikt, cls)
