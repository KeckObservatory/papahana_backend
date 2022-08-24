from copy import deepcopy
from common_template import dither_schema

# Acquisition Templates
kcwi_acq_direct_template_parameters = {
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
    "tcs_coord_po": {
        "ui_name": "Pointing origin",
        "option": "set",
        "allowed": ["REF", "IFU"],
        "default": None,
        "optionality": "required",
        "type": "string",
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
    }
}

kcwi_ifu_sci_dither_parameters = {

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

kcwi_ifu_sci_stare_parameters = {
    "det1_exp_time": {
        "ui_name": "Blue exposure time for individual exposures",
        "option": "range",
        "allowed": [0.0, 3600.0],
        "default": None,
        "optionality": "required",
        "type": "float",
        "units": "seconds"
    },
    "det1_exp_number": {
        "ui_name": "Blue number of exposures per dither position",
        "option": "range",
        "allowed": [0.0, 100.0],
        "default": None,
        "optionality": "required",
        "type": "integer",
        "units": None
    },
    "det2_exp_time": {
        "ui_name": "Red exposure time for individual exposures",
        "option": "range",
        "allowed": [0.0, 3600.0],
        "default": None,
        "optionality": "optional",
        "type": "float",
        "units": "seconds"
    },
    "det2_exp_number": {
        "ui_name": "Red number of exposures per dither position",
        "option": "range",
        "allowed": [0, 100],
        "default": None,
        "optionality": "optional",
        "type": "integer",
        "units": None
    }
}

kcwi_ifu_sci_dither_template = {
    "metadata": {
        "name": "kcwi_ifu_sci_dither",
        "ui_name": "KCWI dither",
        "instrument": "KCWI",
        "template_type": "science",
        "version": "0.1.1",
        "script": "kcwi_ifu_sci_stare",
        "script_version": "0.1.1",
        "sequence_number": 1
    },
    "parameters": dict(list(kcwi_ifu_sci_stare_parameters.items()) +
                        list(kcwi_ifu_sci_dither_parameters.items()))

}


kcwi_ifu_sci_stare_template = {
    "metadata": {
        "name": "kcwi_ifu_sci_stare",
        "ui_name": "KCWI stare",
        "instrument": "KCWI",
        "template_type": "science",
        "version": "0.1.1",
        "script": "kcwi_ifu_sci_stare",
        "script_version": "0.1.0",
        "sequence_number": 1
    },
    "parameters": kcwi_ifu_sci_stare_parameters
}

kcwi_ifu_acq_direct_template = {
    "metadata": {
        "name": "kcwi_ifu_acq_direct",
        "ui_name": "KCWI direct",
        "instrument": "KCWI",
        "template_type": "acquisition",
        "version": "0.1.1",
        "script": "kcwi_ifu_acq_direct",
        "script_version": "0.1.0",
        "sequence_number": 0

    },
    "parameters": kcwi_acq_direct_template_parameters
}

kcwi_ifu_acq_offsetStar_template = deepcopy(kcwi_ifu_acq_direct_template)
kcwi_ifu_acq_offsetStar_template['metadata']['name'] = 'kcwi_ifu_acq_offsetStar'

kcwi_common_parameters = {
    "metadata": {
        "name": "kcwi_common_parameters",
        "ui_name": "KCWI Common Parameters",
        "template_type": "common_parameters",
        "instrument": "KCWI",
        "version": "0.1.0"
    },
    "instrument_parameters": {
        "inst_cfg_hatch": {
            "ui_name": "Hatch Position",
            "option": "set",
            "allowed": ["open", "closed"],
            "default": "open",
            "optionality": "optional",
            "type": "string",
            "units": None
        },
        "inst_cfg_slicer": {
            "ui_name": "Image slicer selection",
            "allowed": ["Large", "Medium", "Small", "FPCam", "Aux"],
            "option": "set",
            "optionality": "required",
            "default": None,
            "type": "string",
            "units": None
        },
        "inst_cfg1_grating": {
            "ui_name": "Grating selection",
            "allowed": ["BL", "BM", "BH1", "BH2", "BH3", "None"],
            "option": "set",
            "optionality": "required",
            "default": None,
            "type": "string",
            "units": None
        },
        "inst_wavelength1_cwave": {
            "ui_name": "Central wavelength",
            "allowed": [3500, 5600],
            "option": "range",
            "optionality": "optional",
            "default": 4500,
            "type": "float",
            "units": "Angstroms"
        },
        "inst_wavelength1_pwave": {
            "ui_name": "Peak efficiency wavelength",
            "allowed": [3500, 5600],
            "option": "range",
            "optionality": "optional",
            "default": 4500,
            "type": "float",
            "units": "Angstroms"
        },
        "inst_cfg1_nasmask": {
            "ui_name": "Nod and Shuffle mask",
            "allowed": ["Mask", "None"],
            "range": None,
            "option": "set",
            "optionality": "required",
            "default": "None",
            "type": "string",
            "units": None
        },
        "inst_cfg1_filter": {
            "ui_name": "Blue filter",
            "allowed": ["Kblue", "None"],
            "option": "set",
            "optionality": "optional",
            "default": "Kblue",
            "type": "string",
            "units": None
        },
        "inst_cfg_polarizer": {
            "ui_name": "Linear polarizer",
            "allowed": ["Sky", "Polar", "Lens"],
            "option": "set",
            "optionality": "required",
            "default": "Sky",
            "type": "string",
            "units": None
        },
        "inst_cfg_polangle": {
            "ui_name": "Polarizer angle",
            "allowed": [0, 360],
            "option": "range",
            "optionality": "required",
            "default": None,
            "type": "float",
            "units": "Degrees"
        },
        "inst_mode_kmirror": {
            "ui_name": "K-Mirror Mode",
            "option": "set",
            "allowed": ["Tracking", "Stationary"],
            "default": None,
            "optionality": "required",
            "type": "string",
            "units": None
        },
        "inst_cfg_kmirrorangle": {
            "ui_name": "K-Mirror Angle",
            "option": "range",
            "allowed": [0, 360],
            "default": None,
            "optionality": "required",
            "type": "float",
            "units": None
        }
    },
    "detector_parameters": {
        "det1_mode_ccdspeed": {
            "ui_name": "Blue CCDMODE 0 (slow) or 1 (fast)",
            "allowed": [0, 1],
            "option": "set",
            "optionality": "optional",
            "default": 0,
            "type": "integer",
            "units": None
        },
        "det1_mode_ampmode": {
            "ui_name": "Blue AMPMODE  0(quad, ALL)), 1 (single C)), 2 (single E)), 3 (single D)), 4 (single F)), 5 (single B)), 6 (single G)), 7 (single A)), 8 (single H)), 9 (dual A&B)), 10 (dual C&D)",
            "allowed": [0, 10],
            "option": "range",
            "optionality": "optional",
            "default": 9,
            "type": "integer",
            "units": None
        },
        "det1_mode_gain": {
            "ui_name": "Blue-Side CCD Gain Multiplier",
            "option": "set",
            "allowed": [1, 2, 5, 10],
            "default": None,
            "optionality": "required",
            "type": "integer",
            "units": None
        },
        "det1_cfg_binning": {
            "ui_name": "Blue binning 1,1 or 2,2",
            "allowed": ["1,1", "2,2"],
            "option": "set",
            "optionality": "required",
            "default": None,
            "type": "string",
            "units": None
        },
    },
    "tcs_parameters": {}
}
