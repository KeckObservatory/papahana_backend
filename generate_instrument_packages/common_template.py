


dither_schema = {
    "ui_name": "Dither Pattern",
    "option": "set",
    "default": None,
    "optionality": "required",
    "type": "array",
    "allowed": [
        {"seq_dither_ra_offset": {
            "ui_name": "Right Ascension Offset",
            "option": "range",
            "allowed": [-20.0, 20.0],
            "default": None,
            "optionality": "required",
            "type": "float",
            "units": "arcseconds"
        }},
        {"seq_dither_dec_offset": {
            "ui_name": "Declination Offset",
            "option": "range",
            "allowed": [-20.0, 20.0],
            "default": None,
            "optionality": "required",
            "type": "float",
            "units": "arcseconds"
        }},
        {"seq_dither_position": {
            "ui_name": "Telescope Position",
            "option": "set",
            "allowed": ["T", "S", "O"],
            "default": None,
            "optionality": "required",
            "type": "string",
            "units": None
        }},
        {"telescope_guided": {
            "ui_name": "Guided",
            "option": "boolean",
            "default": True,
            "optionality": "required",
            "type": "boolean",
            "units": None
        }}
    ]
}