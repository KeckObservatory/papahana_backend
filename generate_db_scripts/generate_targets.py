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
            "name": "multi_object_target",
            "ui_name": "Multi-Object Spectroscopy Target",
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
    schema['parameters']['target_coord_dra'] = random_utils.randFloat()
    schema['parameters']['target_coord_ddec']: random_utils.randFloat()

    return schema


def generate_mos_target():
    schema = generate_sidereal_target()
    schema['parameters']['inst_cfg_mask_name'] = "Science Mask 101"
    schema['parameters']['inst_cfg_mask_barcode'] = "H01830928"

    return schema