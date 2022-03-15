from papahana.controllers import controller_helper as utils


# ---------------------------------
# Instrument Package Specific Utils
# ---------------------------------
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


def get_template_metadata(template_name, template_ver=None):
    if not template_ver:
        query = {'metadata.name': template_name}
        template_ver = most_recent_version(query, 'templateCollect')

    query = {"metadata.name": template_name, 'metadata.version': template_ver}
    fields = {"metadata": 1, "_id": 0}

    metadata = utils.get_fields_by_query(query, fields, 'templateCollect')

    if not metadata:
        return {}

    return utils.json_with_objectid(metadata[0])

#
# def get_scripts(script_name, ip_version=None):
#     get_template_metadata()


def get_template_info(instrument, ip_version, template_name, func):
    if not ip_version:
        query = {'metadata.instrument': instrument}
        ip_version = most_recent_version(query, 'ipCollect')

    # get the instrument package,  with references to templates (name, version)
    query = {"metadata.instrument": instrument.upper(), "metadata.version": ip_version}
    fields = {"template_list": 1, "_id": 0}
    package_list = utils.get_fields_by_query(query, fields, 'ipCollect')

    if not package_list:
        return {}

    # only one result for a version
    template_info = package_list[0]

    info = {}
    for tmp_name, tmp_ver in template_info["template_list"].items():
        info[tmp_name] = func(tmp_name, tmp_ver)
        if template_name and tmp_name == template_name:
            return {template_name: info[tmp_name]}

    return info


def most_recent_version(query, collection):
    fields = {'metadata.version': 1}
    results = utils.get_fields_by_query(query, fields, collection)
    version = '0.0.0'
    for result in results:
        new_version = result['metadata']['version']
        if new_version > version:
            version = new_version

    return version

def get_by_script_name(script_name, script_version=None):
    query = {'metadata.name': script_name}
    if not script_version:
        script_version = most_recent_version(query, 'scriptCollect')

    query = {'metadata.name': script_name, 'metadata.version': script_version}
    scripts = utils.get_by_query(query, 'scriptCollect')
    return utils.list_with_objectid(scripts)

