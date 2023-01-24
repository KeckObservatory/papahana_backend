import generate_utils as utils
import generate_random_utils as random_utils
import random

def generate_mag(nLen=2):
    return {'target_info_band': random_utils.spectral_types[random.randint(0, len(random_utils.spectral_types)-1)],
            'target_info_mag': random_utils.randFloat(nLen)}


def generate_ra():
    raDeg = random_utils.z_fill_number(random_utils.randInt(0, 24))
    arcMinutes = random_utils.z_fill_number(random_utils.randInt(0, 60))
    arcSeconds = random_utils.z_fill_number(random_utils.randInt(0, 60))
    ra = ":".join([raDeg, arcMinutes, arcSeconds])
    return ra


def generate_dec():
    arcMinutes = random_utils.z_fill_number(random_utils.randInt(0, 60))
    arcSeconds = random_utils.z_fill_number(random_utils.randInt(0, 60))
    decDeg = random_utils.z_fill_number(random_utils.randInt(0, 90))
    elevation = random.choice(['+', '-'])
    dec = elevation+":".join([decDeg, arcMinutes, arcSeconds])
    return dec


def generate_sidereal_target():
    schema = {
        "metadata": {
            "name": "sidereal_target",
            "ui_name": "Sidereal Target",
            "template_type": "target",
            "version": "0.1.1"
        },
        "parameters": {
            'target_info_name': random_utils.randString(),
            'target_coord_ra': generate_ra(),
            'target_coord_dec': generate_dec(),
            'rot_cfg_pa': random_utils.randFloat(),
            'target_coord_pm_ra': random_utils.randFloat(),
            'target_coord_pm_dec': random_utils.randFloat(),
            'target_coord_epoch': '2000',
            'target_coord_frame': 'FK5',
            'seq_constraint_obstime':  '2021-04-22 15:08:04',
            'target_info_magnitude': generate_mag(),
            'target_info_comment': random_utils.optionalRandComment()
        }
    }

    return schema


def generate_nonsidereal_target():
    schema = generate_sidereal_target()
    schema['metadata']['name'] = "non_sidereal_target"
    schema['parameters']['target_coord_dra'] = random_utils.randFloat()
    schema['parameters']['target_coord_ddec']: random_utils.randFloat()

    return schema


def generate_kpf_target():
    schema = {
        "metadata": {
            "instrument": "KPF",
            "name": "kpf_target",
            "template_type": "target",
            "ui_name": "KPF Target",
            "version": "0.1.0"
        },
        "parameters": {
            "target_info_name": "My KPF Target",
            "target_info_comment": "A planet with life!",
            "target_info_2mass_id": "2mass",
            "target_info_gaia_id": "gaia",
            "target_info_gmag": 24.4,
            "target_info_jmag": 11.2,
            "target_coord_parallax": 30000.0,
            "target_coord_rv": 10.3,
            "target_info_teff": 334.4,
            "target_coord_ra": generate_ra(),
            "target_coord_dec": generate_dec(),
            "target_coord_pm_ra": 0.1,
            "target_coord_pm_dec": 1.2,
            "target_coord_frame": "FK5",
            "target_coord_epoch": 2000.0,
            "rot_cfg_pa": 359.0,
            "seq_constraint_obstime": None
        }
    }

    return schema

# def generate_mos_target():
#     schema = generate_sidereal_target()
#     schema['parameters']['inst_cfg_mask_name'] = "Science Mask 101"
#     schema['parameters']['inst_cfg_mask_barcode'] = "H01830928"
#
#     return schema
