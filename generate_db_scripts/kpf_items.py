import generate_utils as utils
import generate_random_utils as random_utils
from papahana import util as papahana_util

def filled_common_parameters():
    schema = {
        "metadata": {
            "name": "kpf_common_parameters",
            "ui_name": "KPF Common Parameters",
            "instrument": "KPF",
            "template_type": "common_parameters",
            "version": "0.1.0"
        },
        "instrument_parameters": {
            "inst_cfg_runagitator": True
        },
        "detector_parameters": {
            "det1_cfg_trigger": True,
            "det2_cfg_trigger": True,
            "det3_cfg_trigger": True
        },
        "guider_parameters": {
        },
        "tcs_parameters": {
        }
    }
    return schema

def filled_cal_templates():
    cal_templates = [
        {
            "metadata": {
                "instrument": "KPF",
                "name": "kpf_arcs",
                "script": "kpf_arcs",
                "template_type": "calibration",
                "ui_name": "KPF Arc Lamps",
                "version": "0.1.0",
                "sequence_number": 0
            },
            "parameters": {
                "inst_cfg_nd1": "OD 0.1",
                "inst_cfg_nd2": "OD 0.3",
                "inst_cfg_calsource": "BrdbandFiber",
                "inst_cfg_fffiberpos": "Blank",
                "det_exp_time": random_utils.randFloat(3600),
                "det_exp_number": random_utils.randInt(1, 100),
                "target_info_object": 'arc',
                "inst_cfg_sss_science": True,
                "inst_cfg_sss_sky": True,
                "inst_cfg_simulcal_ts": True
            }
        }
    ]
    return cal_templates

def filled_acq_templates():
    acq_templates = [
        {
            "metadata": {
                "instrument": "KPF",
                "name": "kpf_acq",
                "script": "kpf_acq",
                "template_type": "acquisition",
                "ui_name": "KPF acquisition",
                "version": "0.1.0",
                "sequence_number": 0

            },
            "parameters": {
                "guider_cfg_gain": "high",
                "guider_cfg_fps": random_utils.randFloat(400.0),
                "guider_cfg_loopgain": random_utils.randFloat(1),
                "guider_mode": "manual",
                "tcs_coord_po": "KPF"
            }
        }
    ]
    return acq_templates


def filled_sci_templates(template_list):
    sci_templates = [
        {
            "metadata": {
                "instrument": "KPF",
                "name": "kpf_sci",
                "script": "kpf_sci",
                "template_type": "science",
                "ui_name": "KPF science",
                "version": "0.1.0"
            },
            "parameters": {
                "inst_cfg_nd1": "OD 0.1",
                "inst_cfg_nd2": "OD 0.1",
                "inst_cfg_calsource": "EtalonFiber",
                "inst_cfg_em_band": 1,
                "inst_cfg_em_exptime":  random_utils.randFloat(1800.0),
                "inst_cfg_em_flux": random_utils.randFloat(1000000000.0),
                "inst_cfg_em_mode": "manual",
                "det_exp_time": random_utils.randFloat(3600.0),
                "det_exp_number": random_utils.randInt(1, 100),
                "target_info_object": 'autocal-flat-sci',
                "inst_cfg_ts_simulcal": True
            }
        }
    ]
    return sci_templates


def generate_kpf_ip(template_list, rlist):

    schema = {
        "metadata": {
            "name": "kpf_instrument_package",
            "ui_name": "KPF Instrument Package",
            "version": "0.1.0",
            "instrument": "KPF",
            "observing_modes": ["spectroscopy"]
        },
        "optical_parameters": {
        },
        "configurable_elements": [
        ],
        "pointing_origins": ["KPF", "SKY", "EM_SKY", "REF"
        ],
        "template_list": utils.parse_templates_version(template_list),
        "recipe_list": rlist,
        "event_table": 'null',
        "comment": "A KPF Instrument Package"
    }

    return schema

