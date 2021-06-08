import pymongo
import pdb
from generate_demo_database import read_mode, read_config
from papahana_flask_server_demo.config import config_collection

kcwi_acq_direct_template_properties = {
        "guider_po": {
            "title": "Pointing origin",
            "enum": ["REF", "IFU"],
            "type": "string"
        },
        "guider_gs_ra": {
            "title": "Guide Star Right Ascention",
            "minimum": 0,
            "maximum": 24,
            "type": "number",
        },
        "guider_gs_dec": {
            "title": "Guide Star Declination",
            "minimum": -90,
            "maximum": 90,
            "type": "number",
        },
        "guider_gs_mode": {
            "title": "Guide Star Selection Mode",
            "enum": ["Automatic", "Operator", "User"],
            "type": "string",
        }
}  

kcwi_acq_direct_template_schema = {
    "title": 'direct acquisition template',
    "type": 'object',
    "required": ["guider_po", "guider_gs_mode"],
    "properties": kcwi_acq_direct_template_properties
}

dither_schema = {
    "type": "object",
    "required": ["min", "max", "position", "guided"],
    "properties": {
      "min": {
          "type": "number",
          "title": "minimum",
      },
      "max": {
          "type": "number",
          "title": "maximum",
      },
      "position": {
          "type": "string",
          "enum": ["T", "S", "O"],
          "title": "telescope position",
      },
      "guided": {
          "type": "bool",
          "title": "guided",
      }
    }
}

dither_schema_array = {
	"title": "List and types of positions",
	"type": "array",
	"items": dither_schema
}

kcwi_ifu_sci_dither_properties = {
	"det1_exptime": {
        "title": "Blue exposure time for individual exposures",
	"minimum": 0,
	"maximum": 3600,
        "type": "number"
	},
	"det1_nexp": {
        "title": "Blue number of exposures per dither position",
	"minimum": 0,
	"maximum": 3600,
        "type": "integer"
	},
	"det2_exptime": {
        "title": "Red exposure time for individual exposures",
	"minimum": 0,
	"maximum": 3600,
        "type": "number"
	},
	"det2_nexp": {
        "title": "Blue number of exposures per dither position",
	"minimum": 0,
	"maximum": 3600,
        "type": "integer",
	},
	"seq_ndither": {
        "title": "Number of dither positions",
	"minimum": 0,
	"maximum": 99,
        "type": "integer",
	},
	"seq_ditarray": dither_schema_array
}

kcwi_config_properties = {
       "cfg_cam1_grating": {
            "title": "Blue Grating",
            "enum": [ "BL","BM","BH1","BH2" ],
            "type": "string",
        },
        "cfg_cam1_cwave": {
            "title": "Blue Central Wavelength",
	    "minimum": 3500,
	    "maximum": 6500,
            "type": "number",
        },
        "cfg_cam2_grating": {
            "title": "Red Grating",
            "enum": [ "RL","RM","RH1","RH2" ],
            "type": "string",
        },
        "cfg_cam2_cwave": {
            "title": "Red Central Wavelength",
	    "minimum": 6500,
	    "maximum": 10000,
            "type": "number",
        },
        "cfg_slicer": {
            "title": "Image Slicer",
            "enum": [ "Small", "Medium", "Large" ],
            "type": "string",
        }
}

kcwi_config_schema = {
        "title": "KCWI configuration",
        "type": "object",
        "required": ["cfg_slicer", "cfg_cam1_cwave", "cfg_cam1_grating"],
        "properties": kcwi_config_properties
}

kcwi_ifu_sci_dither_schema = {
        "title": "Dither Properies",
        "type": "object",
	"required": ["seq_ndither", "seq_ditarray", "det1_exptime", "det2_exptime"],
        "properties": kcwi_ifu_sci_dither_properties 
}

kcwi_ifu_sci_stare_schema = {
	"title": "stare properties",
	"type": "object",
	"required": ["det1_exptime", "det1_nexp"],
	"properties": {
		"det1_exptime": {
		"title": "Blue exposure time",
		"minimum": 0,
		"maximum": 3600,
		"type": "number",
		},
		"det1_nexp": {
		"title": "Blue number of exposures",
		"minimum": 0,
		"maximum": 3600,
		"type": "integer",
		},
		"det2_exptime": {
		"title": "Red exposure time",
		"minimum": 0,
		"maximum": 3600,
		"type": "number",
		},
		"det2_nexp": {
		"title": "Blue number of exposures",
		"minimum": 0,
		"maximum": 3600,
		"type": "integer",
		}
	}
}

kcwi_ifu_sci_dither_template = {
        "name": "KCWI_ifu_sci_dither",
        "instrument": "KCWI",
        "type": "sci",
        "version": 0.1,
	"schema": kcwi_ifu_sci_dither_schema
}

kcwi_ifu_sci_stare_template = {
        "name" : "KCWI_ifu_sci_stare",
        "instrument" : "KCWI",
        "type" : "sci",
        "version" : 0.1,
        "schema": kcwi_ifu_sci_stare_schema
}

kcwi_ifu_acq_direct_template = {
        "name": "KCWI_ifu_acq_direct",
        "instrument": "KCWI",
        "type": "acq",
        "wrap": "shortest",
        "rotmode": "stationary",
        "version": 0.1,
	"schema": kcwi_acq_direct_template_schema,
}

#TODO: Fill with separate template
kcwi_ifu_acq_offsetStar_template = kcwi_ifu_acq_direct_template.copy()
kcwi_ifu_acq_offsetStar_template['name'] = 'KCWI_ifu_acq_offsetStar'

kcwi_config_template = {
        "name": "KCWI_config",
        "instrument": "KCWI",
        "type": "config",
        "version": 0.1,
        "schema": kcwi_config_schema
}

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
        "science": [ kcwi_ifu_sci_stare_template, kcwi_ifu_sci_dither_template ],
        "configuration": [ kcwi_config_template ]
    },
}

if __name__=="__main__":
   pdb.set_trace()
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
