from generate_scripts import generate_scripts_collection
from kpf_templates import kpf_common_parameters, kpf_science,  kpf_acq, kpf_arc, kpf_darks, kpf_target
from kpf_recipes import kpf_recipes
from papahana import util as papahana_util

import generate_utils as utils
import pymongo

from papahana import util as papahana_util
from os import path

CONFIG = 'config.live.ini'
APP_PATH = path.abspath(path.dirname(__file__))
INST_LIST = ['KPF', 'KCWI', 'SSC']


def generate_kpf_ip(template_list, recipe_list):

    rlist = []
    for recipe_schema in recipe_list:
        rlist.append(recipe_schema['metadata']['name'])

    schema = {
        "metadata": {
            "name": "kpf_instrument_package",
            "ui_name": "KPF Instrument Package",
            "version": "0.0.1",
            "instrument": "KPF",
            "observing_modes": ["spectroscopy"]
        },
        "optical_parameters": {
        },
        "configurable_elements": [
        ],
        "pointing_origins": ["KPF", "SKY", "EM_SKY", "REF"
        ],
        "template_list": utils.parse_templates_version(template_list),
        "recipe_list": rlist,
        "event_table": 'null',
        "comment": "A KPF Instrument Package"
    }

    return schema


def gen_inst_package(config, template_list=None):
    print("...generating instrument package")

    # add templates
    if not template_list:
        coll_tmp = papahana_util.config_collection('templateCollect', conf=config)
        fields = {'metadata.name': 1, 'metadata.version': 1}
        template_list = list(coll_tmp.find({}, fields))

    # add recipes
    coll_recipe = papahana_util.config_collection('recipeCollect', conf=config)
    fields = {'metadata.name': 1, '_id': 0}
    recipe_list = list(coll_recipe.find({}, fields))

    coll = papahana_util.config_collection('ipCollect', conf=config)
    coll.drop()

    inst_specific_templates = utils.parse_template_list('KPF', INST_LIST, template_list)
    ip = generate_kpf_ip(inst_specific_templates, recipe_list)

    return ip



if __name__=='__main__':
    args = utils.parse_args()
    mode = args.mode
    if not args.mode:
        mode = papahana_util.read_mode()

    config = utils.read_config(mode, f"{APP_PATH}/{CONFIG}")
    ob_db = config['ob_db']

    if args.drop:
        print(f"Using DataBase: {ob_db}")
        papahana_util.drop_db(ob_db, conf=config)

    # generate templates
    if args.generate_templates:
        print("...generating templates")
        coll = papahana_util.config_collection('templateCollect', conf=config)
        coll.drop()

        templates = [kpf_common_parameters, kpf_science, kpf_acq, kpf_arc, kpf_darks, kpf_target]

        result = coll.insert_many(templates, ordered=False, bypass_document_validation=True)

    # Create recipe collection
    if args.generate_recipes:
        print("...generating recipes")
        coll = papahana_util.config_collection('recipeCollect', conf=config)
        coll.drop()

        kpf_recipes = kpf_recipes()
        for name, schema in kpf_recipes.items():
            _ = coll.insert_one(schema)

    inst = 'KPF'
    inst_lower = 'kpf'

    # generate instrument package
    if args.generate_ip:
        print("...generating instrument package")

        # add templates
        coll_tmp = papahana_util.config_collection('templateCollect', conf=config)
        fields = {'metadata.name': 1, 'metadata.version': 1}
        template_list = list(coll_tmp.find({}, fields))

        # add recipes
        coll_recipe = papahana_util.config_collection('recipeCollect', conf=config)
        fields = {'metadata.name': 1, '_id': 0}
        recipe_list = list(coll_recipe.find({}, fields))

        coll = papahana_util.config_collection('ipCollect', conf=config)
        coll.drop()

        inst_specific_templates = utils.parse_template_list(
            inst, INST_LIST, template_list)
        ip = generate_kpf_ip(inst_specific_templates, recipe_list)

        result = coll.insert_one(ip)

    # Create script collection
    if args.generate_scripts:
        print("...generating scripts")
        coll = papahana_util.config_collection('scriptCollect', conf=config)
        coll.drop()

        coll_inst = papahana_util.config_collection('ipCollect', conf=config)
        coll_tmp = papahana_util.config_collection('templateCollect', conf=config)

        generate_scripts_collection(coll, coll_inst, coll_tmp, 'KPF')

    # set of collections:
    # collections = ('containers', 'deltas_observation_blocks', 'instrument_packages',
    #                'ob_recipes', 'observation_blocks', 'tag_info', 'templates')

    collections = ('obCollect', 'obDeltaCollect', 'observerCollect',
                   'containerCollect', 'scriptCollect', 'recipeCollect',
                   'templateCollect', 'ipCollect', 'deltaCollect',
                   'tagsCollect')
    # db = config[db_name]
    mongo_url = papahana_util.compose_set_url(config)
    mongo = pymongo.MongoClient(mongo_url)
    db = mongo[ob_db]

    for collection in collections:
        # if no observation_blocks colection -- create
        collectName = config[collection]
        collist = db.list_collection_names()
        # print(collist)
        if collectName in collist:
            # print(collectName, collist)
            mycol = db[collectName]

        # papahana_util.create_collection(collection, ob_db, mongo_url)


