import argparse

import generate_utils as utils
from papahana import util as papahana_util
from copy import deepcopy
from collections import OrderedDict


# Target Templates
# target_base_keys = ['target_info_name', 'target_coord_ra']

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
        "version": "0.1.1"
    }),
    ("parameters", target_base_parameters)
])


nonsidereal_target = OrderedDict([
    ("metadata", {
        "name": "non_sidereal_target",
        "ui_name": "Non-Sidereal Target",
        "template_type": "target",
        "version": "0.1.1"
    }),
    ("parameters", nonsidereal_extra_params)
])


mos_target = OrderedDict([
    ("metadata", {
        "name": "multi_object_target",
        "ui_name": "Multi-Object Spectroscopy Target",
        "template_type": "target",
        "version": "0.1.1"
    }),
    ("parameters", mos_extra_params)
])

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

dither_schema = {
    "ui_name": "Dither Pattern",
    "option": "set",
    "default": None,
    "optionality": "required",
    "type": "array",
    "allowed": [
        {"seq_dither_ra_offset": {
            "ui_name": "Right Ascension Offset",
            "option": "range",
            "allowed": [-20.0, 20.0],
            "default": None,
            "optionality": "required",
            "type": "float",
            "units": "arcseconds"
        }},
        {"seq_dither_dec_offset": {
            "ui_name": "Declination Offset",
            "option": "range",
            "allowed": [-20.0, 20.0],
            "default": None,
            "optionality": "required",
            "type": "float",
            "units": "arcseconds"
        }},
        {"seq_dither_position": {
            "ui_name": "Telescope Position",
            "option": "set",
            "allowed": ["T", "S", "O"],
            "default": None,
            "optionality": "required",
            "type": "string",
            "units": None
        }},
        {"telescope_guided": {
            "ui_name": "Guided",
            "option": "boolean",
            "default": True,
            "optionality": "required",
            "type": "boolean",
            "units": None
        }}
    ]
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

#TODO: Fill with separate template
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
        "det1_cfg_exptime": {
            "ui_name": "Blue exposure time for individual exposures",
            "allowed": [0.0, 3600.0],
            "option": "range",
            "optionality": "required",
            "default": None,
            "type": "float",
            "units": None
        }
    },
    "tcs_parameters": {}
}


