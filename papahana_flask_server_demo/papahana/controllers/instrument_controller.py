import connexion
import six

from papahana.models.instrument_enum import InstrumentEnum
from papahana.models.instrument_package import InstrumentPackage
from papahana import util

from papahana.controllers import controller_helper as utils


def instrument_packages(instrument):
    """instrument_packages

    Retrieves the the available instrument packages for an instrument.

    :param instrument: instrument used to make observation
    :type instrument: str

    :rtype: [InstrumentPackage]
    """
    if connexion.request.is_json:
        instrument = InstrumentEnum.from_dict(connexion.request.get_json())

    query = {'instrument': instrument}

    return utils.get_by_query(query, 'templateCollect')


def instrument_packages_ip_parameter(instrument, ip_version):
    """
    List all template parameters that can be attached to OBs using this
    instrument package

    :param instrument: instrument used to make observation
    :type instrument: str
    :param ip_version: ip version description here
    :type ip_version: float

    :rtype: InstrumentPackage
    """
    if connexion.request.is_json:
        instrument = InstrumentEnum.from_dict(connexion.request.get_json())

    query = {"instrument": instrument, "version": ip_version}
    fields ={"_id": 0, "optical_parameters": 1, "guider": 1,
             "common_inst_params": 1, "pointing_origins": 1}

    return utils.get_fields_by_query(query, fields, 'ipCollect')


def instrument_packages_ip_template(instrument, ip_version, template_name=None):
    """
    Retrieves the specified instrument package template metadata

    :param instrument: instrument used to make observation
    :type instrument: str
    :param ip_version: ip version description here
    :type ip_version: float
    :param template_name: template name description goes here
    :type template_name: str

    :rtype: InstrumentPackage
    """
    # if connexion.request.is_json:
    #     instrument = InstrumentEnum.from_dict(connexion.request.get_json())

    if template_name:
        return {template_name: get_template_metadata(template_name, ip_version)}

    query = {"instrument": instrument.upper(), "version": ip_version}
    fields = {"template_names": 1, "_id": 0}
    templates = utils.get_fields_by_query(query, fields, 'ipCollect')

    metadata = {}
    for template_name in templates["template_names"]:
        metadata[template_name] = get_template_metadata(template_name, ip_version)

    return metadata


def get_template_metadata(template_name, ip_version):
    query = {"metadata.name": template_name, "version": ip_version}
    fields = {"metadata": 1, "_id": 0}

    return utils.get_fields_by_query(query, fields, 'templateCollect')