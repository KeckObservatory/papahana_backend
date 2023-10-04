from common_template import dither_schema
import generate_utils as utils
import generate_random_utils as random_utils
import generate_targets as ge
import numpy as np

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
                "name": "nires_cals",
                "script": "nires_cals",
                "template_type": "calibration",
                "ui_name": "NIRES Calibration",
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
            "tcs_coord_po": np.random.choice( [ "NIRES", "SLIT_IMAG", "REF_SLIT", "IMAG", "MIRA", "REF" ]),
            "tcs_coord_raoff": random_utils.randInt(0, 100),
            "tcs_coord_decoff": random_utils.randInt(0, 100),
            "rot_cfg_wrap": np.random.choice(['south', 'north', 'auto']),
            "rot_cfg_mode": np.random.choice(['PA', 'stationary', 'vertical_angle']),
            "rot_coord_angle": random_utils.randInt(0, 360),
            "guider1_coord_ra": ge.generate_ra(),
            "guider1_coord_dec": ge.generate_dec(),
            "guider1_cfg_mode": np.random.choice(['auto', 'operator', 'user'])
        }
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
            "target_info_object": random_utils.randString(8),
            "det_exp_time": random_utils.randFloat(3600),
            "det_exp_number": random_utils.randInt(0, 100),
            "det_num_fs": random_utils.randInt(0, 100),
            "det_exp_read_pairs": random_utils.randInt(0, 100),
            "det_samp_mode": np.random.choice(["MCDS", "PCDS", "UTR", "Single"]),
            "det_num_fs": random_utils.randInt(0, 100),
            "det_coord_north_off": random_utils.randFloat(2000),
            "det_coord_east_off": random_utils.randFloat(2000)
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
            "target_info_object": random_utils.randString(8),
            "det_exp_time": random_utils.randFloat(3600),
            "det_exp_number": random_utils.randInt(0, 100),
            "det_exp_read_pairs": random_utils.randInt(0, 100),
            "det_samp_mode": np.random.choice(["MCDS", "PCDS", "UTR", "Single"]),
            "det_num_fs": random_utils.randInt(0, 100),
            "det_coord_north_off": random_utils.randFloat(2000),
            "det_coord_east_off": random_utils.randFloat(2000),
            "det_type_mode": np.random.choice(["Spectrograph", "Imager", "Both"]),
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
            "target_info_object": random_utils.randString(8),
            "det_exp_time": random_utils.randFloat(3600),
            "det_exp_number": random_utils.randInt(0, 100),
            "det_exp_read_pairs": random_utils.randInt(0, 100),
            "det_samp_mode": np.random.choice(["MCDS", "PCDS", "UTR", "Single"]),
            "det_num_fs": random_utils.randInt(0, 100),
            "det_coord_north_off": random_utils.randFloat(2000),
            "det_coord_east_off": random_utils.randFloat(2000),
            "det_type_mode": np.random.choice(["Spectrograph", "Imager", "Both"]),
            "det_drift_length": random_utils.randFloat(100)
            }
    }

    ]
    return sci_templates

