import generate_utils as utils
import generate_random_utils as random_utils

def filled_acq_templates():
    acq_templates = [
        {
            "metadata": {
                "name": "kpf_acq_bright",
                "ui_name": "KPF Bright Acquisition",
                "instrument": "KPF",
                "template_type": "acquisition",
                "version": "0.1.1",
                "script": "kpf_acq_bright",
                "script_version": "0.1.0",
                "sequence_number": 0
            },
        },
        {
            "metadata": {
                "name": "kpf_acq_faint",
                "ui_name": "KPF Faint Acquisition",
                "instrument": "KPF",
                "template_type": "acquisition",
                "version": "0.1.1",
                "script": "kpf_sci_acq_script",
                "script_version": "0.1.0",
                "sequence_number": 0
            },
        }
    ]

    return acq_templates


def filled_common_parameters():
    schema = {
        "metadata": {
            "name": "kpf_common_parameters",
            "ui_name": "KPF Common Parameters",
            "instrument": "KPF",
            "template_type": "common_parameters",
            "version": "0.1.1"
        },
        "instrument_parameters": {
            "inst_cfg_simulcal_source": "science",
            "inst_cfg_simulcal_autofilter": random_utils.rand_bool(),
            "inst_cfg_simulcal_nd1": 'ND0.1',
            "inst_cfg_simulcal_nd2": 'ND0.1',
            "inst_cfg_sss_sky": random_utils.rand_bool(),
            "inst_cfg_sss_sci": random_utils.rand_bool(),
            "inst_cfg_sss_socal_sci": random_utils.rand_bool(),
            "inst_cfg_sss_socal_cal": random_utils.rand_bool()
        },
        "guider_parameters": {
            "guider1_cfg_mode": "manual",
            "guider1_cfg_framerate": random_utils.randInt(1, 400),
            "guider1_cfg_camgain": "high",
            "guider1_cfg_exptime": random_utils.randFloat(),
            "guider1_cfg_loopgain": random_utils.randFloat(),
            "guider1_cfg_xwindow": 24,
            "guider1_cfg_ywindow": 24,
            "guider1_cfg_raoffset": 20.0*random_utils.randFloat(),
            "guider1_cfg_decoffset": 20.0*random_utils.randFloat(),
        },
        "detector parameters": {},
        "tcs_parameters": {}
    }


def filled_sci_templates(template_list):
    templates_version = utils.parse_templates_version(template_list)

    sci_templates = [
        {
            "metadata": {
                "name": "kpf_sci_stare",
                "ui_name": "kpf stare observation",
                "instrument": "KPF",
                "template_type": "science",
                "version": templates_version["kpf_sci_stare"],
                "script": "kpf_sci_stare",
                "script_version": "0.1.0",
                "sequence_number": 1
            },
            "parameters": {
                "target_info_spectraltype": "B",
                "inst_cfg_nexp": random_utils.randInt(1, 100),
                "inst_cfg_exptime": random_utils.randInt(1, 3600),
                "inst_cfg_trigger_cahk": random_utils.rand_bool(),
                "inst_cfg_trigger_green": random_utils.rand_bool(),
                "inst_cfg_trigger_red": random_utils.rand_bool(),
                "inst_cfg_expmeter_active": random_utils.rand_bool(),
                "inst_cfg_expmeter_flux": 10000*random_utils.randFloat(),
            }
        }
    ]

    return sci_templates

def generate_inst_package(template_list):

    schema = {
        "metadata": {
            "name": "kpf_instrument_package",
            "ui_name": "KPF Instrument Package",
            "version": "0.0.1",
            "instrument": "KPF",
            "observing_modes": ["spectroscopy"]
        },
        "optical_parameters": {
            "field_of_view": [1200, 1200],
            "slit_length": 4
        },
        "guider1": {
            "name": "Guider",
            "fov": [120, 120],
            "pixel_scale": 0.17,
            "pa_offset": 'null',
            "read_noise": 'null',
            "gain": 'null',
            "zero_points": 'null',
            "sensitivity": 'null',
            "filters": 'null'
        },
        "configurable_elements": [
        ],
        "pointing_origins": [
            "SKY",
            "REF",
            "SPEC"
        ],
        "template_list": utils.parse_templates_version(template_list),
        "event_table": 'null',
        "comment": "A KPF Instrument Package"
    }

    return schema
