def parse_templates_version(template_list):
    schema = {}
    for template in template_list:
        version = template["metadata"]["version"]
        schema[template["metadata"]["name"]] = version

    return schema