kpf_common_parameters = {
    "metadata": {
        "name": "kpf_common_parameters",
        "ui_name": "KPF Common Parameters",
        "instrument": "KPF",
        "template_type": "common_parameters",
        "version": "0.1.1"
    },
    "instrument_parameters": {
        "inst_cfg_simulcal_source": {
            "ui_name": "Simultaneous Cal Fiber Source",
            "description": "Source to illuminate the simultaneous cal fiber (i.e. octagon position)",
            "option": "set",
            "allowed": [
            ],
            "default": None,
            "optionality": "required",
            "type": "string",
            "units": None
        },
        "inst_cfg_simulcal_autofilter": {
            "ui_name": "Simultaneous Cal Fiber Filter",
            "description": "System should automatically set ND filters for cal source?",
            "option": "boolean",
            "default": None,
            "optionality": "required",
            "type": "boolean",
            "units": None
        },
        "inst_cfg_simulcal_nd1": {
            "ui_name": "Simultaneous Cal Fiber ND Filter 1",
            "description": "ND filter in first filter wheel if inst_cfg_simulcal_autofilter is not True",
            "option": "set",
            "allowed": ['ND0.1', 'ND0.2', 'ND0.3', 'ND0.4', 'ND0.5'],
            "default": "ND0.1",
            "optionality": "optional",
            "type": "string",
            "units": None
        },
        "inst_cfg_simulcal_nd2": {
            "ui_name": "Simultaneous Cal Fiber ND Filter 1",
            "description": "ND filter in second filter wheel if inst_cfg_simulcal_autofilter is not True",
            "option": "set",
            "allowed": ['ND0.1', 'ND0.2', 'ND0.3', 'ND0.4', 'ND0.5'],
            "default": "ND0.1",
            "optionality": "optional",
            "type": "string",
            "units": None
        },
        "inst_cfg_sss_sky": {
            "ui_name": "Source Select Shutter Sky",
            "description": "Should the source select shutter for sky be open?",
            "option": "boolean",
            "default": None,
            "optionality": "required",
            "type": "boolean",
            "units": None
        },
        "inst_cfg_sss_sci": {
            "ui_name": "Source Select Shutter Science",
            "description": "Should the source select shutter for science be open?",
            "option": "boolean",
            "default": None,
            "optionality": "required",
            "type": "boolean",
            "units": None
        },
        "inst_cfg_sss_socal_sci": {
            "ui_name": "Source Select Shutter SoCal Science",
            "description": "Should the source select shutter for SoCal science be open?",
            "option": "boolean",
            "default": None,
            "optionality": "required",
            "type": "boolean",
            "units": None
        },
        "inst_cfg_sss_socal_cal": {
            "ui_name": "Source Select Shutter SoCal Calibration",
            "description": "Should the source select shutter for SoCal cal be open?",
            "option": "boolean",
            "default": None,
            "optionality": "required",
            "type": "boolean",
            "units": None
        }
    },
    "guider_parameters": {
        "guider1_cfg_mode": {
            "ui_name": "Guide Camera Mode",
            "option": "set",
            "allowed": [
                "auto",
                "manual",
                "off"
            ],
            "default": None,
            "optionality": "required",
            "type": "string",
            "units": None
        },
        "guider1_cfg_framerate": {
            "ui_name": "Guide Camera Frame Rate",
            "description": "If guide_cfg_mode is manual, frame rate for camera",
            "option": "range",
            "allowed": [
                1,
                400
            ],
            "default": 100,
            "optionality": "optional",
            "type": "int",
            "units": "Hz"
        },
        "guider1_cfg_camgain": {
            "ui_name": "Guide Camera Gain",
            "description": "If guide_cfg_mode is manual, gain for camera",
            "option": "set",
            "allowed": [
                "high",
                "medium",
                "low"
            ],
            "default": "high",
            "optionality": "optional",
            "type": "string",
            "units": None
        },
        "guider1_cfg_exptime": {
            "ui_name": "Guide Camera Exposure Time",
            "description": "If guide_cfg_mode is manual, exposure time for camera",
            "option": "range",
            "allowed": [
                1e-6,
                1
            ],
            "default": None,
            "optionality": "optional",
            "type": "float",
            "units": "seconds"
        },
        "guider1_cfg_loopgain": {
            "ui_name": "Guide Camera Loop Gain",
            "description": "If guide_cfg_mode is manual, tip tilt loop gain",
            "option": "range",
            "allowed": [
                0,
                1
            ],
            "default": None,
            "optionality": "optional",
            "type": "float",
            "units": None,
        },
        "guider1_cfg_xwindow": {
            "ui_name": "Guide Camera X-Window Size",
            "description": "Size of the guide window in X pixels",
            "option": "range",
            "allowed": [
                0,
                640
            ],
            "default": 64,
            "optionality": "optional",
            "type": "int",
            "units": 'pixels',
        },
        "guider1_cfg_ywindow": {
            "ui_name": "Guide Camera Y-Window Size",
            "description": "Size of the guide window in Y pixels",
            "option": "range",
            "allowed": [
                0,
                640
            ],
            "default": 64,
            "optionality": "optional",
            "type": "int",
            "units": 'pixels',
        },
        "guider1_cfg_raoffset": {
            "ui_name": "Guider RA Offset",
            "description": "Offset distance in RA from the guide star to science target",
            "option": "range",
            "allowed": [
                0,
                20
            ],
            "default": None,
            "optionality": "required",
            "type": "float",
            "units": "arcseconds",
        },
        "guider1_cfg_decoffset": {
            "ui_name": "Guider RA Offset",
            "description": "Offset distance in Dec from the guide star to science target",
            "option": "range",
            "allowed": [
                0,
                20
            ],
            "default": None,
            "optionality": "required",
            "type": "float",
            "units": "arcseconds",
        },
    },
    "detector parameters": {},
    "tcs_parameters": {}
}