def generate_inst_package(template_list, rlist, config, inst_list):
    print("...generating instrument package")

    # add templates
    if not template_list:
        coll_tmp = papahana_util.config_collection('templateCollect', conf=config)
        fields = {'metadata.name': 1, 'metadata.version': 1}
        template_list = list(coll_tmp.find({}, fields))

    # add recipes
    coll_recipe = papahana_util.config_collection('recipeCollect', conf=config)
    fields = {'metadata.name': 1, '_id': 0}
    recipe_list = list(coll_recipe.find({}, fields))

    coll = papahana_util.config_collection('ipCollect', conf=config)
    coll.drop()

    inst_specific_templates = utils.parse_template_list('KPF', inst_list, template_list)
    ip = generate_kpf_ip(inst_specific_templates, recipe_list)

    return ip

kpf_common_parameters_template = {
    "metadata": {
        "name": "kpf_common_parameters",
        "ui_name": "KPF Common Parameters",
        "instrument": "KPF",
        "template_type": "common_parameters",
        "version": "0.1.0"
    },
    "instrument_parameters": {
        "inst_cfg_runagitator": {
            "default": None,
            "description": "Run the agitator during exposures?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Agitator On",
            "units": None
        }
    },
    "detector_parameters": {
        "det1_cfg_trigger": {
            "default": None,
            "description": "Trigger the Ca H&K detector?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Ca H&K Detector Trigger",
            "units": None
        },
        "det2_cfg_trigger": {
            "default": None,
            "description": "Trigger the green detector?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Green Detector Trigger",
            "units": None
        },
        "det3_cfg_trigger": {
            "default": None,
            "description": "Use red detector?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Red Detector Trigger",
            "units": None
        }
    },
    "guider_parameters": {
    },
    "tcs_parameters": {
    }
}

