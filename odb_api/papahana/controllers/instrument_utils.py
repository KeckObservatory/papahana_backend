from papahana.controllers import controller_helper as utils


def get_ip(instrument, ip_version=None):
    """
    Retrieve then instrument package for an instrument,  the version is optional
    and will default to the highest version number.
    """

    if not ip_version:
        query = {'metadata.instrument': instrument}
        ip_version = most_recent_version(query, 'ipCollect')

    # get the instrument package,  with references to templates (name, version)
    query = {"metadata.instrument": instrument, "metadata.version": ip_version}
    package_list = utils.get_by_query(query, 'ipCollect')

    if package_list:
        return package_list[0]
    else:
        return None


def get_ip_template(template_name, template_ver=None):
    """
    Get the template by name and optionally template_version
    """
    if not template_ver:
        query = {"metadata.name": template_name}
        template_ver = most_recent_version(query, 'templateCollect')

    query = {"metadata.name": template_name, "metadata.version": template_ver}
    templates = utils.get_by_query(query, 'templateCollect')

    if not templates:
        return {}

    return utils.json_with_objectid(templates[0])


def get_template_field(field, template_name, template_ver=None):
    """
    Get the information for a field from the template collection by name
    """
    if not template_ver:
        query = {'metadata.name': template_name}
        template_ver = most_recent_version(query, 'templateCollect')

    query = {"metadata.name": template_name, 'metadata.version': template_ver}
    fields = {field: 1, "_id": 0}

    info = utils.get_fields_by_query(query, fields, 'templateCollect')

    if not info:
        return {}

    return utils.json_with_objectid(info[0])


def get_template_metadata(template_name, template_ver=None):
    """
    get the metadata of the template by name
    """
    return get_template_field('metadata', template_name, template_ver)


def get_ip_scripts(template_name, template_ver=None):
    """
    get the script from the template by template_name
    """
    return get_template_field('metadata.script', template_name, template_ver)


def get_template_info(instrument, ip_version, template_name, func):
    """
    Get the template information
    """
    ip = get_ip(instrument, ip_version)

    if not ip:
        return {}

    info = {}
    for tmp_name, tmp_ver in ip["template_list"].items():
        if not template_name:
            info[tmp_name] = func(tmp_name, tmp_ver)
        elif tmp_name == template_name:
            return {template_name: func(tmp_name, tmp_ver)}

    return info


def most_recent_version(query, collection):
    """
    Find the highest version of the collection and query.
    """
    fields = {'metadata.version': 1}
    results = utils.get_fields_by_query(query, fields, collection)
    version = '0.0.0'
    for result in results:
        new_version = result['metadata']['version']
        if new_version > version:
            version = new_version

    return version


def get_by_script_name(script_name, script_version=None):
    """
    Retrieve the script by name.
    """
    query = {'metadata.name': script_name}
    if not script_version:
        script_version = most_recent_version(query, 'scriptCollect')

    query = {'metadata.name': script_name, 'metadata.version': script_version}
    scripts = utils.get_by_query(query, 'scriptCollect')

    if scripts:
        return utils.list_with_objectid(scripts)[0]
    else:
        return {}