def generate_inst_package(template_list, rlist):


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
        "recipe_list": rlist,
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
            "default": 1,
            "description": "Number of frames to take",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Frames",
            "units": None
        },
        "det_coadd_number": {
            "allowed": [
                1,
                100
            ],
            "default": 1,
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
            "option": "set",
            "allowed": ["MCDS", "PCDS", "UTR", "Single"],
            "default": "MCDS",
            "optionality": "optional",
            "type": "string",
            "units": None
        },
        "det_num_fs": {
            "allowed": [
                1,
                100
            ],
            "default": None,
            "description": "Applicable for Fowler sample mode only",
            "option": "range",
            "optionality": "optional",
            "type": "integer",
            "ui_name": "Number of MCDS (Fowler) Samples",
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
        "det_type_mode": {
            "ui_name": "Spectrograph, Imager, or Both",
            "option": "set",
            "allowed": ["Spectrograph", "Imager", "Both"],
            "default": "Spectrograph",
            "optionality": "required",
            "type": "string",
            "units": None
        },
        "det_exp_test": {
            "default": False,
            "description": "True prevents exposures from being taken",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Test Mode",
            "units": None
        }
    },
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
            "ui_name": "Spectrograph, Imager, or Both",
            "option": "set",
            "allowed": ["Spectrograph", "Imager", "Both"],
            "default": "Spectrograph",
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
        "det_num_fs": {
            "allowed": [
                1,
                100
            ],
            "default": None,
            "description": "Applicable for Fowler sample mode only",
            "option": "range",
            "optionality": "optional",
            "type": "integer",
            "ui_name": "Number of MCDS (Fowler) Samples",
            "units": None
        },
        "det_exp_number": {
            "allowed": [
                1,
                100
            ],
            "default": 1,
            "description": "Number of frames to take",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Frames",
            "units": None
        },
        "det_coadd_number": {
            "allowed": [
                1,
                100
            ],
            "default": 1,
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
            "option": "set",
            "allowed": ["MCDS", "PCDS", "UTR", "Single"],
            "default": "MCDS",
            "optionality": "required",
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
        "sequence_dither_type": {
            "ui_name": "Dither Type",
            "option": "set",
            "allowed": ["ABBA", "AB", "sp2", "sp3", "sp5", "sp7", "box4", "box5", "box8", "box9", "bxy4", "bxy5", "bxy8", "bxy9"],
            "default": "ABBA",
            "optionality": "required",
            "type": "string",
            "units": None
        },
        "sequence_dither_offset": {
            "ui_name": "Dither Offset",
            "option": "range",
            "allowed": [0, 100],
            "default": None,
            "optionality": "required",
            "units": "arcseconds",
            "type": "float"
        },
        "det_exp_test": {
            "default": False,
            "description": "True prevents exposures from being taken",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Test Mode",
            "units": None
        }
    },
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
            "default": 1,
            "description": "Number of frames to take",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Frames",
            "units": None
        },
        "det_coadd_number": {
            "allowed": [
                1,
                100
            ],
            "default": 1,
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
            "option": "set",
            "allowed": ["MCDS", "PCDS", "UTR", "Single"],
            "default": "MCDS",
            "optionality": "required",
            "type": "string",
            "units": None
        },
        "det_num_fs": {
            "allowed": [
                1,
                100
            ],
            "default": None,
            "description": "Applicable for Fowler sample mode only",
            "option": "range",
            "optionality": "optional",
            "type": "integer",
            "ui_name": "Number of MCDS (Fowler) Samples",
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
        "det_exp_test": {
            "default": False,
            "description": "True prevents exposures from being taken",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Test Mode",
            "units": None
        },
        "det_type_mode": {
            "ui_name": "Spectrograph, Imager, or Both",
            "option": "set",
            "allowed": ["Spectrograph", "Imager", "Both"],
            "default": "Spectrograph",
            "optionality": "required",
            "type": "string",
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
            "option": "set",
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

nires_calibration_template = {
    "metadata": {
        "instrument": "NIRES",
        "name": "nires_calibration",
        "script": "nires_calibration",
        "template_type": "calibration",
        "ui_name": "NIRES Calibration",
        "version": "0.1.0",
        "sequence_number": 0
    },
    "parameters": {
        "det_cal_type": {
            "ui_name": "Calibration Type",
            "option": "set",
            "allowed": ["Arcs", "Darks", "Flats", "Flats On Flats Off"],
            "default": "Darks",
            "optionality": "required",
            "type": "string",
            "units": None
        },
        "det_exp_time": {
            "allowed": [
                0.1,
                3600
            ],
            "default": 120,
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
            "default": 1,
            "description": "Number of frames to take",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Frames",
            "units": None
        },
        "det_coadd_number": {
            "allowed": [
                1,
                100
            ],
            "default": 1,
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
            "default": 1,
            "description": "Number of read pairs",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Read Pairs",
            "units": None
        },
        "det_num_fs": {
            "allowed": [
                1,
                100
            ],
            "default": 1,
            "description": "Applicable for Fowler sampling mode for spectrograph.",
            "option": "range",
            "optionality": "optional",
            "type": "integer",
            "ui_name": "Number of MCDS (Fowler) Samples",
            "units": None
        },
        "det_samp_mode": {
            "ui_name": "Sampling Mode",
            "description": "Note: imager mode always uses MCDS.",
            "option": "set",
            "allowed": ["MCDS", "PCDS", "UTR", "Single"],
            "default": "MCDS",
            "optionality": "required",
            "type": "string",
            "units": None
        },
        "det_type_mode": {
            "ui_name": "Spectrograph, Imager, or Both",
            "option": "set",
            "allowed": ["Spectrograph", "Imager", "Both"],
            "default": "Spectrograph",
            "optionality": "required",
            "type": "string",
            "units": None
        },
        "target_info_object": {
            "default": "",
            "description": "Notes",
            "option": "open",
            "optionality": "optional",
            "type": "string",
            "ui_name": "Notes",
            "units": None
        },

    }
}

def generate_scripts():
    scripts = {}

    scripts['nires_acq'] = [
        ['BEGIN_SLEW', 'Starts telescope slew'],
        ['CONFIGURE_ACQUISITION', 'target parameters, guide camera parameters'],
        ['WAITFOR_CONFIGURE_ACQUISITION', ''],
        ['WAITFOR_SLEW', ''],
        ['ACQUIRE', 'OA acquires to PO'],
        ['WAITFOR_ACQUIRE', ''],
    ]

    scripts['nires_drift_scan_sci'] = [
        ['CONFIGURE_SCIENCE', ''],
        ['WAITFOR_CONFIGURE_SCIENCE', 'Waits until detector is ready'],
        ['EXECUTE_OBSERVATION', 'Point and shoot']
    ]
    scripts['nires_dither_sci'] = [
        ['CONFIGURE_SCIENCE', ''],
        ['WAITFOR_CONFIGURE_SCIENCE', 'Waits until detector is ready'],
        ['EXECUTE_OBSERVATION', 'Point and shoot']
    ]
    scripts['nires_stare_sci'] = [
        ['CONFIGURE_SCIENCE', ''],
        ['WAITFOR_CONFIGURE_SCIENCE', 'Waits until detector is ready'],
        ['EXECUTE_OBSERVATION', 'Point and shoot']
    ]

    scripts['nires_calibration'] = [
        ['CONFIGURE_SCIENCE', ''],
        ['WAITFOR_CONFIGURE_SCIENCE', 'Waits until detector is ready'],
        ['EXECUTE_OBSERVATION', 'Point and shoot']
    ]
    return scripts

def generate_recipes():
    recipes = {}


    recipes["calibration_dark"] = {
        "metadata": {
                "name": "calibration_dark",
                "ob_type": "calibration",
                "ui_name": "Darks Calibration",
                "instrument": "NIRES"
        },
        "recipe": [
            "nires_calibration"
        ],
        "ob_data": {
            "metadata": {
                "comment": "",
                "instrument": "NIRES",
                "name": "NIRES Calibration Darks",
                "ob_type": "Calibration",
                "tags": [ "calibration", "darks"],
                "version": "0.1.0"
            },
            "observations": [
                {
                    "metadata": {
                        "instrument": "NIRES",
                        "name": "nires_calibration",
                        "script": "nires_calibration",
                        "sequence_number": 1,
                        "template_type": "calibration",
                        "ui_name": "NIRES Calibration",
                        "version": "0.1.0"
                    },
                    "parameters": {
                        "det_cal_type": "Darks",
                        "det_coadd_number": 1,
                        "det_exp_number": 1,
                        "det_exp_read_pairs": 1,
                        "det_exp_time": 100,
                        "det_num_fs": 1,
                        "det_samp_mode": "MCDS"
                    }
                }
            ],
            "status": {
                "current_exp_det1": 0,
                "current_exp_det2": 0,
                "current_seq": 0,
                "current_step": 0,
                "deleted": False,
                "executions": [],
                "state": 0
            }
}

    }

    recipes["calibration_arcs"] = {
        "metadata": {
                "name": "calibration_arcs",
                "ob_type": "calibration",
                "ui_name": "Arcs Calibration",
                "instrument": "NIRES"
        },
        "recipe": [
            "nires_calibration"
        ],
        "ob_data":  {
            "metadata": {
                "comment": "",
                "instrument": "NIRES",
                "name": "NIRES Calibration Arcs",
                "ob_type": "Calibration",
                "tags": ["calibration", "arcs"],
                "version": "0.1.0"
            },
            "observations": [
                {
                "metadata": {
                    "instrument": "NIRES",
                    "name": "nires_calibration",
                    "script": "nires_calibration",
                    "sequence_number": 1,
                    "template_type": "calibration",
                    "ui_name": "NIRES Calibration",
                    "version": "0.1.0"
                },
                "parameters": {
                    "det_cal_type": "Arcs",
                    "det_coadd_number": 1,
                    "det_exp_number": 1,
                    "det_exp_read_pairs": 1,
                    "det_exp_time": 120,
                    "det_num_fs": 1,
                    "det_samp_mode": "MCDS"
                }
                }
            ],
            "status": {
                "current_exp_det1": 0,
                "current_exp_det2": 0,
                "current_seq": 0,
                "current_step": 0,
                "deleted": False,
                "executions": [],
                "state": 0
            }
            }
    }

    recipes["calibration_flats"] = {
        "metadata": {
                "name": "calibration_arcs",
                "ob_type": "calibration",
                "ui_name": "Flats Calibration",
                "instrument": "NIRES"
        },
        "recipe": [
            "nires_calibration"
        ],
        "ob_data": {
            "metadata": {
                "comment": "",
                "instrument": "NIRES",
                "name": "NIRES Calibration Flats",
                "ob_type": "Calibration",
                "tags": [ "calibration", "flats" ],
                "version": "0.1.0"
            },
            "observations": [
                {
                    "metadata": {
                        "instrument": "NIRES",
                        "name": "nires_calibration",
                        "script": "nires_calibration",
                        "sequence_number": 1,
                        "template_type": "calibration",
                        "ui_name": "NIRES Calibration",
                        "version": "0.1.0"
                    },
                    "parameters": {
                        "det_cal_type": "Flats",
                        "det_coadd_number": 1,
                        "det_exp_number": 1,
                        "det_exp_read_pairs": 1,
                        "det_exp_time": 100,
                        "det_num_fs": 1,
                        "det_samp_mode": "MCDS"
                    }
                }
            ],
            "status": {
                "current_exp_det1": 0,
                "current_exp_det2": 0,
                "current_seq": 0,
                "current_step": 0,
                "deleted": False,
                "executions": [],
                "state": 0
            }
        }

    }

    recipes["calibration_flatsonof"] = {
        "metadata": {
                "name": "calibration_arcs",
                "ob_type": "calibration",
                "ui_name": "Flats On and Off Calibration",
                "instrument": "NIRES"
        },
        "recipe": [
            "nires_calibration"
        ],
        "ob_data": {
            "metadata": {
                "comment": "",
                "instrument": "NIRES",
                "name": "NIRES Calibrations Flats on/off",
                "ob_type": "Calibration",
                "tags": [ "calibration", "flats on/off" ],
                "version": "0.1.0"
            },
            "observations": [
                {
                    "metadata": {
                        "instrument": "NIRES",
                        "name": "nires_calibration",
                        "script": "nires_calibration",
                        "sequence_number": 1,
                        "template_type": "calibration",
                        "ui_name": "NIRES Calibration",
                        "version": "0.1.0"
                    },
                    "parameters": {
                        "det_cal_type": "Flats On Flats Off",
                        "det_coadd_number": 1,
                        "det_exp_number": 1,
                        "det_exp_read_pairs": 1,
                        "det_exp_time": 100,
                        "det_num_fs": 1,
                        "det_samp_mode": "MCDS"
                    }
                }
            ],
            "status": {
                "current_exp_det1": 0,
                "current_exp_det2": 0,
                "current_seq": 0,
                "current_step": 0,
                "deleted": False,
                "executions": [],
                "state": 0
            }
        }


    }

    return recipes