
from instpack_base import InstPackBase
import configuration_kpf as kpf_cfg
import generate_utils as utils

class InstPack_KPF(InstPackBase):
    def __init__(self, inst):
        super(InstPack_KPF, self).__init__('KPF')

    def generate_ip(self, template_list, recipe_list):

        rlist = []
        for recipe_schema in recipe_list:
            rlist.append(recipe_schema['metadata']['name'])

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

    def acq_templates(self):
        return [kpf_cfg.kpf_acq_template]

    def sci_templates(self):
        return [kpf_cfg.kpf_science_template]

    def common_parameters_template(self):
        return [kpf_cfg.kpf_common_parameters_template]

    def cal_templates(self):
        cal_tmps = [kpf_cfg.kpf_arc_template, kpf_cfg.kpf_darks_template]
        return cal_tmps

    def misc_templates(self):
        return [kpf_cfg.kpf_target_template]

    def get_scripts(self):
        scripts = {}
        scripts['kpf_acq'] = kpf_cfg.kpf_acq
        scripts['kpf_sci'] = kpf_cfg.kpf_sci
        return scripts

    def get_recipes(self):
        recipes = {}

        recipes["science_sidereal_target"] = kpf_cfg.science_sidereal_target
        recipes["science_non_sidereal_target"] = kpf_cfg.science_non_sidereal_target
        recipes["science_kpf_target"] = kpf_cfg.science_kpf_target
        recipes["calibration_dark"] = kpf_cfg.calibration_dark
        recipes["calibration_arcs"] = kpf_cfg.calibration_arcs

        return recipes
