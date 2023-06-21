import generate_utils as utils
from common_template import dither_schema
import generate_random_utils as random_utils

def filled_common_parameters():

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
    return nires_common_parameters_template 

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
    acq_templates = [ {
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
            },
            "tcs_coord_raoff": {
                "ui_name": "The offset from coordinates to get to the target",
                "option": "range",
                "allowed": [0.0, 2000.0],
                "default": 0,
                "optionality": "optional",
                "type": "float",
                "units": "arcseconds"
            },
            "tcs_coord_decoff": {
                "ui_name": "The offset from coordinates to get to the target",
                "option": "range",
                "allowed": [0.0, 2000.0],
                "default": 0,
                "optionality": "optional",
                "type": "float",
                "units": "arcseconds"
            },
            "rot_cfg_wrap": {
                "ui_name": "Rotator Wrap Position",
                "option": "set",
                "allowed": ['south', 'north', 'auto'],
                "default": 'auto',
                "optionality": "optional",
                "type": "string",
                "units": None
            },
            "rot_cfg_mode": {
                "ui_name": "Rotator Mode",
                "option": "set",
                "allowed": ["PA", "stationary", "vertical_angle"],
                "default": "PA",
                "optionality": "optional",
                "type": "string",
                "units": None
            },
            "rot_coord_angle": {
                "ui_name": "The rotator angle",
                "option": "range",
                "allowed": [0.0, 360.0],
                "default": 0,
                "optionality": "optional",
                "type": "float",
                "units": "degrees"
            },
            "guider1_coord_ra": {
                "ui_name": "Guide Star Right Ascension",
                "option": "regex",
                "allowed": 'HH:MM:SS.SS',
                "default": None,
                "optionality": "optional",
                "type": "string",
                "units": "Hours:Minutes:Seconds"
            },
            "guider1_coord_dec": {
                "ui_name": "Guide Star Declination",
                "option": "regex",
                "allowed": "DD:MM:SS.S",
                "default": None,
                "optionality": "optional",
                "type": "string",
                "units": "Degrees:Minutes:Seconds"
            },
            "guider1_cfg_mode": {

                "ui_name": "Guide Star Selection Mode",
                "option": "list",
                "allowed": ["auto", "operator", "user"],
                "default": "operator",
                "optionality": "optional",
                "type": "string",
                "units": None
            },
            "bright_acquisition": {
                "default": None,
                "description": "Is acq bright? If false, take a sky image",
                "option": "boolean",
                "optionality": "optional",
                "type": "boolean",
                "ui_name": "Bright Acquisition",
                "units": None
            },
        },
    }
    ]
    return acq_templates

