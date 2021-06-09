import pymongo
import pdb
from generate_demo_database import read_mode, read_config
from papahana_flask_server_demo.config import config_collection

kcwi_acq_direct_template_properties = {
        "wrap": {
            "ui_name": "Rotator Wrap Position",
            "option": "list",
            "allowed": ['south', 'north'],
            "default": None,
            "optionality": "optional",
            "type": "string"
        },
        "rotmode": {
            "ui_name": "Rotator Mode",
            "option": "list",
            "allowed": ["PA", "stationary", "vert_angle"],
            "default": "PA",
            "optionality": "required",
            "type": "string"
        },
        "guider_po": {
            "ui_name": "Pointing origin",
            "option": "list",
            "allowed": ["REF", "IFU"],
            "default": "IFU",
            "optionality": "required",
            "type": "string"
        },
        "guider_gs_ra": {
            "ui_name": "Guide Star Right Ascension",
            "option": "range",
            "allowed": [0, 24],
            "default": None,
            "optionality": "optional",
            "type": "number",
        },
        "guider_gs_dec": {
            "ui_name": "Guide Star Declination",
            "option": "range",
            "allowed": [-90, 90],
            "default": None,
            "optionality": "optional",
            "type": "number",
        },
        "guider_gs_mode": {
            "ui_name": "Guide Star Selection Mode",
            "option": "list",
            "allowed": ["Automatic", "Operator", "User"],
            "default": "Automatic",
            "optionality": "required",
            "type": "string"
        }
}  

# kcwi_acq_direct_template_schema = {
#     "title": 'direct acquisition template',
#     "type": 'object',
#     "required": ["guider_po", "guider_gs_mode"],
#     "properties": kcwi_acq_direct_template_properties
# }


dither_schema = {
    "min": {
        "ui_name": "minimum",
        "option": "range",
        "allowed": [-4000.0, 4000.0],
        "default": None,
        "optionality": "required",
        "type": "number"
      },
    "max": {
        "ui_name": "minimum",
        "option": "range",
        "allowed": [-4000.0, 4000.0],
        "default": None,
        "optionality": "required",
        "type": "number"
    },
    "position": {
        "ui_name": "Telescope Position",
        "option": "list",
        "allowed": ["T", "S", "O"],
        "default": "T",
        "optionality": "required",
        "type": "string",
    },
    "guided": {
        "ui_name": "Guided",
        "option": "bool",
        "default": True,
        "optionality": "required",
        "type": "bool"
    }
}

# dither_schema_array = {
#     "title": "List and types of positions",
#     "type": "array",
#     "items": dither_schema
# }


kcwi_ifu_sci_dither_properties = {
    "det1_exptime": {
        "ui_name": "Blue exposure time for individual exposures",
        "option": "range",
        "allowed": [0, 3600],
        "default": None,
        "optionality": "required",
        "type": "integer"
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
        "allowed": [0, 3600],
        "default": None,
        "optionality": "optional",
        "type": "integer"
    },
    "det2_nexp": {
        "ui_name": "Blue number of exposures per dither position",
        "option": "range",
        "allowed": [0, 3600],
        "default": None,
        "optionality": "optional",
        "type": "integer",
    },
    "seq_ndither": {
        "ui_name": "Number of dither positions",
        "option": "range",
        "allowed": [0, 99],
        "default": None,
        "optionality": "required",
        "type": "integer",
    },
    "seq_ditarray": dither_schema
}
#
# kcwi_config_properties = {
#        "cfg_cam1_grating": {
#             "title": "Blue Grating",
#             "enum": [ "BL","BM","BH1","BH2" ],
#             "type": "string",
#         },
#         "cfg_cam1_cwave": {
#             "title": "Blue Central Wavelength",
# 	    "minimum": 3500,
# 	    "maximum": 6500,
#             "type": "number",
#         },
#         "cfg_cam2_grating": {
#             "title": "Red Grating",
#             "enum": [ "RL","RM","RH1","RH2" ],
#             "type": "string",
#         },
#         "cfg_cam2_cwave": {
#             "title": "Red Central Wavelength",
# 	    "minimum": 6500,
# 	    "maximum": 10000,
#             "type": "number",
#         },
#         "cfg_slicer": {
#             "title": "Image Slicer",
#             "enum": [ "Small", "Medium", "Large" ],
#             "type": "string",
#         }
# }

# kcwi_config_schema = {
#         "title": "KCWI configuration",
#         "type": "object",
#         "required": ["cfg_slicer", "cfg_cam1_cwave", "cfg_cam1_grating"],
#         "properties": kcwi_config_properties
# }

# kcwi_ifu_sci_dither_schema = {
#         "title": "Dither Properies",
#         "type": "object",
# 	"required": ["seq_ndither", "seq_ditarray", "det1_exptime", "det2_exptime"],
#         "properties": kcwi_ifu_sci_dither_properties
# }


kcwi_ifu_sci_stare_parameters = {
    "det1_exptime": {
        "ui_name": "Blue exposure time",
        "option": "range",
        "allowed": [0, 3600],
        "default": None,
        "optionality": "required",
        "type": "number",
    },
    "det1_nexp": {
        "ui_name": "Blue number of exposures",
        "option": "range",
        "allowed": [0, 3600],
        "default": None,
        "optionality": "required",
        "type": "integer",
    },
    "det2_exptime": {
        "ui_name": "Red exposure time",
        "option": "range",
        "allowed": [0, 3600],
        "default": None,
        "optionality": "required",
        "type": "number",
    },
    "det2_nexp": {
        "ui_name": "Blue number of exposures",
        "option": "range",
        "allowed": [0, 3600],
        "default": None,
        "optionality": "required",
        "type": "integer",
    }
}

kcwi_ifu_sci_dither_template = {
    "metadata": {
        "name": "KCWI_ifu_sci_dither",
        "ui_name": "KCWI dither",
        "instrument": "KCWI",
        "type": "science",
        "version": 0.1,
        "script": "KCWI_ifu_sci_stare"
    },
    "properties": kcwi_ifu_sci_dither_properties

}

kcwi_ifu_sci_stare_template = {
    "metadata": {
        "name": "KCWI_ifu_sci_stare",
        "ui_name": "KCWI stare",
        "instrument": "KCWI",
        "type": "science",
        "version": 0.1,
        "script": "KCWI_ifu_sci_stare"
    },
    "properties": kcwi_ifu_sci_stare_parameters
}

kcwi_ifu_acq_direct_template = {
    "metadata": {
        "name": "KCWI_ifu_acq_direct",
        "ui_name": "KCWI direct",
        "instrument": "KCWI",
        "type": "acquisition",
        "version": 0.1,
        "script": "KCWI_ifu_acq_direct"
    },
    "properties": kcwi_acq_direct_template_properties
	# "schema": kcwi_acq_direct_template_schema,
}

#TODO: Fill with separate template
kcwi_ifu_acq_offsetStar_template = kcwi_ifu_acq_direct_template.copy()
kcwi_ifu_acq_offsetStar_template['name'] = 'KCWI_ifu_acq_offsetStar'

# kcwi_config_template = {
#         "name": "KCWI_config",
#         "instrument": "KCWI",
#         "type": "config",
#         "version": 0.1,
#         "schema": kcwi_config_schema
# }

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
        "acquisition": [ kcwi_ifu_acq_direct_template, kcwi_ifu_acq_offsetStar_template ],
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
