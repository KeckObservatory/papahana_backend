import connexion
import six

from papahana.models.instrument_package import InstrumentPackage
from papahana import util
from papahana.controllers import controller_helper as utils


def instrument_packages(instrument):
    """instrument_packages

    Retrieves the the available instrument packages for an instrument.

    :param instrument: instrument used to make observation
    :type instrument: str

    :rtype: InstrumentPackage
    """
    return 'do some magic!'


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
    query = {"instrument": instrument, "version": ip_version}
    results = utils.get_by_query(query, 'templateCollect')

    return results


def instrument_packages_ip_template(instrument, ip_version, template_name):
    """
    Retrieves the specified instrument package template signature

    :param instrument: instrument used to make observation
    :type instrument: str
    :param ip_version: ip version description here
    :type ip_version: float
    :param template_name: template name description goes here
    :type template_name: str

    :rtype: InstrumentPackage
    """
    #TODO -- why does need instrument?  template_name is "KCWI_ifu_sci_stare"?
    # should it default to all templates and have name optional?
    query = {"name": template_name, "version": ip_version}
    packages = utils.get_by_query(query, 'templateCollect')

    return packages