def filled_sci_templates(template_list):
    sci_templates = [ {
        "metadata": {
            "instrument": "NIRES",
            "name": "nires_stare_sci",
            "script": "nires_stare_sci",
            "template_type": "science",
            "ui_name": "NIRES stare science",
            "version": "0.1.0"
        },
        "parameters": {
            "target_info_object": {
                "default": "",
                "description": "Value for the object keyword",
                "option": "open",
                "optionality": "optional",
                "type": "string",
                "ui_name": "Object Keyword",
                "units": None
            },
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
                "description": "Number of coadd exposures to take",
                "option": "range",
                "optionality": "required",
                "type": "integer",
                "ui_name": "Number of Coadd Exposures",
                "units": None
            },
            "det_exp_read_pairs": {
                "allowed": [
                    1,
                    100
                ],
                "default": None,
                "description": "Number of read pairs",
                "option": "range",
                "optionality": "required",
                "type": "integer",
                "ui_name": "Number of Read Pairs",
                "units": None
            },
            "det_samp_mode": {
                "ui_name": "Sampling Mode",
                "option": "list",
                "allowed": ["MCDS", "PCDS", "UTR", "Single"],
                "default": "MCDS",
                "optionality": "optional",
                "type": "string",
                "units": None
            },
            "det_coord_north_off": {
                "ui_name": "North offset",
                "option": "range",
                "allowed": [0.0, 2000.0],
                "default": 0,
                "optionality": "optional",
                "type": "float",
                "units": "arcseconds"
            },
            "det_coord_east_off": {
                "ui_name": "East offset",
                "option": "range",
                "allowed": [0.0, 2000.0],
                "default": 0,
                "optionality": "optional",
                "type": "float",
                "units": "arcseconds"
            },
        }
    },
    {
        "metadata": {
            "instrument": "NIRES",
            "name": "nires_dither_sci",
            "script": "nires_dither_sci",
            "template_type": "science",
            "ui_name": "NIRES dither science",
            "version": "0.1.0"
        },
        "parameters": {
            "target_info_object": {
                "default": "",
                "description": "Value for the object keyword",
                "option": "open",
                "optionality": "optional",
                "type": "string",
                "ui_name": "Object Keyword",
                "units": None
            },
            "det_type_mode": {
                "ui_name": "Spectrograph or Imager",
                "option": "list",
                "allowed": ["Spectrograph", "Imager", "Both"],
                "default": "Spectorgraph",
                "optionality": "required",
                "type": "string",
                "units": None
            },
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
                "description": "Number of coadd exposures to take",
                "option": "range",
                "optionality": "required",
                "type": "integer",
                "ui_name": "Number of Coadd Exposures",
                "units": None
            },
            "det_exp_read_pairs": {
                "allowed": [
                    1,
                    100
                ],
                "default": None,
                "description": "Number of read pairs",
                "option": "range",
                "optionality": "required",
                "type": "integer",
                "ui_name": "Number of Read Pairs",
                "units": None
            },
            "det_samp_mode": {
                "ui_name": "Sampling Mode",
                "option": "list",
                "allowed": ["MCDS", "PCDS", "UTR", "Single"],
                "default": "MCDS",
                "optionality": "optional",
                "type": "string",
                "units": None
            },
            "det_coord_north_off": {
                "ui_name": "North offset",
                "option": "range",
                "allowed": [0.0, 2000.0],
                "default": 0,
                "optionality": "optional",
                "type": "float",
                "units": "arcseconds"
            },
            "det_coord_east_off": {
                "ui_name": "East offset",
                "option": "range",
                "allowed": [0.0, 2000.0],
                "default": 0,
                "optionality": "optional",
                "type": "float",
                "units": "arcseconds"
            },
            "sequence_ndither": {
                "ui_name": "Number of dither positions",
                "option": "range",
                "allowed": [0, 100],
                "default": None,
                "optionality": "required",
                "type": "integer",
            },
            "sequence_ditarray": dither_schema
            }
    },
    {
        "metadata": {
            "instrument": "NIRES",
            "name": "nires_drift_scan_sci",
            "script": "nires_drift_scan_sci",
            "template_type": "science",
            "ui_name": "NIRES stare science",
            "version": "0.1.0"
        },
        "parameters": {
            "target_info_object": {
                "default": "",
                "description": "Value for the object keyword",
                "option": "open",
                "optionality": "optional",
                "type": "string",
                "ui_name": "Object Keyword",
                "units": None
            },
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
                "description": "Number of coadd exposures to take",
                "option": "range",
                "optionality": "required",
                "type": "integer",
                "ui_name": "Number of Coadd Exposures",
                "units": None
            },
            "det_exp_read_pairs": {
                "allowed": [
                    1,
                    100
                ],
                "default": None,
                "description": "Number of read pairs",
                "option": "range",
                "optionality": "required",
                "type": "integer",
                "ui_name": "Number of Read Pairs",
                "units": None
            },
            "det_samp_mode": {
                "ui_name": "Sampling Mode",
                "option": "list",
                "allowed": ["MCDS", "PCDS", "UTR", "Single"],
                "default": "MCDS",
                "optionality": "optional",
                "type": "string",
                "units": None
            },
            "det_drift_length": {
                "ui_name": "Length to drift over",
                "option": "range",
                "allowed": [0.0, 100.0],
                "default": 0,
                "optionality": "optional",
                "type": "float",
                "units": "arcseconds"
            },
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
            "observing_modes": ["imaging", "spectroscopy"]
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

nires_stare_science_template = {
    "metadata": {
        "instrument": "NIRES",
        "name": "nires_stare_sci",
        "script": "nires_stare_sci",
        "template_type": "science",
        "ui_name": "NIRES stare science",
        "version": "0.1.0"
    },
    "parameters": {
        "target_info_object": {
            "default": "",
            "description": "Value for the object keyword",
            "option": "open",
            "optionality": "optional",
            "type": "string",
            "ui_name": "Object Keyword",
            "units": None
        },
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
            "description": "Number of coadd exposures to take",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Coadd Exposures",
            "units": None
        },
        "det_exp_read_pairs": {
            "allowed": [
                1,
                100
            ],
            "default": None,
            "description": "Number of read pairs",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Read Pairs",
            "units": None
        },
        "det_samp_mode": {
            "ui_name": "Sampling Mode",
            "option": "list",
            "allowed": ["MCDS", "PCDS", "UTR", "Single"],
            "default": "MCDS",
            "optionality": "optional",
            "type": "string",
            "units": None
        },
        "det_coord_north_off": {
            "ui_name": "North offset",
            "option": "range",
            "allowed": [0.0, 2000.0],
            "default": 0,
            "optionality": "optional",
            "type": "float",
            "units": "arcseconds"
        },
        "det_coord_east_off": {
            "ui_name": "East offset",
            "option": "range",
            "allowed": [0.0, 2000.0],
            "default": 0,
            "optionality": "optional",
            "type": "float",
            "units": "arcseconds"
        },
    }
}

