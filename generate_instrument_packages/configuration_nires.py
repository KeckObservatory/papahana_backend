from common_template import dither_schema
"""
------------------------------- Scripts ----------------------------------------
"""

nires_acq_script = [
        ['BEGIN_SLEW', 'Starts telescope slew'],
        ['CONFIGURE_FOR_ACQUISITION', 'target parameters, guide camera parameters'],
        ['WAITFOR_CONFIGURE_ACQUISITION', ''],
        ['WAITFOR_SLEW', ''],
        ['ACQUIRE', 'OA acquires to PO'],
        ['WAITFOR_ACQUIRE', ''],
    ]

nires_sci_script = [
        ['CONFIGURE_SCIENCE', ''],
        ['WAITFOR_CONFIGURE_SCIENCE', 'Waits detector ready'],
        ['EXECUTE_OBSERVATION', ''],
        ['POST_OBSERVATION_CLEANUP', '']
    ]

"""
------------------------------- Recipes ----------------------------------------
"""


"""
------------------------------- Templates --------------------------------------
"""

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
        "det_exp_test": {
            "default": False,
            "description": "True prevents exposures from being taken",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Test Mode",
            "units": None
        }
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
            "option": "set",
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
        "sequence_ditarray": dither_schema,
        "det_exp_test": {
            "default": False,
            "description": "True prevents exposures from being taken",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Test Mode",
            "units": None
        }
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
        }
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
        "det_samp_mode": {
            "ui_name": "Sampling Mode",
            "option": "set",
            "allowed": ["MCDS", "PCDS", "UTR", "Single"],
            "default": "MCDS",
            "optionality": "optional",
            "type": "string",
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