kpf_sci_stare = {
    "metadata": {
        "name": "kpf_sci_stare",
        "ui_name": "kpf stare observation",
        "instrument": "KPF",
        "template_type": "science",
        "version": "0.1.1",
        "script": "kpf_sci_stare",
        "script_version": "0.1.0",
        "sequence_number": 1
    },
    "parameters": {
        "target_info_spectraltype": {
            "ui_name": "Spectral Type",
            "description": "The spectral type of target.  used by drp and possibly by automatic guide parameters",
            "option": "set",
            "allowed": ["O", "B", "A", "F", "G", "K", "M"],
            "default": None,
            "optionality": "required",
            "type": "string",
            "units": None
        },
        "inst_cfg_nexp": {
            "ui_name": "Number of Exposures",
            "description": "The number of exposures to take.",
            "option": "range",
            "allowed": [1, 100],
            "default": None,
            "optionality": "required",
            "type": "int",
            "units": None
        },
        "inst_cfg_exptime": {
            "ui_name": "Exposure Time",
            "description": "The exposure time of an individual science exposure.",
            "option": "range",
            "allowed": [1, 3600],
            "default": None,
            "optionality": "required",
            "type": "float",
            "units": "seconds"
        },
        "inst_cfg_trigger_cahk": {
            "ui_name": "CA H&K Detector On",
            "description": "Trigger the ca h&k detector?",
            "option": "boolean",
            "default": None,
            "optionality": "required",
            "type": "boolean",
            "units": None
        },
        "inst_cfg_trigger_green": {
            "ui_name": "Green Detector On",
            "description": "Trigger the green detector?",
            "option": "boolean",
            "default": None,
            "optionality": "required",
            "type": "boolean",
            "units": None
        },
        "inst_cfg_trigger_red": {
            "ui_name": "Red Detector On",
            "description": "Trigger the red detector?",
            "option": "boolean",
            "default": None,
            "optionality": "required",
            "type": "boolean",
            "units": None
        },
        "inst_cfg_expmeter_active": {
            "ui_name": "Use Exposure Meter",
            "description": "Use the exposure meter to end the exposure?",
            "option": "boolean",
            "default": None,
            "optionality": "optional",
            "type": "boolean",
            "units": None
        },
        "inst_cfg_expmeter_flux": {
            "ui_name": "Flux Level",
            "description": "The flux level on exposure meter at which to end exposure.",
            "option": "range",
            "allowed": [1, 1e8],
            "default": 1e6,
            "optionality": "optional",
            "type": "float",
            "units": None
        },
    }
}


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


def generate_kcwi_templates(coll):

    templates = [kcwi_ifu_acq_offsetStar_template,
                 kcwi_ifu_acq_direct_template,
                 kcwi_ifu_sci_stare_template,
                 kcwi_ifu_sci_dither_template,
                 sidereal_target,
                 nonsidereal_target,
                 mos_target, kcwi_common_parameters]

    result = coll.insert_many(templates, ordered=False, bypass_document_validation=True)

    fields = {'metadata.name': 1, 'metadata.version': 1}
    doc = list(coll.find({}, fields))

    return doc


def generate_templates(config):
    coll = papahana_util.config_collection('templateCollect', conf=config)

    coll.drop()
    print('...adding templates to collection')

    # add kcwi

    templates_kcwi = [
        kcwi_ifu_acq_offsetStar_template,
        kcwi_ifu_acq_direct_template,
        kcwi_ifu_sci_stare_template,
        kcwi_ifu_sci_dither_template]
    templates_targets = [
        sidereal_target,
        nonsidereal_target,
        mos_target,
        kcwi_common_parameters
    ]
    templates_kpf = [kpf_common_parameters, kpf_sci_stare]

    templates = []

    templates += templates_kpf
    templates += templates_kcwi
    templates += templates_targets

    result = coll.insert_many(templates, ordered=False, bypass_document_validation=True)

    fields = {'metadata.name': 1, 'metadata.version': 1}
    doc = list(coll.find({}, fields))

    return doc
