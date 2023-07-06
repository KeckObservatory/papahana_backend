import argparse
import yaml

from papahana import util as papahana_util
from copy import deepcopy
from collections import OrderedDict
from os import path

CONFIG = 'config.live.yaml'
APP_PATH = path.abspath(path.dirname(__file__))

target_base_parameters = OrderedDict([
    ("target_info_name", {
        "ui_name": "Target Name",
        "option": "regex",
        "allowed": ['[ -~]{100}'],
        "default": None,
        "optionality": "required",
        "type": "string",
        "units": None
    }),
    ("target_coord_ra", {
        "ui_name": "Right Ascension",
        "option": "regex",
        "description": "In sexigesimal (00:00:00) or decimal degrees.",
        "allowed": ['^\d{2}:\d{2}:\d{2}$',
                    '^\d{2}:\d{2}:\d{2}.\d{1}$',
                    '^\d{2}:\d{2}:\d{2}.\d{2}$'],
        "default": None,
        "optionality": "required",
        "type": "string",
        "units": "Hours:Minutes:Seconds"
    }),
    ("target_coord_dec", {
        "ui_name": "Declination",
        "option": "regex",
        "description": "In sexigesimal (00:00:00) or decimal degrees.",
        "allowed": ['^\d{2}:\d{2}:\d{2}$',
                    '^\d{2}:\d{2}:\d{2}.\d{1}$',
                    '^\d{2}:\d{2}:\d{2}.\d{2}$',
                    '^-\d{2}:\d{2}:\d{2}$',
                    '^-\d{2}:\d{2}:\d{2}.\d{1}$',
                    '^-\d{2}:\d{2}:\d{2}.\d{2}$'],
        "default": None,
        "optionality": "required",
        "type": "string",
        "units": "Degrees:Minutes:Seconds"
    }),
    ("target_coord_pm_ra", {
        "ui_name": "Proper Motion (RA)",
        "option": "range",
        "allowed": [0.0, 5000.0],
        "default": 0.0,
        "optionality": "optional",
        "type": "string",
        "units": "arcseconds/yr"
    }),
    ("target_coord_pm_dec", {
        "ui_name": "Proper Motion (DEC)",
        "option": "range",
        "allowed": [0.0, 100.0],
        "default": 0.0,
        "optionality": "optional",
        "type": "string",
        "units": "arcseconds/yr"
    }),
    ("target_coord_frame", {
        "ui_name": "Frame",
        "option": "set",
        "allowed": ['mount', 'FK5'],
        "default": 'FK5',
        "optionality": "optional",
        "type": "string",
        "units": None
    }),
    ("target_coord_epoch", {
        "ui_name": "Epoch",
        "option": "range",
        "allowed": [1900.0, 2100.0],
        "default": 'FK5',
        "optionality": "optional",
        "type": "float",
        "units": "year"
    }),
    ("rot_cfg_pa", {
        "ui_name": "Position Angle",
        "option": "range",
        "allowed": [0.0, 360.0],
        "default": 0.0,
        "optionality": "optional",
        "type": "float",
        "units": "Degrees"
    }),
    ("target_magnitude", {
        "ui_name": "Target Magnitude",
        "option": "list",
        "allowed": [
            {'target_info_band': {
                "ui_name": "Spectral Band",
                "option": "set",
                "allowed": ['V', 'R', 'I', 'J', 'H', 'K'],
                "default": None,
                "optionality": "required",
                "type": "string",
                "units" : None}
            },
            {'target_info_mag': {
                "ui_name": "Magnitude",
                "option": "range",
                "allowed": ['-27.0', '50.0'],
                "default": None,
                "optionality": "required",
                "type": "float",
                "units": 'Apparent'}}
        ],
        "default": None,
        "optionality": "required",
        "type": "array",
        "units": None
    }),
    ("seq_constraint_obstime", {
        "ui_name": "Scheduled Time of Observation",
        "option": "regex",
        "allowed": [None, '^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'],
        "default": None,
        "optionality": "optional",
        "type": "string",
        "units": 'YR-MM-DD hh:mm:ss'
    }),
    ("target_info_comment", {
        "ui_name": "Target Comment",
        "option": "regex",
        "allowed": [None, '[ -~]{100}'],
        "default": None,
        "optionality": "optional",
        "type": "string",
        "units": None
    })
])

nonsidereal_extra_params = deepcopy(target_base_parameters)
nonsidereal_extra_params["target_coord_dra"] = {
        "ui_name": "Differential Tracking (RA)",
        "option": 'range',
        "allowed": [0.0, 5000.0],
        "default": None,
        "optionality": "required",
        "type": "float",
        "units": 'acrseconds/hr'
    }
nonsidereal_extra_params["target_coord_ddec"] = {
        "ui_name": "Differential Tracking (DEC)",
        "option": 'range',
        "allowed": [0.0, 5000.0],
        "default": None,
        "optionality": "required",
        "type": "float",
        "units": 'acrseconds/hr'
    }
nonsidereal_extra_params.move_to_end('target_coord_ddec', last=False)
nonsidereal_extra_params.move_to_end('target_coord_dra', last=False)
nonsidereal_extra_params.move_to_end('target_coord_dec', last=False)
nonsidereal_extra_params.move_to_end('target_coord_ra', last=False)
nonsidereal_extra_params.move_to_end('target_info_name', last=False)



mos_extra_params = deepcopy(target_base_parameters)
mos_extra_params["inst_cfg_mask"] = {
        "ui_name": "Mask Name",
        "option": "regex",
        "allowed": ['[ -~]{100}'],
        "default": None,
        "optionality": "required",
        "type": "string",
        "units": None
    }
mos_extra_params.move_to_end('inst_cfg_mask', last=False)
mos_extra_params.move_to_end('target_info_name', last=False)


sidereal_target = OrderedDict([
    ("metadata", {
        "name": "sidereal_target",
        "ui_name": "Sidereal Target",
        "template_type": "target",
        "instrument": "all",
        "version": "0.1.0"
    }),
    ("parameters", target_base_parameters)
])


nonsidereal_target = OrderedDict([
    ("metadata", {
        "name": "non_sidereal_target",
        "ui_name": "Non-Sidereal Target",
        "template_type": "target",
        "instrument": "all",
        "version": "0.1.0"
    }),
    ("parameters", nonsidereal_extra_params)
])



def parse_args():
    """
    Parse the command line arguments.
    :return: <obj> commandline arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--mode", "-m", type=str,
                        default='dev',
                        help="The configuration to read")

    parser.add_argument("--replace", type=int, default=1,
                        help="The configuration to read")

    return parser.parse_args()


def read_config(mode, config):
    with open(config) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)[mode]

    return config


# def generate_templates(config):
if __name__ == '__main__':
    args = parse_args()
    mode = args.mode
    replace = args.replace

    config = read_config(mode, f"{APP_PATH}/{CONFIG}")

    coll = papahana_util.config_collection('templateCollect', conf=config)

    print('...adding target templates to collection')

    templates = []
    templates.append(sidereal_target)
    templates.append(nonsidereal_target)

    if replace != 1:
        for tmp in templates:
            _ = coll.insert_one(tmp)

    else:
        for tmp in templates:
            tmp_name = tmp['metadata']['name']
            query = {'metadata.name': tmp_name}
            fields = {'_id': 1}

            result = list(coll.find(query, fields))
            if not result:
                coll.insert_one(tmp)
                continue

            query = result[0]
            _ = coll.replace_one(query, tmp)


