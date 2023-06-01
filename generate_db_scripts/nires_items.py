import generate_utils as utils
import generate_random_utils as random_utils

def filled_common_parameters():
    common_parameters = {
        "metadata": {
            "name": "nires_common_parameters",
            "ui_name": "NIRES Common Parameters",
            "instrument": "NIRES",
            "template_type": "common_parameters",
            "version": "0.1.0"
        },
        "instrument_parameters": {
        },
        "detector_parameters": {
            "sample_mode": "CDS"
        },
        "guider_parameters": {
        },
        "tcs_parameters": {
        }
    }
    return common_parameters 

def filled_cal_templates():
    cal_templates = [
        {
            "metadata": {
                "instrument": "NIRES",
                "name": "nires_arcs",
                "script": "nires_arcs",
                "template_type": "calibration",
                "ui_name": "NIRES Arc Lamps",
                "version": "0.1.0",
                "sequence_number": 0
            },
            "parameters": {
                "det_exp_time": random_utils.randFloat(3600),
                "det_exp_number": random_utils.randInt(1, 100),
                "target_info_object": 'arc',
            }
        },
        {
            "metadata": {
                "instrument": "NIRES",
                "name": "nires_flats",
                "script": "nires_flats",
                "template_type": "calibration",
                "ui_name": "NIRES Flats",
                "version": "0.1.0",
                "sequence_number": 0
            },
            "parameters": {
                "det_exp_time": random_utils.randFloat(3600),
                "det_exp_number": random_utils.randInt(1, 100),
                "target_info_object": 'flats',
            }
        }
    ]
    return cal_templates

def filled_acq_templates():
    acq_templates = [
        {
            "metadata": {
                "instrument": "NIRES",
                "name": "nires_acq",
                "script": "nires_acq",
                "template_type": "acquisition",
                "ui_name": "NIRES acquisition",
                "version": "0.1.0",
                "sequence_number": 0

            },
            "parameters": {
                "tcs_coord_po": "NIRES"
            }
        }
    ]
    return acq_templates

def filled_sci_templates(template_list):
    sci_templates = [
        {
            "metadata": {
                "instrument": "NIRES",
                "name": "nires_sci",
                "script": "nires_sci",
                "template_type": "science",
                "ui_name": "NIRES science",
                "version": "0.1.0"
            },
            "parameters": {
                "det_exp_time": random_utils.randFloat(3600.0),
                "det_exp_number": random_utils.randInt(1, 100),
                "target_info_object": 'autocal-flat-sci',
            }
        }
    ]
    return sci_templates

def generate_inst_package(template_list, config, inst_list):
    schema = {
        "metadata": {
            "name": "nires_instrument_package",
            "ui_name": "NIRES Instrument Package",
            "version": "0.1.0",
            "instrument": "NIRES",
            "observing_modes": ["spectroscopy"]
        },
        "optical_parameters": {
        },
        "configurable_elements": [
        ],
        "pointing_origins": ["NIRES", "SLIT_IMAG", "REF_SLIT", "REF", "IMAG", "MIRA"
        ],
        "template_list": utils.parse_templates_version(template_list),
        "event_table": None,
        "comment": "A NIRES Instrument Package"
    }
    return schema
nires_common_parameters_template = {
    "metadata": {
        "name": "nires_common_parameters",
        "ui_name": "NIRES Common Parameters",
        "instrument": "NIRES",
        "template_type": "common_parameters",
        "version": "0.1.0"
    },
    "instrument_parameters": {
    },
    "detector_parameters": {
    },
    "guider_parameters": {
    },
    "tcs_parameters": {
    }
}

nires_science_template = {
    "metadata": {
        "instrument": "NIRES",
        "name": "nires_sci",
        "script": "nires_sci",
        "template_type": "science",
        "ui_name": "NIRES science",
        "version": "0.1.0"
    },
    "parameters": {
        "det_exp_time": {
            "allowed": [
                0.1,
                3600
            ],
            "default": None,
            "description": "Exposure time in seconds",
            "option": "range",
            "optionality": "required",
            "type": "float",
            "ui_name": "Exposure time",
            "units": "seconds"
        },
        "det_exp_number": {
            "allowed": [
                1,
                100
            ],
            "default": None,
            "description": "Number of exposures to take",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Exposures",
            "units": None
        },
        "target_info_object": {
            "default": "",
            "description": "Value for the object keyword",
            "option": "open",
            "optionality": "optional",
            "type": "string",
            "ui_name": "Object Keyword",
            "units": None
        },
    }
}

nires_acq_template = {
    "metadata": {
        "instrument": "NIRES",
        "name": "nires_acq",
        "script": "nires_acq",
        "template_type": "acquisition",
        "ui_name": "NIRES acquisition",
        "version": "0.1.0",
        "sequence_number": 0
    },
    "parameters": {
        "guider_cfg_gain": {
            "allowed": [
                "high",
                "medium",
                "low"
            ],
            "description": "Only used if guide mode is manual",
            "option": "set",
            "optionality": "required",
            "type": "string",
            "ui_name": "Guider camera gain (high, medium, or low).",
            "units": None
        },
        "tcs_coord_po": {
            "allowed": [
                "NIRES",
                "SLIT_IMAG",
                "REF_SLIT",
                "IMAG",
                "MIRA",
                "REF"
            ],
            "description": "Pointing origin",
            "option": "set",
            "optionality": "required",
            "type": "string",
            "ui_name": "Pointing origin",
            "units": None
        }
    }
}

nires_arc_template = {
    "metadata": {
        "instrument": "NIRES",
        "name": "nires_arcs",
        "script": "nires_arcs",
        "template_type": "calibration",
        "ui_name": "NIRES Arc Lamps",
        "version": "0.1.0",
        "sequence_number": 0
    },
    "parameters": {
        "det_exp_time": {
            "allowed": [
                0.1,
                3600
            ],
            "default": None,
            "description": "Exposure time in seconds",
            "option": "range",
            "optionality": "required",
            "type": "float",
            "ui_name": "Exposure Time",
            "units": "seconds"
        },
        "det_exp_number": {
            "allowed": [
                1,
                100
            ],
            "default": None,
            "description": "Number of exposures to take",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of exposures to take",
            "units": None
        },
        "target_info_object": {
            "default": "",
            "description": "Value for the object keyword",
            "option": "open",
            "optionality": "optional",
            "type": "string",
            "ui_name": "Value for the object keyword",
            "units": None
        },
    }
}

def generate_scripts():
    scripts = {}

    scripts['nires_acq'] = [
        ['BEGIN_SLEW', 'Starts telescope slew'],
        ['CONFIGURE_FOR_ACQUISITION', 'target parameters, guide camera parameters'],
        ['WAITFOR_CONFIGURE_ACQUISITION', ''],
        ['WAITFOR_SLEW', ''],
        ['ACQUIRE', 'OA acquires to PO'],
        ['WAITFOR_ACQUIRE', ''],
    ]

    scripts['nires_sci'] = [
        ['CONFIGURE_SCIENCE', ''],
        ['WAITFOR_CONFIGURE_SCIENCE', 'Waits detector ready'],
        ['EXECUTE_OBSERVATION', ''],
        ['POST_OBSERVATION_CLEANUP', '']
    ]
    return scripts

