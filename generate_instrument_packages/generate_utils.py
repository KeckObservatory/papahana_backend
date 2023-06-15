def parse_templates_metadata(template_list):
    schema = {}
    for template in template_list:
        schema[template["metadata"]["name"]] = template["metadata"] 

    return schema