import connexion
import six

from papahana.models.instrument_enum import InstrumentEnum
from papahana.models.instrument_package import InstrumentPackage
from papahana import util

from papahana.controllers import controller_helper as utils
from papahana.controllers import instrument_controller_utils as inst_utils


def instrument_packages(instrument):
    """instrument_packages

    Retrieves the the available instrument packages for an instrument.

    :param instrument: instrument used to make observation
    :type instrument: str

    :rtype: [InstrumentPackage]
    """
    if connexion.request.is_json:
        instrument = InstrumentEnum.from_dict(connexion.request.get_json())

    query = {"metadata.instrument": instrument}

    ip_packages = utils.get_by_query(query, 'ipCollect')

    return utils.list_with_objectid(ip_packages)


def instrument_packages_parameter(instrument, ip_version=None):
    """
    /instrumentPackages/{instrument}/parameters

    List all template parameters that can be attached to OBs using this
    instrument package

    :param instrument: instrument used to make observation
    :type instrument: str
    :param ip_version: ip version description here
    :type ip_version: str

    :rtype: InstrumentPackage
    """
    if connexion.request.is_json:
        instrument = InstrumentEnum.from_dict(connexion.request.get_json())

    if not ip_version:
        query = {'metadata.instrument': instrument}
        ip_version = utils.most_recent_version(query, 'ipCollect')

    query = {"metadata.instrument": instrument, "metadata.version": ip_version}
    fields = {"_id": 0, "configurable_elements": 1}

    package_list = utils.get_fields_by_query(query, fields, 'ipCollect')

    if package_list:
        return package_list[0]
    else:
        return {}


def instrument_packages_template(instrument, ip_version=None, template_name=None):
    """
    Retrieves the specified instrument package template metadata
    /instrumentPackages/{instrument}/templates

    :param instrument: instrument used to make observation
    :type instrument: str
    :param ip_version: ip version description here
    :type ip_version: str
    :param template_name: template name description goes here
    :type template_name: str

    :rtype: InstrumentPackage
    """
    func = inst_utils.get_ip_template
    return inst_utils.get_template_info(instrument, ip_version,
                                        template_name, func)


def instrument_packages_template_metadata(instrument, ip_version=None,
                                          template_name=None):
    """
    Retrieves the specified instrument package template metadata

    /instrumentPackages/{instrument}/templates/metadata

    :param instrument: instrument used to make observation
    :type instrument: str
    :param ip_version: ip ip_version description here
    :type ip_version: str
    :param template_name: template name description goes here
    :type template_name: str

    :rtype: InstrumentPackage
    """
    func = inst_utils.get_template_metadata
    return inst_utils.get_template_info(instrument, ip_version,
                                        template_name, func)


def instrument_packages_scripts(instrument, ip_version=None, script_name=None):
    """
    /instrumentPackages/{instrument}/scripts

    Retrieves all the scripts associated with the instrument package. The
    ip_version is optional,  the default to most recent ip_version.

    :param instrument: instrument used to make observation
    :type instrument: dict | bytes
    :param ip_version: ip version description here
    :type ip_version: str
    :param script_name: the name of the script to retrieve
    :type script_name: str

    :rtype: InstrumentPackage
    """
    if connexion.request.is_json:
        instrument = InstrumentEnum.from_dict(connexion.request.get_json())

    metadata = instrument_packages_template_metadata(instrument,
                                                     ip_version=ip_version)

    if script_name:
        return inst_utils.get_by_script_name(script_name)

    scripts = []
    for meta in metadata:
        try:
            script_name = metadata[meta]['metadata']['script']
            script_ver = metadata[meta]['metadata']['script_version']
            scripts.append(inst_utils.get_by_script_name(script_name,
                                                         script_ver))
        except KeyError:
            pass

    return scripts



