

kpf_common_parameters = {
    "metadata": {
        "name": "kpf_common_parameters",
        "ui_name": "KPF Common Parameters",
        "instrument": "KPF",
        "template_type": "common_parameters",
        "version": "0.1.1"
    },
    "instrument_parameters": {
        "inst_cfg_runagitator": {
            "default": 'null',
            "description": "Run the agitator during exposures?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Agitator On",
            "units": 'null'
        }
    },
    "detector_parameters": {
        "det1_cfg_trigger": {
            "default": 'null',
            "description": "Trigger the Ca H&K detector?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Ca H&K Detector Trigger",
            "units": 'null'
        },
        "det2_cfg_trigger": {
            "default": 'null',
            "description": "Trigger the green detector?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Green Detector Trigger",
            "units": 'null'
        },
        "det3_cfg_trigger": {
            "default": 'null',
            "description": "Use red detector?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Red Detector Trigger",
            "units": 'null'
        }
    },
    "guider_parameters": {
    },
    "tcs_parameters": {
    }
}

kpf_science = {
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
            "default": 'null',
            "description": "Filter to use in the ND1 filter wheel",
            "option": "set",
            "optionality": "required",
            "type": "str",
            "ui_name": "ND1 Filter",
            "units": 'null'
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
            "default": 'null',
            "description": "Filter to use in the ND2 filter wheel",
            "option": "set",
            "optionality": "required",
            "type": "str",
            "ui_name": "ND2 Filter",
            "units": 'null'
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
            "default": 'null',
            "description": "Calibration source to use",
            "option": "set",
            "optionality": "required",
            "type": "str",
            "ui_name": "Calibration source",
            "units": 'null'
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
            "units": 'null'
        },
        "inst_cfg_em_exptime": {
            "allowed": [
                0.1,
                1800
            ],
            "default": 'null',
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
            "units": 'null'
        },
        "det_exp_time": {
            "allowed": [
                0.1,
                3600
            ],
            "default": 'null',
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
            "default": 'null',
            "description": "Number of exposures to take",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Exposures",
            "units": 'null'
        },
        "target_info_object": {
            "default": "",
            "description": "Value for the object keyword",
            "option": "open",
            "optionality": "optional",
            "type": "string",
            "ui_name": "Object Keyword",
            "units": 'null'
        },
        "inst_cfg_ts_simulcal": {
            "default": 'null',
            "description": "Should the timed shutter for simultaneous calibration fiber be opened during exposure?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Simultaneous Calibration fiber Timed Shutter Open",
            "units": 'null'
        }
    }
}

kpf_acq = {
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
            "units": 'null'
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
            "units": 'null'
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
            "units": 'null'
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
            "units": 'null'
        }
    }
}

kpf_arc = {
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
            "default": 'null',
            "description": "Filter to use in the ND1 filter wheel",
            "option": "set",
            "optionality": "required",
            "type": "string",
            "ui_name": "ND1 Filter",
            "units": 'null'
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
            "default": 'null',
            "description": "Filter to use in the ND2 filter wheel",
            "option": "set",
            "optionality": "required",
            "type": "string",
            "ui_name": "ND2 Filter",
            "units": 'null'
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
            "default": 'null',
            "description": "Calibration source to use",
            "option": "set",
            "optionality": "required",
            "type": "string",
            "ui_name": "Calibration source",
            "units": 'null'
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
            "units": 'null'
        },
        "det_exp_time": {
            "allowed": [
                0.1,
                3600
            ],
            "default": 'null',
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
            "default": 'null',
            "description": "Number of exposures to take",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of exposures to take",
            "units": 'null'
        },
        "target_info_object": {
            "default": "",
            "description": "Value for the object keyword",
            "option": "open",
            "optionality": "optional",
            "type": "string",
            "ui_name": "Value for the object keyword",
            "units": 'null'
        },
        "inst_cfg_sss_science": {
            "default": 'null',
            "description": "Should the source select shutter for science be open?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Source Shutter Open",
            "units": 'null'
        },
        "inst_cfg_sss_sky": {
            "default": 'null',
            "description": "Should the source select shutter for sky be open?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Sky Shutter Open",
            "units": 'null'
        },
        "inst_cfg_simulcal_ts": {
            "default": 'null',
            "description": "Should the timed shutter for simultaneous calibration fiber be opened during exposure?",
            "option": "boolean",
            "optionality": "required",
            "type": "boolean",
            "ui_name": "Simultaneous Calibration Fiber Timed Shutter Open",
            "units": 'null'
        },
    }
}

kpf_darks = {
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
            "default": 'null',
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
            "default": 'null',
            "description": "Number of exposures to take",
            "option": "range",
            "optionality": "required",
            "type": "integer",
            "ui_name": "Number of Exposures",
            "units": 'null'
        },
        "target_info_object": {
            "default": "",
            "description": "Value for the object keyword",
            "option": "open",
            "optionality": "optional",
            "type": "string",
            "ui_name": "Object Keyword",
            "units": 'null'
        },
    }
}

kpf_target = {
    "metadata": {
        "instrument": "KPF",
        "name": "kpf_target",
        "template_type": "target",
        "ui_name": "KPF Target",
        "version": "0.1.0"
    },
    "parameters": {
        "target_info_name": {
            "default": 'null',
            "description": "observer provided name",
            "optionality": "required",
            "type": "string",
            "ui_name": "Target Name",
            "units": 'null'
        },
        "target_info_comment": {
            "ui_name": "Target Comment",
            "option": "optional",
            "default": "",
            "optionality": "optional",
            "type": "string",
            "units": 'null'
        },
        "target_info_2mass_id": {
            "default": 'null',
            "description": "The 2MASS ID of the target",
            "optionality": "required",
            "type": "string",
            "ui_name": "2MASS ID",
            "units": 'null'
        },
        "target_info_gaia_id": {
            "default": 'null',
            "description": "The GAIA DR3 ID of the target",
            "optionality": "required",
            "type": "string",
            "ui_name": "GAIA DR3 ID",
            "units": 'null'
        },
        "target_info_gmag": {
            "allowed": [
                -30,
                30
            ],
            "default": 'null',
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
            "default": 'null',
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
            "default": 'null',
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
            "default": 'null',
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
            "default": 'null',
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
            "default": 'null',
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
            "default": 'null',
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
            "units": 'null'
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
                'null',
                "^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}$"
            ],
            "default": 'null',
            "optionality": "optional",
            "type": "string",
            "units": "YR-MM-DD hh:mm:ss"
        }
    }
}


