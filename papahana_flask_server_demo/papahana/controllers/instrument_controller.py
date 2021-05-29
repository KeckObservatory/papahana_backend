import connexion
import six

from papahana.models.instrument_package import InstrumentPackage
from papahana import util


def instrument_packages(instrument):  # noqa: E501
    """
    Retrieves the list of available instrument packages for an instrument

    :param instrument: instrument used to make observation
    :type instrument: str

    :rtype: List[InstrumentPackage]
    """
    return 'do some magic!'


def instrument_packages_ip_signature(instrument, ip_version):  # noqa: E501
    """
    List all template signatures that can be attached to OBs using this instrument package

    :param instrument: instrument used to make observation
    :type instrument: str
    :param ip_version: ip version description here
    :type ip_version: int

    :rtype: InstrumentPackage
    """
    return 'do some magic!'


def instrument_packages_ip_template(instrument, ip_version, template_name):
    """
    Retrieves the specified instrument package template signature # noqa: E501

    :param instrument: instrument used to make observation
    :type instrument: str
    :param ip_version: ip version description here
    :type ip_version: int
    :param template_name: template name description goes here
    :type template_name: str

    :rtype: InstrumentPackage
    """
    return 'do some magic!'
