import generate_random_utils as random_utils


def generate_scripts_collection(coll, inst):
    query = {'$and': [{'metadata.instrument': 'KPF'},
                      {'$or': [{'metadata.template_type': 'science'},
                               {'metadata.template_type': 'acquisition'},
                               {'metadata.template_type': 'calibration'}
                               ]}
                      ]
             }
    fields = {'_id': 0, 'metadata.script_version': 1, 'metadata.script': 1,
              'metadata.template_type': 1}

    results = list(coll.find(query, fields))

    for result in results:
        script_version = result["metadata"]["script_version"]
        script_name = result["metadata"]["script"]
        script_type = result["metadata"]["template_type"]
        schema = generate_scripts(inst, script_name, script_type, script_version)
        _ = coll.insert_one(schema)


def generate_scripts(inst, script_name, script_type, version):
    schema = {
        'metadata': {
            'name': script_name,
            'version': version,
            'instrument': inst,
            'script_type': script_type,
            'comment': random_utils.optionalRandComment()
        },
        'script': {'TBD': 'TBD'}
    }

    return schema

