import generate_utils as utils
from instpack_base import InstPackBase
import configuration_nires as nires_cfg

class InstPack_NIRES(InstPackBase):
    def __init__(self, inst):
        super(InstPack_NIRES, self).__init__('NIRES')

    @staticmethod
    def generate_ip(template_list, config=None, inst_list=None):
        schema = {
            "metadata": {
                "name": "nires_instrument_package",
                "ui_name": "NIRES Instrument Package",
                "version": "0.1.0",
                "instrument": "NIRES",
                "observing_modes": ["imaging", "spectroscopy"]
            },
            "optical_parameters": {
            },
            "configurable_elements": [
            ],
            "pointing_origins": ["NIRES", "SLIT_IMAG", "REF_SLIT", "REF", "IMAG", "MIRA"
            ],
            "template_list": utils.parse_templates_version(template_list),
            "recipe_list": None,
            "event_table": None,
            "comment": "A NIRES Instrument Package"
        }
        return schema

    def acq_templates(self):
        return [nires_cfg.nires_acq_template]

    def sci_templates(self):
        return [nires_cfg.nires_dither_science_template,
                nires_cfg.nires_stare_science_template, 
                nires_cfg.nires_drift_scan_science_template]

    def common_parameters_template(self):
        return [nires_cfg.nires_common_parameters_template]

    def cal_templates(self):
        cal_tmps = [nires_cfg.nires_calibration_template]
        return cal_tmps

    def get_scripts(self):
        scripts = {}
        scripts['nires_acq'] = nires_cfg.nires_acq
        scripts['nires_sci'] = nires_cfg.nires_sci
        return scripts


    def get_recipes(self):
        return [] 

    def misc_templates(self):
        return [] 