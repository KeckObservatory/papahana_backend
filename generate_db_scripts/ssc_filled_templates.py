import generate_utils as utils
import generate_random_utils as random_utils

def filled_acq_templates():
    acq_templates = [
        {
            "metadata": {
                "name": "ssc_acq_direct",
                "ui_name": "SSC Acquisition",
                "instrument": "SSC",
                "template_type": "acquisition",
                "version": "0.1.1",
                "script": "ssc_acq_direct",
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
            "version": "0.0.1"
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
                "name": "ssc_sci_image",
                "script": "ssc_sci_image",
                "script_version": "0.1.0",
                "sequence_number": 1,
                "template_type": "science",
                "ui_name": "SSC image",
                "version": templates_version["ssc_sci_image"]
            },
            "parameters": {
                "det1_exp_number": random_utils.randInt(1, 100),
                "det1_exp_time": random_utils.randInt(1, 3600),
            },
        }
    ]

    return sci_templates


def generate_inst_package(template_list):

    schema = {
        "metadata": {
            "name": "ssc_instrument_package",
            "ui_name": "SSC Instrument Package",
            "version": "0.0.1",
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
