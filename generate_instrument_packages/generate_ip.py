from papahana import util as papahana_util
import argparse
import importlib
from os import path
import yaml

CONFIG = 'config.live.yaml'
APP_PATH = path.abspath(path.dirname(__file__))


def parse_args():
    """
    Parse the command line arguments.

    :return: <obj> commandline arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--mode", "-m", type=str, default='dev', required=True,
                        help="The configuration to read")

    parser.add_argument("--inst", type=str, required=True,
                        help="The instrument to generate a package for")

    parser.add_argument("--replace", type=int, default=1,
                        help="The configuration to read")

    parser.add_argument("--generate_templates", "-t", type=int, default=1,
                        help="The configuration to read")

    parser.add_argument("--generate_scripts", "-s", type=int, default=1,
                        help="The configuration to read")

    parser.add_argument("--generate_recipes", "-r", type=int, default=1,
                        help="The configuration to read")

    parser.add_argument("--generate_ip", "-i", type=int, default=1,
                        help="The configuration to read")

    return parser.parse_args()


def read_config(mode, config):
    with open(config) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)[mode]

    return config


if __name__=='__main__':
    args = parse_args()
    mode = args.mode
    if not args.mode:
        mode = papahana_util.read_mode()

    config = read_config(mode, f"{APP_PATH}/{CONFIG}")

    inst = args.inst.upper()
    replace = args.replace

    inst_mod = importlib.import_module(f'instpack_{inst.lower()}')
    inst_cls = getattr(inst_mod, f"InstPack_{inst}")
    inst_obj = inst_cls('KPF')

    # generate templates
    if args.generate_templates:
        inst_obj.generate_templates(config, replace=replace)

    # Create recipe collection
    if args.generate_recipes:
        inst_obj.generate_recipes(config, replace=replace)

    # generate instrument package
    if args.generate_ip:
        ip = inst_obj.get_inst_package(config, None)
        coll = papahana_util.config_collection('ipCollect', conf=config)

        # delete the current instrument package
        query = {
            'metadata.name': ip['metadata']['name'],
            'metadata.version': ip['metadata']['version']
        }
        result = coll.delete_many(query)

        coll.insert_one(ip)

    # Create script collection
    if args.generate_scripts:
        print("...generating scripts")
        coll = papahana_util.config_collection('scriptCollect', conf=config)

        query = {'metadata.instrument': inst}

        # Delete the matching records
        result = coll.delete_many(query)

        coll_inst = papahana_util.config_collection('ipCollect', conf=config)
        coll_tmp = papahana_util.config_collection('templateCollect', conf=config)

        inst_obj.generate_inst_scripts(coll, coll_inst, coll_tmp, inst)
