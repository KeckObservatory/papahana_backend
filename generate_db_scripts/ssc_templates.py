ssc_acq_direct = {
    "metadata": {
        "instrument": "SSC",
        "name": "ssc_acq_direct",
        "script": "ssc_acq_direct",
        "script_version": "0.0.1",
        "sequence_number": 0,
        "template_type": "acquisition",
        "ui_name": "SSC direct",
        "version": "0.0.1"
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

ssc_common_parameters = {
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
        "version": "0.0.1"
    }
}


ssc_sci_image = {
    "metadata": {
        "instrument": "SSC",
        "name": "ssc_sci_image",
        "script": "ssc_sci_image",
        "script_version": "0.1.0",
        "sequence_number": 1,
        "template_type": "science",
        "ui_name": "SSC image",
        "version": "0.1.1"
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

ssc_sci_dither = {
    "metadata": {
        "instrument": "SSC",
        "name": "ssc_sci_dither",
        "script": "ssc_sci_dither",
        "script_version": "0.1.1",
        "sequence_number": 1,
        "template_type": "science",
        "ui_name": "SSC dither",
        "version": "0.1.1"
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



