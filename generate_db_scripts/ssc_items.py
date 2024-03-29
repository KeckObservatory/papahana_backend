import generate_utils as utils
import generate_random_utils as random_utils

def filled_acq_templates():
    acq_templates = [
        {
            "metadata": {
                "name": "ssc_acq",
                "ui_name": "SSC Acquisition",
                "instrument": "SSC",
                "template_type": "acquisition",
                "version": "0.1.0",
                "script": "ssc_acq",
                "script_version": "0.1.0",
                "sequence_number": 0
            },
        }
    ]

    return acq_templates


def filled_common_parameters():
    schema = {
        "metadata": {
            "instrument": "SSC",
            "name": "ssc_common_parameters",
            "template_type": "common_parameters",
            "ui_name": "SSC Common Parameters",
            "version": "0.1.0"
        },
        "detector_parameters": {
            "det1_cfg_binning": {
                "allowed": ["1x1", "2x2", "4x4", "8x8"],
                "default": "1",
                "option": "set",
                "optionality": "optional",
                "type": "string",
                "ui_name": "Binning",
                "units": None
            },
            "det1_mode_gain": {
                "allowed": [1, 2, 5, 10],
                "default": 1,
                "option": "set",
                "optionality": "optional",
                "type": "integer",
                "ui_name": "The gain",
                "units": None
            },
        },
        "instrument_parameters": {
        }
    }

    return schema


def filled_sci_templates(template_list):
    templates_version = utils.parse_templates_version(template_list)


    sci_templates = [
        {
            "metadata": {
                "instrument": "SSC",
                "name": "ssc_sci",
                "script": "ssc_sci",
                "script_version": "0.1.0",
                "sequence_number": 1,
                "template_type": "science",
                "ui_name": "SSC image",
                "version": templates_version["ssc_sci"]
            },
            "parameters": {
                "det1_exp_number": random_utils.randInt(1, 100),
                "det1_exp_time": random_utils.randInt(1, 3600),
            },
        }
    ]

    return sci_templates


def generate_inst_package(template_list, rlist):

    schema = {
        "metadata": {
            "name": "ssc_instrument_package",
            "ui_name": "SSC Instrument Package",
            "version": "0.1.0",
            "instrument": "SSC",
            "observing_modes": ["imaging"]
        },
        "optical_parameters": {
            "field_of_view": [30.24, 40.32],
            "pixel_scale": 0.105
        },
        "pointing_origins": ["REF"],
        "template_list": utils.parse_templates_version(template_list),
        "event_table": 'null',
        "comment": "A SSC Instrument Package"
    }

    return schema

ssc_acq_template = {
    "metadata": {
        "instrument": "SSC",
        "name": "ssc_acq",
        "script": "ssc_acq",
        "sequence_number": 0,
        "template_type": "acquisition",
        "ui_name": "SSC direct",
        "version": "0.1.0"
    },
    "parameters": {
        "tcs_coord_decoff": {
            "allowed": [0.0, 2000.0],
            "default": 0,
            "option": "range",
            "optionality": "optional",
            "type": "float",
            "ui_name": "The declination offset from coordinates to get to the target",
            "units": "arcseconds"
        },
        "tcs_coord_raoff": {
            "allowed": [0.0, 2000.0],
            "default": 0,
            "option": "range",
            "optionality": "optional",
            "type": "float",
            "ui_name": "The right ascension offset from coordinates to get to the target",
            "units": "arcseconds"
        }
    }
}

ssc_common_parameters_template = {
    "detector_parameters": {
        "det1_cfg_binning": {
            "allowed": ["1x1", "2x2", "4x4", "8x8"],
            "default": "1",
            "option": "set",
            "optionality": "optional",
            "type": "string",
            "ui_name": "Binning",
            "units": None
        },
        "det1_mode_gain": {
            "allowed": [1, 2, 5, 10],
            "default": 1,
            "option": "set",
            "optionality": "optional",
            "type": "integer",
            "ui_name": "The gain",
            "units": None
        },
    },
    "instrument_parameters": {
    },
    "metadata": {
        "instrument": "SSC",
        "name": "ssc_common_parameters",
        "template_type": "common_parameters",
        "ui_name": "SSC Common Parameters",
        "version": "0.1.0"
    }
}


ssc_sci_template = {
    "metadata": {
        "instrument": "SSC",
        "name": "ssc_sci",
        "script": "ssc_sci",
        "sequence_number": 1,
        "template_type": "science",
        "ui_name": "SSC image",
        "version": "0.1.0"
    },
    "parameters": {
        "det1_exp_number": {
            "allowed": [0.0, 100.0],
        "default": None,
        "option": "range",
        "optionality": "required",
        "type": "integer",
        "ui_name": "Number of exposures per image position",
        "units": None
        },
        "det1_exp_time": {
            "allowed": [0.0, 3600.0 ],
            "default": None,
            "option": "range",
            "optionality": "required",
            "type": "float",
            "ui_name": "Exposure time for individual exposures",
            "units": "seconds"
        },
    }
}

ssc_sci_dither_template = {
    "metadata": {
        "instrument": "SSC",
        "name": "ssc_sci_dither",
        "script": "ssc_sci_dither",
        "sequence_number": 1,
        "template_type": "science",
        "ui_name": "SSC dither",
        "version": "0.1.0"
    },
    "parameters": {
        "det1_exp_number": {
            "allowed": [0.0, 100.0],
            "default": None,
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of exposures per dither position",
            "units": None
        },
        "det1_exp_time": {
            "allowed": [0.0, 3600.0],
            "default": None,
            "option": "range",
            "optionality": "required",
            "type": "float",
            "ui_name": "Exposure time for individual exposures",
            "units": "seconds"
        },
        "sequence_ditarray": {
            "allowed": [
                {
                    "seq_dither_ra_offset": {
                        "allowed": [-20.0, 20.0],
                        "default": None,
                        "option": "range",
                        "optionality": "required",
                        "type": "float",
                        "ui_name": "Right Ascension Offset",
                        "units": "arcseconds"
                    }
                },
                {
                    "seq_dither_dec_offset": {
                        "allowed": [-20.0, 20.0],
                        "default": None,
                        "option": "range",
                        "optionality": "required",
                        "type": "float",
                        "ui_name": "Declination Offset",
                        "units": "arcseconds"
                    }
                },
                {
                    "seq_dither_position": {
                        "allowed": ["T", "S", "O"],
                        "default": None,
                        "option": "set",
                        "optionality": "required",
                        "type": "string",
                        "ui_name": "Telescope Position",
                        "units": None
                    }
                },
            ],
            "default": None,
            "option": "set",
            "optionality": "required",
            "type": "array",
            "ui_name": "Dither Pattern"
        },
        "sequence_ndither": {
            "allowed": [0, 100],
            "default": None,
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of dither positions"
        }
    }
}

def generate_recipes():
    recipes = {}
    return recipes

def generate_scripts():
    scripts = {}
    scripts['ssc_acq'] = [
      ["BEGIN_SLEW", "Starts telescope slew"],
      ["WAITFOR_SLEW", "Execution queue locked while slewing"],
      ["ACQUIRE", "OA acquires to PO"],
      ["WAITFOR_ACQUIRE", "Execution queue locked while acquiring"],
      ["CONFIGURE_FOR_SCIENCE", "Sets up SSC for science"],
      ["WAITFOR_CONFIGURE_SCIENCE", "Execution queue locked while science is being configured"]
    ]

    scripts['ssc_sci'] = [
      ["EXECUTE_OBSERVATION", "Point and shoot"]
    ]
    return scripts