nires_dither_science_template = {
    "metadata": {
        "instrument": "NIRES",
        "name": "nires_dither_sci",
        "script": "nires_dither_sci",
        "template_type": "science",
        "ui_name": "NIRES dither science",
        "version": "0.1.0"
    },
    "parameters": {
        "target_info_object": {
            "default": "",
            "description": "Value for the object keyword",
            "option": "open",
            "optionality": "optional",
            "type": "string",
            "ui_name": "Object Keyword",
            "units": None
        },
        "det_type_mode": {
            "ui_name": "Spectrograph or Imager",
            "option": "list",
            "allowed": ["Spectrograph", "Imager", "Both"],
            "default": "Spectorgraph",
            "optionality": "required",
            "type": "string",
            "units": None
        },
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
            "description": "Number of coadd exposures to take",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Coadd Exposures",
            "units": None
        },
        "det_exp_read_pairs": {
            "allowed": [
                1,
                100
            ],
            "default": None,
            "description": "Number of read pairs",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Read Pairs",
            "units": None
        },
        "det_samp_mode": {
            "ui_name": "Sampling Mode",
            "option": "list",
            "allowed": ["MCDS", "PCDS", "UTR", "Single"],
            "default": "MCDS",
            "optionality": "optional",
            "type": "string",
            "units": None
        },
        "det_coord_north_off": {
            "ui_name": "North offset",
            "option": "range",
            "allowed": [0.0, 2000.0],
            "default": 0,
            "optionality": "optional",
            "type": "float",
            "units": "arcseconds"
        },
        "det_coord_east_off": {
            "ui_name": "East offset",
            "option": "range",
            "allowed": [0.0, 2000.0],
            "default": 0,
            "optionality": "optional",
            "type": "float",
            "units": "arcseconds"
        },
        "sequence_ndither": {
            "ui_name": "Number of dither positions",
            "option": "range",
            "allowed": [0, 100],
            "default": None,
            "optionality": "required",
            "type": "integer",
        },
        "sequence_ditarray": dither_schema
        }
}

nires_drift_scan_science_template = {
    "metadata": {
        "instrument": "NIRES",
        "name": "nires_drift_scan_sci",
        "script": "nires_drift_scan_sci",
        "template_type": "science",
        "ui_name": "NIRES drift scan science",
        "version": "0.1.0"
    },
    "parameters": {
        "target_info_object": {
            "default": "",
            "description": "Value for the object keyword",
            "option": "open",
            "optionality": "optional",
            "type": "string",
            "ui_name": "Object Keyword",
            "units": None
        },
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
            "description": "Number of coadd exposures to take",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Coadd Exposures",
            "units": None
        },
        "det_exp_read_pairs": {
            "allowed": [
                1,
                100
            ],
            "default": None,
            "description": "Number of read pairs",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Read Pairs",
            "units": None
        },
        "det_samp_mode": {
            "ui_name": "Sampling Mode",
            "option": "list",
            "allowed": ["MCDS", "PCDS", "UTR", "Single"],
            "default": "MCDS",
            "optionality": "optional",
            "type": "string",
            "units": None
        },
        "det_drift_length": {
            "ui_name": "Length to drift over",
            "option": "range",
            "allowed": [0.0, 100.0],
            "default": 0,
            "optionality": "optional",
            "type": "float",
            "units": "arcseconds"
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
        },
        "tcs_coord_raoff": {
            "ui_name": "The offset from coordinates to get to the target",
            "option": "range",
            "allowed": [0.0, 2000.0],
            "default": 0,
            "optionality": "optional",
            "type": "float",
            "units": "arcseconds"
        },
        "tcs_coord_decoff": {
            "ui_name": "The offset from coordinates to get to the target",
            "option": "range",
            "allowed": [0.0, 2000.0],
            "default": 0,
            "optionality": "optional",
            "type": "float",
            "units": "arcseconds"
        },
        "rot_cfg_wrap": {
            "ui_name": "Rotator Wrap Position",
            "option": "set",
            "allowed": ['south', 'north', 'auto'],
            "default": 'auto',
            "optionality": "optional",
            "type": "string",
            "units": None
        },
        "rot_cfg_mode": {
            "ui_name": "Rotator Mode",
            "option": "set",
            "allowed": ["PA", "stationary", "vertical_angle"],
            "default": "PA",
            "optionality": "optional",
            "type": "string",
            "units": None
        },
        "rot_coord_angle": {
            "ui_name": "The rotator angle",
            "option": "range",
            "allowed": [0.0, 360.0],
            "default": 0,
            "optionality": "optional",
            "type": "float",
            "units": "degrees"
        },
        "guider1_coord_ra": {
            "ui_name": "Guide Star Right Ascension",
            "option": "regex",
            "allowed": 'HH:MM:SS.SS',
            "default": None,
            "optionality": "optional",
            "type": "string",
            "units": "Hours:Minutes:Seconds"
        },
        "guider1_coord_dec": {
            "ui_name": "Guide Star Declination",
            "option": "regex",
            "allowed": "DD:MM:SS.S",
            "default": None,
            "optionality": "optional",
            "type": "string",
            "units": "Degrees:Minutes:Seconds"
        },
        "guider1_cfg_mode": {

            "ui_name": "Guide Star Selection Mode",
            "option": "list",
            "allowed": ["auto", "operator", "user"],
            "default": "operator",
            "optionality": "optional",
            "type": "string",
            "units": None
        },
        "bright_acquisition": {
            "default": None,
            "description": "Is acq bright? If false, take a sky image",
            "option": "boolean",
            "optionality": "optional",
            "type": "boolean",
            "ui_name": "Bright Acquisition",
            "units": None
        },
    },
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