kpf_science_template = {
    "metadata": {
        "instrument": "KPF",
        "name": "kpf_sci",
        "script": "kpf_sci",
        "template_type": "science",
        "ui_name": "KPF science",
        "version": "0.1.0"
    },
    "parameters": {

        "inst_cfg_nd1": {
            "allowed": [
                "OD 0.1",
                "OD 1.0",
                "OD 1.3",
                "OD 2.0",
                "OD 3.0",
                "OD 4.0"
            ],
            "default": None,
            "description": "Filter to use in the ND1 filter wheel",
            "option": "set",
            "optionality": "required",
            "type": "str",
            "ui_name": "ND1 Filter",
            "units": None
        },
        "inst_cfg_nd2": {
            "allowed": [
                "OD 0.1",
                "OD 0.3",
                "OD 0.5",
                "OD 0.8",
                "OD 1.0",
                "OD 4.0"
            ],
            "default": None,
            "description": "Filter to use in the ND2 filter wheel",
            "option": "set",
            "optionality": "required",
            "type": "str",
            "ui_name": "ND2 Filter",
            "units": None
        },
        "inst_cfg_calsource": {
            "allowed": [
                "Home",
                "EtalonFiber",
                "BrdbandFiber",
                "U_gold",
                "U_daily",
                "Th_daily",
                "Th_gold",
                "SoCal-CalFib",
                "LFCFiber"
            ],
            "default": None,
            "description": "Calibration source to use",
            "option": "set",
            "optionality": "required",
            "type": "str",
            "ui_name": "Calibration source",
            "units": None
        },
        "inst_cfg_em_band": {
            "allowed": [
                1,
                2,
                3,
                4
            ],
            "default": 1,
            "description": "Which wavelength band of the exposure meter to use for termination condition?",
            "option": "set",
            "optionality": "optional",
            "type": "integer",
            "ui_name": "Exposure Meter Wavelength Band",
            "units": None
        },
        "inst_cfg_em_exptime": {
            "allowed": [
                0.1,
                1800
            ],
            "default": None,
            "description": "Exposure time in seconds",
            "option": "range",
            "optionality": "required",
            "type": "float",
            "ui_name": "Exposure time in seconds",
            "units": "s"
        },
        "inst_cfg_em_flux": {
            "allowed": [
                1,
                1000000000.0
            ],
            "default": 100000.0,
            "description": "What flux value should trigger the exposure termination?",
            "option": "range",
            "optionality": "optional",
            "type": "float",
            "ui_name": "Termination flux",
            "units": "counts"
        },
        "inst_cfg_em_mode": {
            "allowed": [
                "off",
                "telescope",
                "manual",
                "auto"
            ],
            "default": "manual",
            "description": "off = do not take EM exposures, monitor = take EM exposures, but do not use for exposure termination, trigger = take EM exposures and use for exposure termination, auto = take EM exposures using automatic exposure time and use for exposure termination",
            "option": "set",
            "optionality": "required",
            "type": "str",
            "ui_name": "Exposure meter mode.",
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
        "inst_cfg_ts_simulcal": {
            "default": None,
            "description": "Should the timed shutter for simultaneous calibration fiber be opened during exposure?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Simultaneous Calibration fiber Timed Shutter Open",
            "units": None
        }
    }
}

kpf_acq_template = {
    "metadata": {
        "instrument": "KPF",
        "name": "kpf_acq",
        "script": "kpf_acq",
        "template_type": "acquisition",
        "ui_name": "KPF acquisition",
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
        "guider_cfg_fps": {
            "allowed": [
                0.01,
                400
            ],
            "description": "Only used if guide mode is manual",
            "option": "range",
            "optionality": "required",
            "type": "float",
            "ui_name": "Guider Rate",
            "units": "Hz"
        },
        "guider_cfg_loopgain": {
            "allowed": [
                0.01,
                1
            ],
            "description": "Tip tilt loop gain",
            "option": "range",
            "optionality": "required",
            "type": "float",
            "ui_name": "Tip tilt loop gain",
            "units": None
        },
        "guider_mode": {
            "allowed": [
                "off",
                "telescope",
                "manual",
                "auto"
            ],
            "description": "off = do not guide, telescope = use slow telescope guiding only, manual = use tip tilt with manually configured exposure parameters, auto = use tip tilt with automatically configured exposure parameters",
            "option": "set",
            "optionality": "required",
            "type": "string",
            "ui_name": "Guide camera exposure mode.",
            "units": None
        },
        "tcs_coord_po": {
            "allowed": [
                "KPF",
                "SKY",
                "EM_SKY",
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

kpf_arc_template = {
    "metadata": {
        "instrument": "KPF",
        "name": "kpf_arcs",
        "script": "kpf_arcs",
        "template_type": "calibration",
        "ui_name": "KPF Arc Lamps",
        "version": "0.1.0",
        "sequence_number": 0
    },
    "parameters": {
        "inst_cfg_nd1": {
            "allowed": [
                "OD 0.1",
                "OD 1.0",
                "OD 1.3",
                "OD 2.0",
                "OD 3.0",
                "OD 4.0"
            ],
            "default": None,
            "description": "Filter to use in the ND1 filter wheel",
            "option": "set",
            "optionality": "required",
            "type": "string",
            "ui_name": "ND1 Filter",
            "units": None
        },
        "inst_cfg_nd2": {
            "allowed": [
                "OD 0.1",
                "OD 0.3",
                "OD 0.5",
                "OD 0.8",
                "OD 1.0",
                "OD 4.0"
            ],
            "default": None,
            "description": "Filter to use in the ND2 filter wheel",
            "option": "set",
            "optionality": "required",
            "type": "string",
            "ui_name": "ND2 Filter",
            "units": None
        },
        "inst_cfg_calsource": {
            "allowed": [
                "Home",
                "EtalonFiber",
                "BrdbandFiber",
                "U_gold",
                "U_daily",
                "Th_daily",
                "Th_gold",
                "SoCal-CalFib",
                "LFCFiber"
            ],
            "default": None,
            "description": "Calibration source to use",
            "option": "set",
            "optionality": "required",
            "type": "string",
            "ui_name": "Calibration source",
            "units": None
        },
        "inst_cfg_fffiberpos": {
            "allowed": [
                "Blank",
                "6 mm f/5",
                "7.5 mm f/4",
                "10 mm f/3",
                "13.2 mm f/2.3",
                "Open"
            ],
            "default": "Open",
            "description": "Flat field aperture choice.",
            "option": "set",
            "optionality": "optional",
            "type": "string",
            "ui_name": "Flat field aperture choice.",
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
        "inst_cfg_sss_science": {
            "default": None,
            "description": "Should the source select shutter for science be open?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Source Shutter Open",
            "units": None
        },
        "inst_cfg_sss_sky": {
            "default": None,
            "description": "Should the source select shutter for sky be open?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Sky Shutter Open",
            "units": None
        },
        "inst_cfg_simulcal_ts": {
            "default": None,
            "description": "Should the timed shutter for simultaneous calibration fiber be opened during exposure?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Simultaneous Calibration Fiber Timed Shutter Open",
            "units": None
        },
    }
}

kpf_darks_template = {
    "metadata": {
        "instrument": "KPF",
        "name": "kpf_dark",
        "script": "kpf_dark",
        "template_type": "calibration",
        "ui_name": "KPF Dark Sequence",
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

kpf_target_template = {
    "metadata": {
        "instrument": "KPF",
        "name": "kpf_target",
        "template_type": "target",
        "ui_name": "KPF Target",
        "version": "0.1.0"
    },
    "parameters": {
        "target_info_name": {
            "default": None,
            "description": "observer provided name",
            "optionality": "required",
            "type": "string",
            "ui_name": "Target Name",
            "units": None
        },
        "target_info_comment": {
            "ui_name": "Target Comment",
            "option": "optional",
            "default": "",
            "optionality": "optional",
            "type": "string",
            "units": None
        },
        "target_info_2mass_id": {
            "default": None,
            "description": "The 2MASS ID of the target",
            "optionality": "required",
            "type": "string",
            "ui_name": "2MASS ID",
            "units": None
        },
        "target_info_gaia_id": {
            "default": None,
            "description": "The GAIA DR3 ID of the target",
            "optionality": "required",
            "type": "string",
            "ui_name": "GAIA DR3 ID",
            "units": None
        },
        "target_info_gmag": {
            "allowed": [
                -30,
                30
            ],
            "default": None,
            "description": "Gaia G magnitude of target",
            "option": "range",
            "optionality": "required",
            "type": "float",
            "ui_name": "Gaia G",
            "units": "magnitude"
        },
        "target_info_jmag": {
            "allowed": [
                -30,
                30
            ],
            "default": None,
            "description": "2MASS J magnitude of target",
            "option": "range",
            "optionality": "required",
            "type": "float",
            "ui_name": "2MASS J",
            "units": "magnitude"
        },
        "target_coord_parallax": {
            "allowed": [
                0,
                1000000.0
            ],
            "default": None,
            "description": "Parallax in milliarcseconds; needed for DRP not pointing telescope",
            "option": "range",
            "optionality": "required",
            "type": "float",
            "ui_name": "Parallax",
            "units": "mas"
        },
        "target_info_rv": {
            "allowed": [
                -1000000.0,
                1000000.0
            ],
            "default": None,
            "description": "Radial velocity in km/s; needed for DRP",
            "option": "range",
            "optionality": "required",
            "type": "float",
            "ui_name": "Radial velocity",
            "units": "km/s"
        },
        "target_info_teff": {
            "allowed": [
                0,
                1000000.0
            ],
            "default": None,
            "description": "Teff of target in K",
            "option": "range",
            "optionality": "required",
            "type": "float",
            "ui_name": "Effective Temperature",
            "units": "K"
        },
        "target_coord_ra": {
            "ui_name": "Right Ascension",
            "option": "regex",
            "allowed": [
                "^\\d{2}:\\d{2}:\\d{2}$",
                "^\\d{2}:\\d{2}:\\d{2}.\\d{1}$",
                "^\\d{2}:\\d{2}:\\d{2}.\\d{2}$"
            ],
            "default": None,
            "optionality": "required",
            "type": "string",
            "units": "Hours:Minutes:Seconds"
        },
        "target_coord_dec": {
            "ui_name": "Declination",
            "option": "regex",
            "allowed": [
                "^\\d{2}:\\d{2}:\\d{2}$",
                "^\\d{2}:\\d{2}:\\d{2}.\\d{1}$",
                "^\\d{2}:\\d{2}:\\d{2}.\\d{2}$",
                "^-\\d{2}:\\d{2}:\\d{2}$",
                "^-\\d{2}:\\d{2}:\\d{2}.\\d{1}$",
                "^-\\d{2}:\\d{2}:\\d{2}.\\d{2}$"
            ],
            "default": None,
            "optionality": "required",
            "type": "string",
            "units": "Degrees:Minutes:Seconds"
        },
        "target_coord_pm_ra": {
            "ui_name": "Proper Motion (RA)",
            "option": "range",
            "allowed": [
                0,
                5000
            ],
            "default": 0,
            "optionality": "optional",
            "type": "float",
            "units": "arcseconds/yr"
        },
        "target_coord_pm_dec": {
            "ui_name": "Proper Motion (DEC)",
            "option": "range",
            "allowed": [
                0,
                100
            ],
            "default": 0,
            "optionality": "optional",
            "type": "float",
            "units": "arcseconds/yr"
        },
        "target_coord_frame": {
            "ui_name": "Frame",
            "option": "set",
            "allowed": [
                "mount",
                "FK5"
            ],
            "default": "FK5",
            "optionality": "optional",
            "type": "string",
            "units": None
        },
        "target_coord_epoch": {
            "ui_name": "Epoch",
            "option": "range",
            "allowed": [
                1900,
                2100
            ],
            "default": "FK5",
            "optionality": "optional",
            "type": "float",
            "units": "year"
        },
        "rot_cfg_pa": {
            "ui_name": "Position Angle",
            "option": "range",
            "allowed": [
                0,
                360
            ],
            "default": 0,
            "optionality": "optional",
            "type": "float",
            "units": "Degrees"
        },
        "seq_constraint_obstime": {
            "ui_name": "Scheduled Time of Observation",
            "option": "regex",
            "allowed": [
                None,
                "^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}$"
            ],
            "default": None,
            "optionality": "optional",
            "type": "string",
            "units": "YR-MM-DD hh:mm:ss"
        }
    }
}





def generate_scripts():
    scripts = {}

    scripts['kpf_acq'] = [
        ['BEGIN_SLEW', 'Starts telescope slew'],
        ['CONFIGURE_FOR_ACQUISITION', 'Sets: octagon, (does slew cal), FIU mode, target parameters, guide camera parameters'],
        ['WAITFOR_CONFIGURE_ACQUISITION', 'Waits for FIU mode'],
        ['WAITFOR_SLEW', ''],
        ['ACQUIRE', 'OA acquires to PO'],
        ['WAITFOR_ACQUIRE', ''],
    ]

    scripts['kpf_sci'] = [
        ['CONFIGURE_SCIENCE', 'Sets CURRENT_BASE, Turns on Tip Tilt, then Sets: octagon (should not move), source select shutters, triggered detectors'],
        ['WAITFOR_CONFIGURE_SCIENCE', 'Waits for FIU mode, octagon, detector ready'],
        ['EXECUTE_OBSERVATION', ''],
        ['POST_OBSERVATION_CLEANUP', '']
    ]
    return scripts


def generate_recipes():
    recipes = {}

    recipes["science_sidereal_target"] = {
        "metadata": {
                "name": "science_sidereal_target",
                "ob_type": "science",
                "ui_name": "Sidereal Science Target",
                "instrument": "KPF"
        },
        "recipe": [
            "kpf_common_parameters",
            "kpf_acq",
            "kpf_sci",
            "sideriel_target"
        ]
    }

    recipes["science_non_sidereal_target"] = {
        "metadata": {
                "name": "science_non_sidereal_target",
                "ob_type": "science",
                "ui_name": "Non Sidereal Science Target",
                "instrument": "KPF"
        },
        "recipe": [
            "kpf_common_parameters",
            "kpf_acq",
            "kpf_sci",
            "non_sideriel_target"
        ]
    }

    recipes["science_kpf_target"] = {
        "metadata": {
                "name": "science_kpf_target",
                "ob_type": "science",
                "ui_name": "KPF Science Target",
                "instrument": "KPF"
        },
        "recipe": [
            "kpf_common_parameters",
            "kpf_acq",
            "kpf_sci",
            "kpf_target"
        ]
    }

    recipes["calibration_dark"] = {
        "metadata": {
                "name": "calibration_dark",
                "ob_type": "calibration",
                "ui_name": "Dark Calibration",
                "instrument": "KPF"
        },
        "recipe": [
            "kpf_common_parameters",
            "kpf_dark"
        ]
    }

    recipes["calibration_arcs"] = {
        "metadata": {
                "name": "calibration_arcs",
                "ob_type": "calibration",
                "ui_name": "Arc Calibration",
                "instrument": "KPF"
        },
        "recipe": [
            "kpf_common_parameters",
            "kpf_arcs"
        ]
    }

    return recipes