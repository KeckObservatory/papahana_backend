import argparse

from kpf_templates import kpf_common_parameters, kpf_science,  kpf_acq, kpf_arc, kpf_darks, kpf_target
from kcwi_templates import kcwi_ifu_acq_offsetStar_template, kcwi_ifu_acq_direct_template, kcwi_ifu_sci_stare_template, kcwi_ifu_sci_dither_template, kcwi_common_parameters
from ssc_templates import ssc_acq, ssc_common_parameters, ssc_sci, ssc_sci_dither

from papahana import util as papahana_util
from copy import deepcopy
from collections import OrderedDict


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
        "version": "0.1.0"
    }),
    ("parameters", target_base_parameters)
])


nonsidereal_target = OrderedDict([
    ("metadata", {
        "name": "non_sidereal_target",
        "ui_name": "Non-Sidereal Target",
        "template_type": "target",
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

    return parser.parse_args()


def generate_templates(config):
    coll = papahana_util.config_collection('templateCollect', conf=config)

    coll.drop()
    print('...adding templates to collection')

    templates_kcwi = [
        kcwi_ifu_acq_offsetStar_template,
        kcwi_ifu_acq_direct_template,
        kcwi_ifu_sci_stare_template,
        kcwi_ifu_sci_dither_template]
    templates_targets = [
        sidereal_target,
        nonsidereal_target,
        kcwi_common_parameters
    ]
    templates_kpf = [kpf_common_parameters, kpf_science, kpf_acq, kpf_arc, kpf_darks, kpf_target]
    templates_ssc = [ssc_acq, ssc_common_parameters, ssc_sci]

    templates = []

    templates += templates_kpf
    templates += templates_kcwi
    templates += templates_ssc
    templates += templates_targets

    result = coll.insert_many(templates, ordered=False, bypass_document_validation=True)

    fields = {'metadata.name': 1, 'metadata.version': 1}
    doc = list(coll.find({}, fields))

    return doc
