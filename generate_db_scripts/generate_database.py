import generate_utils as utils
import generate_observation_block as ob_utils
import generate_tags as tags_utils
import generate_containers as container_utils
from generate_scripts import generate_scripts_collection
from generate_observers import generate_observer_collection
import pdb

import importlib

import generate_template
from papahana import util as papahana_util
from os import path

CONFIG = 'config.live.yaml'
APP_PATH = path.abspath(path.dirname(__file__))

if __name__=='__main__':
    args = utils.parse_args()
    mode = args.mode
    if not args.mode:
        mode = papahana_util.read_mode()

    config = utils.read_config(mode, f"{APP_PATH}/{CONFIG}")
    instList = config['inst_list']
    ob_db = config['ob_db']

    # print(f"Using DataBase: {ob_db}")
    # papahana_util.drop_db(ob_db, conf=config)

    # generate templates
    print("...generating templates")
    template_list = generate_template.generate_templates(config)

    print("...generating recipes")
    coll = papahana_util.config_collection('recipeCollect', conf=config)
    coll.drop()

    for inst in instList:
        try:
            instModule = importlib.import_module(f'{inst.lower()}_items')
            recipes = instModule.generate_recipes()
        except ModuleNotFoundError as err:
            print(f'{err} for {inst}')
            continue
        except AttributeError as err:
            print(f'{err} for {inst}')
            continue
        for name, schema in recipes.items():
            _ = coll.insert_one(schema)

    # # Create ob_blocks collection,  zero first
    # print("...zeroing deltas")
    # coll = papahana_util.config_collection('deltaCollect', conf=config)
    # coll.drop()

    # # Create ob_blocks collection
    # print("...generating OBs")
    # coll = papahana_util.config_collection('obCollect', conf=config)
    # coll.drop()
    # ob_blocks = []
    # for inst in instList:
    #     ob_blocks += ob_utils.generate_obs(
    #         config, inst.upper(), instList, template_list)

    # # create tags collection
    # coll = papahana_util.config_collection('tagsCollect', conf=config)
    # keck_id_obj_id = tags_utils.generate_tag_list(coll)

    # # add tags randomly to OBs
    # for ob in ob_blocks:
    #     tags_utils.add_tags_to_ob(config, ob, keck_id_obj_id)

    # # Create containers collection
    # print("...generating containers")
    # coll = papahana_util.config_collection('containerCollect', conf=config)
    # coll.drop()
    # container_list = container_utils.generate_containers(config, coll, ob_blocks)

    # Create Instrument package
    print("...generating instrument package")
    coll = papahana_util.config_collection('ipCollect', conf=config)
    coll.drop()

    for inst in instList:
        inst_specific_templates = utils.parse_template_list(
            inst, instList, template_list)
        
        try:
            instModule = importlib.import_module(f'{inst.lower()}_items')
            recipes = instModule.generate_recipes()
            rlist = [ x['metadata']['name'] for key, x in recipes.items()] 
            ip = instModule.generate_inst_package(template_list=inst_specific_templates, rlist=rlist)
        except ModuleNotFoundError as err:
            print(f'{err} for {inst}')
            continue
        except AttributeError as err:
            print(f'{err} for {inst}')
            continue

        result = coll.insert_one(ip)

    # # Create script collection
    # print('...creating scripts')
    # coll_script = papahana_util.config_collection('scriptCollect', conf=config)
    # coll_inst = papahana_util.config_collection('ipCollect', conf=config)
    # coll_tmp = papahana_util.config_collection('templateCollect', conf=config)
    # coll_script.drop()
    # for inst in instList:
    #     generate_scripts_collection(coll_script, coll_inst, coll_tmp, inst)

    # if args.generate_observers:
    #     obs_db = config['obs_db']
    #     print(f"Using DataBase: {obs_db}")
    #     papahana_util.drop_db(obs_db, config)

    #     # Create observer collection
    #     print("...generating observers")

    #     coll = papahana_util.config_collection('observerCollect',
    #                                            db_name='obs_db', conf=config)
    #     coll.drop()
    #     generate_observer_collection(coll)

