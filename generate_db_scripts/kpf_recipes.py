

def generate_recipes():
    recipes = {}

    recipes["science_sidereal_target"] = {
        "metadata": {
                "name": "science_sidereal_target",
                "ob_type": "science",
                "ui_name": "Sidereal Science Target",
                "instrument": "KPF"
        },
        "recipe": [
            "kpf_common_parameters",
            "kpf_acq",
            "kpf_sci",
            "sideriel_target"
        ]
    }

    recipes["science_non_sidereal_target"] = {
        "metadata": {
                "name": "science_non_sidereal_target",
                "ob_type": "science",
                "ui_name": "Non Sidereal Science Target",
                "instrument": "KPF"
        },
        "recipe": [
            "kpf_common_parameters",
            "kpf_acq",
            "kpf_sci",
            "non_sideriel_target"
        ]
    }

    recipes["science_kpf_target"] = {
        "metadata": {
                "name": "science_kpf_target",
                "ob_type": "science",
                "ui_name": "KPF Science Target",
                "instrument": "KPF"
        },
        "recipe": [
            "kpf_common_parameters",
            "kpf_acq",
            "kpf_sci",
            "kpf_target"
        ]
    }

    recipes["calibration_dark"] = {
        "metadata": {
                "name": "calibration_dark",
                "ob_type": "calibration",
                "ui_name": "Dark Calibration",
                "instrument": "KPF"
        },
        "recipe": [
            "kpf_common_parameters",
            "kpf_dark"
        ]
    }

    recipes["calibration_arcs"] = {
        "metadata": {
                "name": "calibration_arcs",
                "ob_type": "calibration",
                "ui_name": "Arc Calibration",
                "instrument": "KPF"
        },
        "recipe": [
            "kpf_common_parameters",
            "kpf_arcs"
        ]
    }

    return recipes

