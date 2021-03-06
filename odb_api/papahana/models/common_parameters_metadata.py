# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from papahana.models.base_model_ import Model
from papahana import util


class CommonParametersMetadata(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, ui_name: str=None, instrument: str=None, template_type: str=None, version: str=None):  # noqa: E501
        """CommonParametersMetadata - a model defined in Swagger

        :param name: The name of this CommonParametersMetadata.  # noqa: E501
        :type name: str
        :param ui_name: The ui_name of this CommonParametersMetadata.  # noqa: E501
        :type ui_name: str
        :param instrument: The instrument of this CommonParametersMetadata.  # noqa: E501
        :type instrument: str
        :param template_type: The template_type of this CommonParametersMetadata.  # noqa: E501
        :type template_type: str
        :param version: The version of this CommonParametersMetadata.  # noqa: E501
        :type version: str
        """
        self.swagger_types = {
            'name': str,
            'ui_name': str,
            'instrument': str,
            'template_type': str,
            'version': str
        }

        self.attribute_map = {
            'name': 'name',
            'ui_name': 'ui_name',
            'instrument': 'instrument',
            'template_type': 'template_type',
            'version': 'version'
        }
        self._name = name
        self._ui_name = ui_name
        self._instrument = instrument
        self._template_type = template_type
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'CommonParametersMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CommonParametersMetadata of this CommonParametersMetadata.  # noqa: E501
        :rtype: CommonParametersMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this CommonParametersMetadata.


        :return: The name of this CommonParametersMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this CommonParametersMetadata.


        :param name: The name of this CommonParametersMetadata.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ui_name(self) -> str:
        """Gets the ui_name of this CommonParametersMetadata.


        :return: The ui_name of this CommonParametersMetadata.
        :rtype: str
        """
        return self._ui_name

    @ui_name.setter
    def ui_name(self, ui_name: str):
        """Sets the ui_name of this CommonParametersMetadata.


        :param ui_name: The ui_name of this CommonParametersMetadata.
        :type ui_name: str
        """
        if ui_name is None:
            raise ValueError("Invalid value for `ui_name`, must not be `None`")  # noqa: E501

        self._ui_name = ui_name

    @property
    def instrument(self) -> str:
        """Gets the instrument of this CommonParametersMetadata.


        :return: The instrument of this CommonParametersMetadata.
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument: str):
        """Sets the instrument of this CommonParametersMetadata.


        :param instrument: The instrument of this CommonParametersMetadata.
        :type instrument: str
        """
        if instrument is None:
            raise ValueError("Invalid value for `instrument`, must not be `None`")  # noqa: E501

        self._instrument = instrument

    @property
    def template_type(self) -> str:
        """Gets the template_type of this CommonParametersMetadata.


        :return: The template_type of this CommonParametersMetadata.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type: str):
        """Sets the template_type of this CommonParametersMetadata.


        :param template_type: The template_type of this CommonParametersMetadata.
        :type template_type: str
        """
        if template_type is None:
            raise ValueError("Invalid value for `template_type`, must not be `None`")  # noqa: E501

        self._template_type = template_type

    @property
    def version(self) -> str:
        """Gets the version of this CommonParametersMetadata.


        :return: The version of this CommonParametersMetadata.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this CommonParametersMetadata.


        :param version: The version of this CommonParametersMetadata.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version
