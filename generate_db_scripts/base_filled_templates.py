import generate_utils as utils


filled_acq_templates = [{}]
filled_common_parameters_templates = {}

def filled_sci_templates(template_list):
    templates_version = utils.parse_templates_metadata(template_list)

filled_common_parameters = {}

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
        "template_list": utils.parse_templates_metadata(template_list),
        "common_parameters": ObjectId
        "event_table": 'null',
        "comment": "A KPF Instrument Package"
    }

    return schema
