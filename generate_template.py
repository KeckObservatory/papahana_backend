import pymongo
import pdb
from generate_demo_database import read_mode, read_config
from papahana_flask_server_demo.config import config_collection
from copy import deepcopy

kcwi_acq_direct_template_parameters = {
        "wrap": {
            "ui_name": "Rotator Wrap Position",
            "option": "list",
            "allowed": ['south', 'north', 'auto'],
            "default": 'auto',
            "optionality": "optional",
            "type": "string"
        },
        "rotmode": {
            "ui_name": "Rotator Mode",
            "option": "list",
            "allowed": ["PA", "stationary", "vertical_angle"],
            "default": None,
            "optionality": "required",
            "type": "string"
        },
        "guider_po": {
            "ui_name": "Pointing origin",
            "option": "list",
            "allowed": ["REF", "IFU"],
            "default": None,
            "optionality": "required",
            "type": "string"
        },
        "ra_offset": {
            "ui_name": "The offset from coordinates to get to the target",
            "option": "range",
            "allowed": [0.0, 2000.0],
            "default": None,
            "optionality": "optional",
            "type": "float",
        },
        "dec_offset": {
            "ui_name": "The offset from coordinates to get to the target",
            "option": "range",
            "allowed": [0.0, 2000.0],
            "default": None,
            "optionality": "optional",
            "type": "float",
        },
        "guider_gs_ra": {
            "ui_name": "Guide Star Right Ascension",
            "option": "range",
            "allowed": [0.0, 24.0],
            "default": None,
            "optionality": "optional",
            "type": "string",
        },
        "guider_gs_dec": {
            "ui_name": "Guide Star Declination",
            "option": "range",
            "allowed": [-90.0, 90.0],
            "default": None,
            "optionality": "optional",
            "type": "string",
        },
        "guider_gs_mode": {
            "ui_name": "Guide Star Selection Mode",
            "option": "list",
            "allowed": ["auto", "operator", "user"],
            "default": None,
            "optionality": "required",
            "type": "string"
        }

}  

dither_schema = {
    "ui_name": "Dither Pattern",
    "option": "list",
    "default": None,
    "optionality": "required",
    "type": "array",
    "allowed": [
        {"ra": {
            "ui_name": "Right Ascension Offset",
            "option": "range",
            "allowed": [-4000.0, 4000.0],
            "default": None,
            "optionality": "required",
            "type": "float"
        }},
        {"dec": {
            "ui_name": "Declination Offset",
            "option": "range",
            "allowed": [-4000.0, 4000.0],
            "default": None,
            "optionality": "required",
            "type": "float"
        }},
        {"position": {
            "ui_name": "Telescope Position",
            "option": "list",
            "allowed": ["T", "S", "O"],
            "default": None,
            "optionality": "required",
            "type": "string",
        }},
        {"guided": {
            "ui_name": "Guided",
            "option": "boolean",
            "default": True,
            "optionality": "required",
            "type": "boolean"
        }}
    ]
}

kcwi_ifu_sci_dither_parameters = {
    "det1_exptime": {
        "ui_name": "Blue exposure time for individual exposures",
        "option": "range",
        "allowed": [0.0, 3600.0],
        "default": None,
        "optionality": "required",
        "type": "float"
    },
    "det1_nexp": {
        "ui_name": "Blue number of exposures per dither position",
        "option": "range",
        "allowed": [0, 100],
        "default": None,
        "optionality": "required",
        "type": "integer"
    },
    "det2_exptime": {
        "ui_name": "Red exposure time for individual exposures",
        "option": "range",
        "allowed": [0.0, 3600.0],
        "default": None,
        "optionality": "optional",
        "type": "float"
    },
    "det2_nexp": {
        "ui_name": "Blue number of exposures per dither position",
        "option": "range",
        "allowed": [0.0, 100],
        "default": None,
        "optionality": "optional",
        "type": "integer",
    },
    "seq_ndither": {
        "ui_name": "Number of dither positions",
        "option": "range",
        "allowed": [0, 100],
        "default": None,
        "optionality": "required",
        "type": "integer",
    },
    "seq_ditarray": dither_schema
}

kcwi_ifu_sci_stare_parameters = {
    "det1_exptime": {
        "ui_name": "Blue exposure time",
        "option": "range",
        "allowed": [0.0, 3600.0],
        "default": None,
        "optionality": "required",
        "type": "float",
    },
    "det1_nexp": {
        "ui_name": "Blue number of exposures",
        "option": "range",
        "allowed": [0.0, 3600.0],
        "default": None,
        "optionality": "required",
        "type": "integer",
    },
    "det2_exptime": {
        "ui_name": "Red exposure time",
        "option": "range",
        "allowed": [0.0, 3600.0],
        "default": None,
        "optionality": "optional",
        "type": "float",
    },
    "det2_nexp": {
        "ui_name": "Blue number of exposures",
        "option": "range",
        "allowed": [0.0, 3600.0],
        "default": None,
        "optionality": "optional",
        "type": "integer",
    }
}

kcwi_ifu_sci_dither_template = {
    "metadata": {
        "name": "KCWI_ifu_sci_dither",
        "ui_name": "KCWI dither",
        "instrument": "KCWI",
        "template_type": "science",
        "version": 0.1,
        "script": "KCWI_ifu_sci_stare"
    },
    "parameters": kcwi_ifu_sci_dither_parameters

}

kcwi_ifu_sci_stare_template = {
    "metadata": {
        "name": "KCWI_ifu_sci_stare",
        "ui_name": "KCWI stare",
        "instrument": "KCWI",
        "template_type": "science",
        "version": 0.1,
        "script": "KCWI_ifu_sci_stare"
    },
    "parameters": kcwi_ifu_sci_stare_parameters
}

kcwi_ifu_acq_direct_template = {
    "metadata": {
        "name": "KCWI_ifu_acq_direct",
        "ui_name": "KCWI direct",
        "instrument": "KCWI",
        "template_type": "acquisition",
        "version": 0.1,
        "script": "KCWI_ifu_acq_direct"
    },
    "parameters": kcwi_acq_direct_template_parameters
}

#TODO: Fill with separate template
kcwi_ifu_acq_offsetStar_template = deepcopy(kcwi_ifu_acq_direct_template)
kcwi_ifu_acq_offsetStar_template['metadata']['name'] = 'KCWI_ifu_acq_offsetStar'

kcwi_instrument_package = {
    "instrument": "KCWI",
    "version": "0.1",
    "modes": ["ifu", "img"],
    "cameras": [
        {
            "name": "BLUE",
            "type": "spectrograph",
            "detector": "4kx4k EE2V",
            "identifier": "CAM1"
            
        },
        {
            "name": "RED",
            "type": "spectrograph",
            "detector": "None",
            "identifier": "CAM2"
        }
    ],
    "templates":{
        "acquisition": [kcwi_ifu_acq_direct_template, kcwi_ifu_acq_offsetStar_template],
        "science": [ kcwi_ifu_sci_stare_template, kcwi_ifu_sci_dither_template ]
        # "configuration": [ kcwi_config_template ]
    },
}

if __name__=="__main__":
   # pdb.set_trace()
   dbName = 'papahana' 
   mode = read_mode()
   config = read_config(mode)
   coll = config_collection('templateCollect', mode=mode, conf=config)
   coll.drop()
   print('adding templates to collection')
   templates = [ kcwi_ifu_acq_offsetStar_template,
                 kcwi_ifu_acq_direct_template,
                 kcwi_ifu_sci_stare_template,
                 kcwi_ifu_sci_dither_template
               ]
   result = coll.insert_many(templates, ordered=False, bypass_document_validation=True)
