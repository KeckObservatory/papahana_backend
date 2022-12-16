
from papahana.controllers import controller_helper as utils
from papahana.controllers import instrument_utils as inst_utils


def instrument_packages(instrument, ip_version=None):
    """
    Retrieves the available instrument packages for an instrument. The
    version is optional,  defaults to most recent version.
        /instrumentPackages/{instrument}

    :param instrument: instrument used to make observation
    :type instrument: str

    :rtype: InstrumentPackage
    """
    package = inst_utils.get_ip(instrument.upper(), ip_version)

    return utils.json_with_objectid(package)


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
    ip = instrument_packages(instrument, ip_version)
    if not ip or 'configurable_elements' not in ip:
        return {}

    return ip['configurable_elements']


def instrument_packages_template(instrument, ip_version=None,
                                 template_name=None, parameter_order=None):
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
                                        template_name, parameter_order, func)


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
                                        template_name, None, func)


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
    if script_name:
        return inst_utils.get_by_script_name(script_name)

    temp_meta_list = instrument_packages_template_metadata(instrument, ip_version)

    script_list = []
    for meta in temp_meta_list.values():
        if 'script' in meta['metadata']:
            script_list.append(meta['metadata']['script'])

    script_names = list(set(script_list))

    script_list = []
    for script_name in script_names:
        script = inst_utils.get_by_script_name(script_name)
        if script:
            script_list.append(script)

    return script_list



