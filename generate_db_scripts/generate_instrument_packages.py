import random

import generate_utils as utils
from papahana import util as papahana_util

kcwi_common_params = {
    "instrument_slicer": {
        "ui_name": "Slicer",
        "option": "list",
        "allowed": ['slicer1', 'slicer2'],
        "default": None,
        "optionality": "required",
        "type": "string"
    },
    "instrument_filter_blocking": {
        "ui_name": "Blocking Filter",
        "option": "list",
        "allowed": ['filter1', 'filter2'],
        "default": None,
        "optionality": "required",
        "type": "float"
    },

    # nod-shuffle
    "instrument_ns_mask": {
        "ui_name": "Nod and Shuffle Mask",
        "option": "list",
        "allowed": ['open', 'Dark', 'Mask'],
        "default": 'open',
        "optionality": "optional",
        "type": "float"
    },
    "instrument_ns_direction": {
        "ui_name": "Nod and Shuffle Direction (1=down, 2=up)",
        "option": "list",
        "allowed": [1, 2],
        "default": 1,
        "optionality": "optional",
        "type": "float"
    },

    # added from KCWI Desktop

    "instrument_hatch": {
        "ui_name": "Hatch",
        "option": "list",
        "allowed": ['open', 'closed'],
        "default": 'open',
        "optionality": "optional",
        "type": "string"
    },

    "instrument_calib": {
        "ui_name": "Calibration",
        "option": "list",
        "allowed": ['Sky', 'Mirror', 'Filter'],
        "default": None,
        "optionality": "required",
        "type": "string"
    },

    "instrument_polarimeter": {
        "ui_name": "Polarimeter",
        "option": "list",
        "allowed": ['Sky', 'Polar', 'Lens'],
        "default": "Lens",
        "optionality": "optional",
        "type": "string"
    },
    "instrument_ifu": {
        "ui_name": "IFU",
        "option": "list",
        "allowed": ['Home', 'Large', 'Medium', 'Small', 'FPCam', 'Aux'],
        "default": None,
        "optionality": "required",
        "type": "string"
    },
    "instrument_filter": {
        "ui_name": "IFU",
        "option": "list",
        "allowed": ['Home', 'Large', 'Medium', 'Small', 'FPCam', 'Aux'],
        "default": None,
        "optionality": "required",
        "type": "string"
    },
    "instrument_grating": {
        "ui_name": "Grating",
        "option": "list",
        "allowed": ['None', 'BH3', 'BL', 'BH2', 'BM', 'GGTrg'],
        "default": None,
        "optionality": "required",
        "type": "string"
    },

    # K-Mirror (rotator in KCWI controlled by observers)
    "instrument_kmirror_mode": {
        "ui_name": "K-Mirror Mode",
        "option": "list",
        "allowed": ["Tracking", "Stationary"],
        "default": None,
        "optionality": "required",
        "type": "string"},

    "instrument_kmirror_angle": {
        "ui_name": "K-Mirror Angle",
        "option": "range",
        "allowed": [0.0, 360.0],
        "default": None,
        "optionality": "required",
        "type": "float"
    },
    # end K-mirror

    "instrument_detector_focus": {
        "ui_name": "Grating",
        "option": "range",
        "allowed": [-5.0, 5.0],
        "default": None,
        "optionality": "required",
        "type": "float"},

    # CCD parameters
    "detector_binning": {
        "ui_name": "Detector Binning",
        "option": "range",
        "allowed": [350, 1050],
        "default": 2,
        "optionality": "optional",
        "type": "integer"},

    "detector_amp_mode": {
        "ui_name": "Amplifier Mode",
        "option": "range",
        "allowed": [1, 10],
        "default": 9,
        "optionality": "optional",
        "type": "integer"},
    "detector_read_mode": {
        "ui_name": "CCD Read Mode (0=slow, 1=fast)",
        "option": "list",
        "allowed": [0, 1],
        "default": None,
        "optionality": "required",
        "type": "integer"},
    "detector_gain": {
        "ui_name": "CCD Gain Multiplier",
        "option": "list",
        "allowed": [1, 2, 5, 10],
        "default": None,
        "optionality": "required",
        "type": "integer"},

    "instrument_wavelength_central": {
        "ui_name": "Central Wavelength (nm)",
        "option": "range",
        "allowed": [350, 1050],
        "default": None, "optionality":
            "required", "type": "float"
    },
    "instrument_wavelength_peak": {
        "ui_name": "Peak Wavelength (nm)",
        "option": "range",
        "allowed": [350, 1050],
        "default": None,
        "optionality": "required",
        "type": "float"},

}
#
# kcwi_optical_params = {
#     "fov"
# 'gain': 2.2, 'bias': 4.4, 'scale': 0.1
# }

kcwi_configurable_elements = list(kcwi_common_params.keys())


