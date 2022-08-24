import generate_utils as utils
import generate_observation_block as ob_utils
import generate_tags as tags_utils
import generate_containers as container_utils
from generate_scripts import generate_scripts_collection
from generate_observers import generate_observer_collection

import kcwi_filled_templates as kcwi_filled
import kpf_filled_templates as kpf_filled

import generate_template
from papahana import util as papahana_util
from os import path

CONFIG = 'config.live.ini'
APP_PATH = path.abspath(path.dirname(__file__))
INST_LIST = ['KPF', 'KCWI']

if __name__=='__main__':
    args = utils.parse_args()
    mode = args.mode
    if not args.mode:
        mode = papahana_util.read_mode()

    config = utils.read_config(mode, f"{APP_PATH}/{CONFIG}")
    ob_db = config['ob_db']

    print(f"Using DataBase: {ob_db}")
    papahana_util.drop_db(ob_db, conf=config)

    # generate templates
    print("...generating templates")
    template_list = generate_template.generate_templates(config)

    # Create ob_blocks collection
    print("...zeroing deltas")
    coll = papahana_util.config_collection('deltaCollect', conf=config)
    coll.drop()

    # Create ob_blocks collection
    print("...generating OBs")
    ob_blocks = []
    for inst in INST_LIST:
        ob_blocks += ob_utils.generate_obs(
            config, inst.lower(), INST_LIST, template_list)

    # create tags collection
    coll = papahana_util.config_collection('tagsCollect', conf=config)
    keck_id_obj_id = tags_utils.generate_tag_list(coll)

    # add tags randomly to OBs
    for ob in ob_blocks:
        tags_utils.add_tags_to_ob(config, ob, keck_id_obj_id)

    # Create containers collection
    print("...generating containers")
    coll = papahana_util.config_collection('containerCollect', conf=config)
    coll.drop()
    container_list = container_utils.generate_containers(config, coll, ob_blocks)

    # Create Instrument package
    print("...generating instrument package")
    coll = papahana_util.config_collection('ipCollect', conf=config)
    coll.drop()

    # ip = generate_inst_package(template_list)
    for inst in INST_LIST:
        inst_lower = inst.lower()
        inst_specific_templates = utils.parse_template_list(
            inst, INST_LIST, template_list, allow_mos=False)
        if inst_lower == 'kcwi':
            ip = kcwi_filled.generate_inst_package(inst_specific_templates)
        elif inst_lower == 'kpf':
            ip = kpf_filled.generate_inst_package(inst_specific_templates)
        else:
            print(f'{inst} filled templates undefined!')
            continue

        result = coll.insert_one(ip)

    # Create script collection
    coll = papahana_util.config_collection('scriptCollect', conf=config)
    coll.drop()
    generate_scripts_collection(coll, inst)

    if args.generate_observers:
        obs_db = config['obs_db']
        print(f"Using DataBase: {obs_db}")
        papahana_util.drop_db(obs_db, config)

        # Create observer collection
        print("...generating observers")

        coll = papahana_util.config_collection('observerCollect',
                                               db_name='obs_db', conf=config)
        coll.drop()
        generate_observer_collection(coll)
