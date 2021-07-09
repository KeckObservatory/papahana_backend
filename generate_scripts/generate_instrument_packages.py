import random

import generate_utils as utils
# from papahana_flask_server_demo.config import config_collection
from papahana import util as papahana_util


def generate_optical_params(inst='KCWI'):
    field_of_view = {'KCWI': [1200, 1200]}
    slit_length = {'KCWI': {'long_slit': 77, 'ifu': 4}}

    schema = {'field_of_view': field_of_view[inst],
              'slit_length': slit_length[inst]}

    return schema


def get_guider_params(inst='KCWI'):
    name = {'KCWI': 'Guider'}
    field_of_view = {'KCWI': [120, 120]}
    pixel_scale = {'KCWI': 0.17}
    pa_offset = {'KCWI': None}
    read_noise = {'KCWI': None}
    gain = {'KCWI': None}
    zero_points = {'KCWI': None}
    sensitivity = {'KCWI': None}
    filters = {'KCWI': None}

    schema = {'name': name[inst],
              'fov': field_of_view[inst],
              'pixel_scale': pixel_scale[inst],
              'pa_offset': pa_offset[inst],
              'read_noise': read_noise[inst],
              'gain': gain[inst],
              'zero_points': zero_points[inst],
              'sensitivity': sensitivity[inst],
              'filters': filters[inst]}

    return schema


def get_kcwi_inst_params(inst='KCWI'):

    schema = {'gain': 2.2,
              'bias': 4.4,
              'scale': 0.1}

    return schema


def get_event_table():

    events = {'dither': 'offset_tel',
              'expose': 'set_exposure_time',
              'pause': 'wait'}

    return


def generate_ip(version, inst="KCWI"):

    schema = {
        "version": version,
        "instrument": "KCWI",
        "observing_modes": ['imaging', 'long-slit', 'multi-slit', 'ifu'],
        "optical_parameters": generate_optical_params(),
        "guider": get_guider_params(),
        "pointing_origins": ["IFU", "REF", "Imaging"],
        "template_names": ["KCWI_ifu_acq_offsetStar", "KCWI_ifu_acq_direct",
                           "KCWI_ifu_sci_stare", "KCWI_ifu_sci_dither"],
        "common_inst_params": {"KCWI": get_kcwi_inst_params()},
        "event_table": get_event_table(),

        "comment": 'A KCWI Instrument Package'
    }

    return schema


if __name__=='__main__':
    n_packages = 5
    args = utils.parse_args()
    mode = args.mode

    config = utils.read_config(mode)
    print(f"Using {config['dbName']} database")

    # Create IP collection
    print("...generating Instrument Packages.")
    coll = papahana_util.config_collection('ipCollect', conf=config)
    coll.drop()

    version = 0.1
    for idx in range(n_packages):
        doc = generate_ip(round(version, 1))
        version += 0.1
        result = coll.insert_one(doc)
