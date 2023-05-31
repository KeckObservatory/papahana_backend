import importlib

def generate_scripts_collection(coll, coll_inst, coll_tmp, inst):

    query = {'metadata.instrument': inst.upper()}
    fields = {'_id': 0, 'template_list': 1}

    results = list(coll_inst.find(query, fields))[0]

    for tmp_name, tmp_ver in results['template_list'].items():
        query = {'metadata.instrument': inst.upper(),
                 'metadata.name': tmp_name,
                 'metadata.version': tmp_ver}

        fields = {'_id': 0, 'metadata': 1}
        results = list(coll_tmp.find(query, fields))
        if not results:
            continue

        results = results[0]
        if not results or 'metadata' not in results:
            continue

        meta = results['metadata']
        print(f'meta {meta}')
        if 'version' not in meta or 'template_type' not in meta \
                or 'script' not in meta:
            print('skipping')
            continue

        script_name = results['metadata']['script']
        version = results['metadata']['version']
        script_type = results['metadata']['template_type']

        schema = generate_scripts(inst, script_name, script_type, version)
        _ = coll.insert_one(schema)

    return coll


def generate_scripts(inst, script_name, script_type, version):
    print('gen', inst, script_name, script_type, version)
    scriptModule = importlib.import_module(f'{inst.lower()}_scripts')
    scripts = scriptModule.generate_scripts()
    if script_name in scripts:
        script = scripts[script_name]
    else:
        script = {'TBD': 'TBD'}

    print('scr', script)
    print('scr', type(script))
    print('-'*8)

    ui_name = script_name.replace('_', ' ').title()
    schema = {
        'metadata': {
            'name': script_name,
            'ui_name': ui_name,
            'version': version,
            'instrument': inst,
            'script_type': script_type,
            'comment': f'Script for template: {script_name}, {version}'
        },
        'script': script
    }

    return schema