

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
    "detector parameters": {
        "det1_trigger": {
            "ui_name": "Green Detector On",
            "description": "Trigger the green detector?",
            "option": "boolean",
            "default": None,
            "optionality": "required",
            "type": "boolean",
            "units": None
        },
        "det1_mode_gain": {
            "ui_name": "The green side gain",
            "option": "set",
            "allowed": [1, 2, 5, 10],
            "default": 1,
            "optionality": "optional",
            "type": "integer",
            "units": None
        },
        "det1_cfg_binning": {
            "ui_name": "The green side binning",
            "allowed": ["1,1", "2,2"],
            "option": "set",
            "optionality": "optional",
            "default": "1,1",
            "type": "string",
            "units": None
        },
        "det2_trigger": {
            "ui_name": "Red Detector On",
            "description": "Trigger the red detector?",
            "option": "boolean",
            "default": None,
            "optionality": "required",
            "type": "boolean",
            "units": None
        },
        "det2_mode_gain": {
            "ui_name": "The green side gain",
            "option": "set",
            "allowed": [1, 2, 5, 10],
            "default": 1,
            "optionality": "optional",
            "type": "integer",
            "units": None
        },
        "det2_cfg_binning": {
            "ui_name": "The green side binning",
            "allowed": ["1,1", "2,2"],
            "option": "set",
            "optionality": "optional",
            "default": "1,1",
            "type": "string",
            "units": None
        },
        "det3_trigger": {
            "ui_name": "CA H&K Detector On",
            "description": "Trigger the ca h&k detector?",
            "option": "boolean",
            "default": None,
            "optionality": "required",
            "type": "boolean",
            "units": None
        },
        "det3_mode_gain": {
            "ui_name": "The green side gain",
            "option": "set",
            "allowed": [1, 2, 5, 10],
            "default": 1,
            "optionality": "optional",
            "type": "integer",
            "units": None
        },
        "det3_cfg_binning": {
            "ui_name": "The green side binning",
            "allowed": ["1,1", "2,2"],
            "option": "set",
            "optionality": "optional",
            "default": "1,1",
            "type": "string",
            "units": None
        },
    },
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
        "det1_exp_number": {
            "ui_name": "Number of Exposures",
            "description": "The number of exposures to take.",
            "option": "range",
            "allowed": [1, 100],
            "default": None,
            "optionality": "required",
            "type": "int",
            "units": None
        },
        "det1_exp_time": {
            "ui_name": "Exposure Time",
            "description": "The exposure time of an individual science exposure.",
            "option": "range",
            "allowed": [1, 3600],
            "default": None,
            "optionality": "required",
            "type": "float",
            "units": "seconds"
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