kcwi_guider_params = {
    'rotCenterX': '498',
    'rotCenterY': '515',
    'rotationOffset': '0.0',
    'refx': '506',
    'className': 'MagiqCamera',
    'signpa': '1.0',
    'flexure': 'false',
    'regName': 'magiq',
    'tvAngl': '0',
    'xPixSize': '0.184',
    'host': 'k2-magiq-camserver1',
    'tvFlip': 'no',
    'height': '1024',
    'width': '1024',
    'telescope': '2',
    'nogrot': 'false',
    'realCamName': 'kcwi',
    'defaultPorg': 'ref',
    'legacyHost': '',
    'arguments': 'null',
    'yPixSize': '0.184',
    'refy': '521',
    'noShutter': 'false',
    'xFlip': 'no',
    'fullBinning': '2',
    'stopKillsGuiding': 'true',
    'defaultDiffGuiding': 'true',
    'name': 'kcwi',
    'rpcProgNum': '34568',
    'mechService': 'kcwm',
    'nFilters': '2',
    'nFocus': '1',
    'biasFlip': 'yes',
    'saturationLevel': '16383',
    'nIQL': '0'}

# kcwi_guider_filters = {
#     ""
#     "R": {
#         focusOffset="0"/>
# <Filter name="I" focusOffset="0"/>
# <Filter name="B" focusOffset="0"/>
# <Filter name="V" focusOffset="0"/>
# <Defaults>
# 	<Filter index="1" value="open"/>
# 	<Filter index="2" value="Open"/>
# 	<Bias index="1" value="645"/>
# 	<Bias index="0" value="609"/>
# 	<Focus value="140"/>
# 	<IqlPosIn value="false"/>
# 	<Bias gain="0" index="0" value="645" />
#         <Bias gain="1" index="0" value="472" />
#         <Bias gain="2" index="0" value="443" />
#         <Bias gain="3" index="0" value="417" />
#
#         <Bias gain="0" index="1" value="609" />
#         <Bias gain="1" index="1" value="450" />
#         <Bias gain="2" index="1" value="423" />
#         <Bias gain="3" index="1" value="398" />
# </Defaults>
# <IQM aperture="107">
# <Focus scale="16.11" offset="0.11" />
# <TiltX scale1="9.07E5" scale2="-8.08E5" offset="0.0"/>
# <TiltY scale1="-1.22E6" scale2="2.03E4" offset="0.0"/>
# </IQM>
# </Guider>
#
# }

kcwi_optical_params = {
    'field_of_view': [1200, 1200],
    'slit_length': 4
}


def get_guider_params():

    inst = "KCWI"
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


def get_event_table():

    events = {'dither': 'offset_tel',
              'expose': 'set_exposure_time',
              'pause': 'wait'}

    return


def generate_ip_kcwi(version):
    """
    https://keckobservatory.atlassian.net/wiki/spaces/DSI/pages/1189052426/DDOI-007+Instrument+packages

    instrument name (e.g. KCWI)
    version (to be able to deal with instrument changes and upgrades)
    observing modes (imaging, long slit, multi_slit, ifu)
    optical parameters (field of view location, shape and size, scale …)
    position, nature and field of view of the guider
    list of pointing origins
    list of configurable elements
    list of available templates (acquisition, science, calibration, engineering)
    common parameters (these are template parameters that are common among all the templates, and are stored here to avoid repeating them for each template)
    event table (this is the key element that translates events into actual python functions, similar to the event table in the DRP framework. It is stored here because the entries into the event table are essentially the only allowed keywords in the script language and they are instrument specific)

    """

    schema = {
        "version": version,
        "instrument": "KCWI",
        "observing_modes": ['imaging', 'ifu'],
        "optical_parameters": kcwi_optical_params,
        "guider": get_guider_params(),
        "configurable_elements": kcwi_configurable_elements,
        "pointing_origins": ["IFU", "REF", "Imaging"],
        "template_names": ["KCWI_ifu_acq_offsetStar", "KCWI_ifu_acq_direct",
                           "KCWI_ifu_sci_stare", "KCWI_ifu_sci_dither"],
        "common_parameters": kcwi_common_params,
        "event_table": get_event_table(),

        "comment": 'A KCWI Instrument Package'
    }

    return schema


# if __name__=='__main__':
#     n_packages = 5
#     args = utils.parse_args()
#     mode = args.mode
#
#     config = utils.read_config(mode)
#
#     # Create IP collection
#     print("...generating Instrument Packages.")
#     coll = papahana_util.config_collection('ipCollect', conf=config)
#     coll.drop()
#
#     version_prefix = '0.1'
#     for idx in range(n_packages):
#         version = f'{version_prefix}.{idx}'
#         doc = generate_ip_kcwi(version)
#         result = coll.insert_one(doc)
