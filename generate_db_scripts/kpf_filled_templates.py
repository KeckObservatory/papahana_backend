import generate_utils as utils
import generate_random_utils as random_utils

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
    # templates_version = utils.parse_templates_version(template_list)
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

    return schema


def filled_sci_templates(template_list):
    templates_version = utils.parse_templates_version(template_list)

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


def generate_inst_package(template_list):

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
        "event_table": None,
        "comment": "A KPF Instrument Package"
    }

    return schema
