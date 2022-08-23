import generate_utils as utils

def filled_acq_templates():
    acq_templates = [
        {
            "metadata": {
                "name": "kcwi_ifu_acq_direct",
                "ui_name": "KCWI direct",
                "instrument": "KCWI",
                "template_type": "acquisition",
                "version": "0.1.1",
                "script": "kcwi_ifu_acq_direct",
                "sequence_number": 0
            },
            "parameters": {
                "rot_cfg_wrap": "auto",
                "rot_cfg_mode": "PA",
                "tcs_coord_po": "IFU",
                "tcs_coord_raoff": "0",
                "tcs_coord_decoff": '1',
                "guider1_coord_ra": "12:44:55.6",
                "guider1_coord_dec": '55:22:19.9',
                "guider1_coord_mode": 'operator'
            }
        }
    ]

    return acq_templates

def filled_common_parameters():
    schema = {
        "metadata": {
            "name": "kcwi_common_parameters",
            "ui_name": "KCWI Common parameters",
            "instrument": "KCWI",
            "template_type": "common_parameters",
            "version": "0.1.1"
        },
        "instrument_parameters": {
            "inst_cfg_slicer": "slicer1",
            "inst_cfg_blockingfilter": "filter1",
            "inst_cfg_calib": "Sky",
            "inst_cfg_hatch": "open",
            "inst_cfg_polarimeter": "Sky",
            "inst_cfg_ifu": "Large",
            "inst_cfg1_filter": "Large",
            "inst_cfg2_filter": "Medium",
            "inst_cfg1_grating": "BH3",
            "inst_cfg2_grating": "RH3",
            "inst_ns_mask": "open",
            "inst_ns_direction": 1,
            "inst_kmirror_mode": "Tracking",
            "inst_kmirror_angle": 122,
            "inst_wavelength1_central": 450,
            "inst_wavelength2_central": 789,
            "inst_wavelength1_peak": 470,
            "inst_wavelength2_peak": 800
        },
        "detector_parameters": {
              "det1_mode_binning": '1x1',
              "det2_mode_binning": '1x1',
              "det1_mode_amp": 0,
              "det2_mode_amp": 5,
              "det1_mode_read": 0,
              "det2_mode_read": 1,
              "det1_mode_gain": 2,
              "det2_mode_gain": 5
        },
        "tcs_parameters": {

        }

    }

    return schema


def filled_sci_templates(template_list):
    templates_version = utils.parse_templates_version(template_list)

    sci_templates = [
        {
            "metadata": {
                "name": "kcwi_ifu_sci_stare",
                "ui_name": "KCWI stare",
                "instrument": "KCWI",
                "template_type": "science",
                "version": templates_version["kcwi_ifu_sci_stare"],
                "script": "kcwi_ifu_sci_stare",
                "sequence_number": 1
            },
            "parameters": {
                "det1_exp_time": 30,
                "det1_exp_number": 4,
                "det2_exp_time": 24,
                "det2_exp_number": 5
            }
        },
        {
            "metadata": {
                "name": "kcwi_ifu_sci_dither",
                "ui_name": "KCWI dither",
                "instrument": "KCWI",
                "template_type": "science",
                "version": templates_version["kcwi_ifu_sci_dither"],
                "script": "kcwi_ifu_sci_dither",
                "sequence_number": 1
            },
            "parameters": {
                "det1_exp_time": 60.0,
                "det1_exp_number": 12,
                "det2_exp_time": 121.0,
                "det2_exp_number": 6,
                "seq_dither_number": 4,
                "seq_dither_pattern": [
                    {"seq_dither_ra_offset": 0, "seq_dither_dec_offset": 0,
                     "seq_dither_position": 'T', "seq_dither_guided": True},
                    {"seq_dither_ra_offset": 5, "seq_dither_dec_offset": 5,
                     "seq_dither_position": 'S', "seq_dither_guided": False},
                    {"seq_dither_ra_offset": 0, "seq_dither_dec_offset": 0,
                     "seq_dither_position": 'T', "seq_dither_guided": True},
                    {"seq_dither_ra_offset": 5, "seq_dither_dec_offset": 5,
                     "seq_dither_position": 'S', "seq_dither_guided": False}
                ]
            }
        }
    ]

    return sci_templates


def generate_inst_package(template_list):

    # for on_id in ob_blocks:
    #     template_name =

    schema = {
        "metadata": {
            "name": "kcwi_instrument_package",
            "ui_name": "KCWI Instrument Package",
            "version": "0.1.0",
            "instrument": "KCWI",
            "observing_modes": ["imaging", "ifu"]
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
            "inst_cfg_slicer",
            "inst_cfg_hatch",
            "inst_cfg_calib",
            "inst_cfg_polarimeter",
            "inst_cfg_ifu",
            "inst_cfg1_filter",
            "inst_cfg1_grating",
            "inst_cfg1_blockingfilter",
            "inst_cfg2_filter",
            "inst_cfg2_grating",
            "inst_cfg2_blockingfilter",
            "inst_ns_mask",
            "inst_ns_direction",
            "inst_kmirror_mode",
            "inst_kmirror_angle",
            "inst_det1_focus",
            "inst_det2_focus",
            "inst_wavelengt1_central",
            "inst_wavelength1_peak"
            "inst_wavelength2_central",
            "inst_wavelength2_peak"
            "det1_mode_binning",
            "det1_mode_amp",
            "det1_mode_read",
            "det1_mode_gain",
            "det2_mode_binning",
            "det2_mode_amp",
            "det2_mode_read",
            "det2_mode_gain",
        ],
        "pointing_origins": [
            "IFU",
            "REF",
            "Imaging"
        ],
        "template_list": utils.parse_templates_version(template_list),
        # "common_parameters": ObjectId("61203d3a86574cd1da879135")
        "event_table": 'null',
        "comment": "A KCWI Instrument Package"
    }

    return schema


