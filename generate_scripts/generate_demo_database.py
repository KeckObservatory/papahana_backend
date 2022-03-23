#!/usr/bin/python
# -*- coding: latin-1 -*-

import random
import string
from functools import wraps
seed = 1984739
random.seed(seed)
import datetime

import generate_utils as utils
import generate_random_utils as random_utils
import generate_template
from papahana import util as papahana_util
from bson.objectid import ObjectId

kcwi_science = ['KCWI_ifu_sci_dither', 'KCWI_ifu_sci_stare']


def filled_sci_templates(template_list):
    templates_version = parse_templates_version(template_list)


    sci_templates = [
        {
            "metadata": {
                "name": "KCWI_ifu_sci_stare",
                "ui_name": "KCWI stare",
                "instrument": "KCWI",
                "template_type": "science",
                "version": templates_version["KCWI_ifu_sci_stare"],
                "script": "KCWI_ifu_sci_stare",
                "sequence_number": 1
            },
            "parameters": {
                "det1_exp_time": 30,
                "det1_exp_number": 4,
                "det2_exp_time": 24,
                "det2_exp_number": 5
            }
        },
        {
            "metadata": {
                "name": "KCWI_ifu_sci_dither",
                "ui_name": "KCWI dither",
                "instrument": "KCWI",
                "template_type": "science",
                "version": templates_version["KCWI_ifu_sci_dither"],
                "script": "KCWI_ifu_sci_dither",
                "sequence_number": 1
            },
            "parameters": {
                "det1_exp_time": 60.0,
                "det1_exp_number": 12,
                "det2_exp_time": 121.0,
                "det2_exp_number": 6,
                "seq_dither_number": 4,
                "seq_dither_pattern": [
                    {"seq_dither_ra_offset": 0, "seq_dither_dec_offset": 0,
                     "seq_dither_position": 'T', "seq_dither_guided": True},
                    {"seq_dither_ra_offset": 5, "seq_dither_dec_offset": 5,
                     "seq_dither_position": 'S', "seq_dither_guided": False},
                    {"seq_dither_ra_offset": 0, "seq_dither_dec_offset": 0,
                     "seq_dither_position": 'T', "seq_dither_guided": True},
                    {"seq_dither_ra_offset": 5, "seq_dither_dec_offset": 5,
                     "seq_dither_position": 'S', "seq_dither_guided": False}
                ]
            }
        }
    ]

    return sci_templates

filled_acq_templates = [{
    "metadata": {
        "name": "KCWI_ifu_acq_direct",
        "ui_name": "KCWI direct",
        "instrument": "KCWI",
        "type": "acquisition",
        "version": "0.1.1",
        "script": "KCWI_ifu_acq_direct",
        "sequence_number" : 0},
    "parameters": {
        "rot_cfg_wrap": "auto",
        "rot_cfg_mode": "PA",
        "tcs_coord_po": "IFU",
        "tcs_coord_raoff": "0",
        "tcs_coord_decoff": '1',
        "guider1_coord_ra": "12:44:55.6",
        "guider1_coord_dec": '55:22:19.9',
        "guider1_coord_mode": 'operator'
    }
}]


def randStatus():
    executions = []
    for x in range(0, random_utils.randInt(0,6)):
        executions.append(generate_random_executions())

    schema = {'state': random_utils.randInt(0,4),
              'priority': random_utils.randInt(0,100),
              'current_seq': random_utils.randInt(0, 6),
              'current_step': random_utils.randInt(0, 4),
              'current_exp_det1': random_utils.randInt(0, 4),
              'current_exp_det2': random_utils.randInt(0, 4),
              'executions': executions,
              'deleted': False}
    return schema


def randTimeConstraint():
    return random.choice(random_utils.timeConstraint)


def generate_container(ob_blocks):
    ob_set = set()
    n_ob = random.randint(0, 9)
    for indx in range(0, n_ob):
        ob_val = random.randint(0, len(ob_blocks)-1)
        ob_set.update({ob_blocks[ob_val]})

    schema = {
        "sem_id": random_utils.randSemId(),
        "name": random_utils.randContainerName(),
        "observation_blocks": list(ob_set),
        "comment": random_utils.randComment()
    }

    return schema


# todo add two versions
def generate_inst_package(template_list):

    # for on_id in ob_blocks:
    #     template_name =

    schema = {
        "metadata": {
            "name": "kcwi_instrument_package",
            "ui_name": "KCWI Instrument Package",
            "version": "0.1.0",
            "instrument": "KCWI",
            "observing_modes": ["imaging", "ifu"]
        },
        "optical_parameters" : {
            "field_of_view" : [1200, 1200],
            "slit_length" : 4
        },
        "guider" : {
            "name" : "Guider",
            "fov" : [120, 120],
            "pixel_scale" : 0.17,
            "pa_offset" : 'null',
            "read_noise" : 'null',
            "gain" : 'null',
            "zero_points" : 'null',
            "sensitivity" : 'null',
            "filters" : 'null'
        },
        "configurable_elements" : [
            "inst_cfg_slicer",
            "inst_cfg_hatch",
            "inst_cfg_calib",
            "inst_cfg_polarimeter",
            "inst_cfg_ifu",
            "inst_cfg1_filter",
            "inst_cfg1_grating",
            "inst_cfg1_blockingfilter",
            "inst_cfg2_filter",
            "inst_cfg2_grating",
            "inst_cfg2_blockingfilter",
            "inst_ns_mask",
            "inst_ns_direction",
            "inst_kmirror_mode",
            "inst_kmirror_angle",
            "inst_det1_focus",
            "inst_det2_focus",
            "inst_wavelengt1_central",
            "inst_wavelength1_peak"
            "inst_wavelength2_central",
            "inst_wavelength2_peak"
            "det1_mode_binning",
            "det1_mode_amp",
            "det1_mode_read",
            "det1_mode_gain",
            "det2_mode_binning",
            "det2_mode_amp",
            "det2_mode_read",
            "det2_mode_gain",
        ],
        "pointing_origins" : [
            "IFU",
            "REF",
            "Imaging"
        ],
        "template_list": parse_templates_version(template_list),
        # "common_parameters": ObjectId("61203d3a86574cd1da879135")
        "event_table" : 'null',
        "comment" : "A KCWI Instrument Package"
    }

    return schema


def parse_templates(template_list):
    schema = {}
    for template in template_list:
        obj_id = str(template["_id"])
        schema[template["metadata"]["name"]] = obj_id

    return schema


def parse_templates_version(template_list):
    schema = {}
    for template in template_list:
        version = template["metadata"]["version"]
        schema[template["metadata"]["name"]] = version

    return schema



def generate_observer_collection(coll):
    n_obs = 15

    keck_id_list = set()
    for obs in range(0, n_obs):
        keck_id_list.add(random_utils.randKeckId())

    for obs_id in keck_id_list:
        sem_id_list = []
        for indx in range(0,random_utils.randInt(2,10)):
            sem_id_list.append(random_utils.randSemId())

        print(sem_id_list)
        akey = random_utils.randInt(10000000, 100000000)
        doc = {'keck_id': obs_id, "api_key": akey, "associations": sem_id_list}
        _ = coll.insert_one(doc)

    # create admin observer
    coll = papahana_util.config_collection('obCollect', conf=config)

    fields = {'metadata.sem_id': 1, '_id': 0}
    sem_ids = list(coll.find({}, fields))
    assoc_list = []
    for result in sem_ids:
        assoc_list.append(result['metadata']['sem_id'])

    coll = papahana_util.config_collection('observerCollect', conf=config)
    doc = {'keck_id': 0000, "api_key": akey, "associations": assoc_list}
    _ = coll.insert_one(doc)

    return


def generate_common_parameters():
    schema = {"metadata":
                  {"name": "kcwi_common_parameters",
                   "ui_name": "KCWI Common parameters",
                   "instrument": "KCWI",
                   "template_type": "common_parameters",
                   "version": "0.1.1", },
              "instrument_parameters": {
                  "inst_cfg_slicer": "slicer1",
                  "inst_cfg_blockingfilter": "filter1",
                  "inst_cfg_calib": "Sky",
                  "inst_cfg_hatch": "open",
                  "inst_cfg_polarimeter": "Sky",
                  "inst_cfg_ifu": "Large",
                  "inst_cfg1_filter": "Large",
                  "inst_cfg2_filter": "Medium",
                  "inst_cfg1_grating": "BH3",
                  "inst_cfg2_grating": "RH3",
                  "inst_ns_mask": "open",
                  "inst_ns_direction": 1,
                  "inst_kmirror_mode": "Tracking",
                  "inst_kmirror_angle": 122,
                  "inst_wavelength1_central": 450,
                  "inst_wavelength2_central": 789,
                  "inst_wavelength1_peak": 470,
                  "inst_wavelength2_peak": 800
              },
            "detector_parameters": {
                  "det1_mode_binning": '1x1',
                  "det2_mode_binning": '1x1',
                  "det1_mode_amp": 0,
                  "det2_mode_amp": 5,
                  "det1_mode_read": 0,
                  "det2_mode_read": 1,
                  "det1_mode_gain": 2,
                  "det2_mode_gain": 5
            },
            "tcs_parameters": {

            }

    }

    return schema

def random_dates():
    start_date = datetime.date(2018, 1, 1)
    end_date = datetime.date(2021, 2, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date


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


def remove_none_values_in_dict(method):
    """
    None values in dict returned by method are removed
    """

    @wraps(method)
    def remove_none(*args, **kw):
        result = method(*args, **kw)
        if type(result) is dict:
            return {key: val for key, val in result.items() if val is not None}
        else:
            return result
    return remove_none


def generate_semester(sem, nLen, maxLen=6):
    return {'_id': sem,
            'semester': sem,
            'obs_id': random_utils.randObserverList(maxLen),
            'comment': random_utils.optionalRandComment()
           }


def generate_semesters(nSem, nLen=5, maxLen=6):
    return [generate_semester(sem, nLen, maxLen) for sem in random_utils.semesters[0:nSem]]


def generate_mag(nLen=2):
    return {'target_info_band': random_utils.spectral_types[random.randint(0, len(random_utils.spectral_types)-1)],
            'target_info_mag': random_utils.randFloat(nLen)}


def generate_mags(maxMags=2):
    return [ generate_mag() for _ in range(random.randint(1, maxMags)) ]


@remove_none_values_in_dict
def generate_observation(nLen, maxArr):
    '''not used atm'''
    schema = {
        'instrument': random_utils.sampleInst(),
        'exposure_sequences': random_utils.randArrStr(nLen, maxArr),
        'associations': random_utils.randArrStr(nLen, maxArr),
        'comment': random_utils.optionalRandComment()
    }
    return schema


@remove_none_values_in_dict
def generate_metadata(maxArr):
    pi_name = random_utils.randPI()
    schema = {
        'name': 'standard stars #' + str(random.randint(0, 9)),
        'version': '0.1.0',
        'priority': random_utils.randInt(100),
        'ob_type': 'science',
        'pi_id': random_utils.pis[pi_name],
        'sem_id': str(random_utils.randSemId()),
        'instrument': 'KCWI',
        'comment': random_utils.optionalRandComment()
    }
    return schema


@remove_none_values_in_dict
def generate_program(container_list):
    observers = []
    for i in range(0, random.randint(0, 9)):
        pi_name = random_utils.randPI()
        observers.append(random_utils.pis[pi_name])

    pi_name = str(random_utils.randPI())
    while pi_name in observers:
        observers.remove(pi_name)

    ob_set = set()
    n_ob = random.randint(0, 9)
    for indx in range(0, n_ob):
        ob_val = random.randint(0, len(container_list)-1)
        ob_set.update({container_list[ob_val]})

    schema = {
        'name': 'Program #' + str(random.randint(0, 99)),
        'sem_id': str(random_utils.randSemId()),
        'container_list': list(ob_set),
        'comment': random_utils.optionalRandComment()
    }
    return schema


def generate_dither():
    dmin, dmax = [random.randint(-15, 15), random.randint(-15, 15)].sort()
    schema = {
        'min': dmin,
        'max': dmax,
        'letter': random.choice(string.ascii_lowercase).upper(),
        'guide': 'Guided'
    }
    return schema


def generate_kcwi_science(template_list):
    import copy

    schema = []
    n_templates = random.randint(0, 5)
    for indx in range(0, n_templates):
        filed_sci = filled_sci_templates(template_list)
        tmp_list = copy.deepcopy(filed_sci)
        filled_template = random.choice(tmp_list)
        filled_template['metadata']['sequence_number'] = indx+1
        schema.append(filled_template)

    return schema


def generate_kcwi_acquisiton(nLen, maxArr):
    acq = random.choice(filled_acq_templates)

    return acq



def generate_acquisition(nLen, maxArr, inst='KCWI'):
    if inst=='KCWI':
        schema = generate_kcwi_acquisiton(nLen, maxArr)
    else:
        schema = {
            'instrument_setup': random_utils.randString(),
            'acquisition_method': random_utils.randString(),
            'guider_selection': random_utils.optionalRandString(),
            'ao_modes': random_utils.optionalRandArrString(nLen, maxArr),
            'offset_stars': random_utils.optionalRandArrString(nLen, maxArr),
            'slitmasks': random_utils.optionalRandArrString(nLen, maxArr),
            'position_angles': random_utils.optionalRandArrString(nLen, maxArr),
            'comment': random_utils.optionalRandComment()
        }
    return schema


def generate_random_executions():
    rdate = random_dates()
    random_time = datetime.datetime.now().replace(hour=random.randint(0, 23),
                                                  minute=random.randint(0, 59))

    random_date = f'{rdate} {random_time.strftime("%H:%M:%S")}'

    return random_date



@remove_none_values_in_dict
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


@remove_none_values_in_dict
def generate_nonsidereal_target():
    schema = generate_sidereal_target()
    schema['target_coord_dra'] = random_utils.randFloat()
    schema['target_coord_ddec']: random_utils.randFloat()

    return schema

@remove_none_values_in_dict
def generate_mos_target():
    schema = generate_sidereal_target()
    schema['inst_cfg_mask_name'] = "Science Mask 101"
    schema['inst_cfg_mask_barcode'] = "H01830928"

    return schema


@remove_none_values_in_dict
def generate_observation_block(nLen, maxArr, template_list, inst='KCWI', _id=None):
    schema = {
        'metadata': generate_metadata(maxArr),
        'target': random.choice([None, generate_sidereal_target(),
                                 generate_nonsidereal_target(),
                                 generate_mos_target()]),
        'acquisition': generate_acquisition(nLen, maxArr, inst),
        'observations': generate_kcwi_science(template_list),
        'associations': random_utils.randArrStr(nLen, maxArr),
        'status': randStatus(),
        'common_parameters': generate_common_parameters(),
        'comment': random_utils.optionalRandComment()
    }
    if _id:
        schema['_id'] = _id
    return schema


def generate_scripts(script_name, stype):

    schema = {
        'metadata': {
            'name': script_name,
            'version': '0.1.0',
            'instrument': 'KCWI',
            'script_type': stype,
            'comment': random_utils.optionalRandComment()
        },
        'script': {'TBD': 'TBD'}
    }

    return schema


def make_status_realistic(ob):
    coll = papahana_util.config_collection('obCollect', conf=config)
    fields = {'observations.metadata.sequence_number': 1}

    ob_info = list(coll.find({"_id": ObjectId(ob)}, fields))
    # if ob_info:
    #     ob_info = ob_info[0]
    print("ob info", ob_info)

    for ob_seq in ob_info:
        print("onseq", ob_seq)
        oid = ob_seq['_id']
        seq_n = 0
        for seq in ob_seq['observations']:
            print("seq", seq)
            cur_n = seq['metadata']['sequence_number']
            if cur_n > seq_n:
                seq_n = cur_n

        current_seq = random_utils.randInt(0,seq_n)
        coll.update_one({'_id': oid}, {'$set': {'status.current_seq': current_seq}})

        fields = {'observations': 1}
        observations = list(coll.find({"_id": ObjectId(ob)}, fields))
        if observations:
            observations = observations[0]

        # update the step, exp_n to match the sequence
        n_steps = 0
        n_exp_det1 = 0
        n_exp_det2 = 0
        for obs in observations['observations']:

            cur_n = obs['metadata']['sequence_number']
            if cur_n == current_seq:
                try:
                    n_exp_det1 = obs['parameters']['det1_exp_number']
                except:
                    pass

                if 'det2_exp_number' in obs['parameters']:
                    n_exp_det2 = obs['parameters']['det2_exp_number']


                if 'seq_dither_number' in obs['parameters']:
                    n_steps = obs['parameters']['seq_dither_number']

                break

        # zero based
        current_step = random_utils.randInt(0, max(n_steps-1, 0))
        current_exp_det1 = random_utils.randInt(0, max(n_exp_det1-1, 0))
        current_exp_det2 = random_utils.randInt(0, max(n_exp_det2-1, 0))

        coll.update_one({'_id': oid},
                        {'$set': {'status.current_step': current_step}})
        coll.update_one({'_id': oid},
                        {'$set': {'status.current_exp_det1': current_exp_det1}})
        coll.update_one({'_id': oid},
                        {'$set': {'status.current_exp_det2': current_exp_det2}})


if __name__=='__main__':
    args = utils.parse_args()
    mode = args.mode

    seed = 1984739
    random.seed(seed)

    config = utils.read_config(mode)
    print(f"Using {config['dbName']} database")


    # generate templates - returns [{'_id': ObjectId('622ff5db24d4e9afb8e2872c'), ..]
    template_list = generate_template.generate_templates()
    print(template_list)

    # # Create ob_blocks collection
    print("...generating OBs")
    coll = papahana_util.config_collection('obCollect', conf=config)
    coll.drop()
    nLen = 5
    maxArr = 5
    inst = 'KCWI'
    ob_blocks = []
    for idx in range(random_utils.NOBS):
        doc = generate_observation_block(nLen, maxArr, template_list, inst)
        result = coll.insert_one(doc)
        ob_blocks.append(str(result.inserted_id))

    for ob in ob_blocks:
        make_status_realistic(ob)

    # Create containers collection
    print("...generating containers")
    coll = papahana_util.config_collection('containerCollect', conf=config)
    coll.drop()
    nContainers = 20
    container_list = []
    for idx in range(nContainers):
        doc = generate_container(ob_blocks)
        result = coll.insert_one(doc)
        container_list.append(str(result.inserted_id))

    # # generate templates - returns [{'_id': ObjectId('622ff5db24d4e9afb8e2872c'), 'metadata': {'name': 'KCWI_ifu_acq_offsetStar'}}, {'_id': ObjectId('622ff5db24d4e9afb8e2872d'), 'metadata': {'name': 'KCWI_ifu_acq_direct'}}, {'_id': ObjectId('622ff5db24d4e9afb8e2872e'), 'metadata': {'name': 'KCWI_ifu_sci_stare'}},
    # template_list = generate_template.generate_templates()
    # print(template_list)

    # # Create Instrument collection
    print("...generating instrument package")
    coll = papahana_util.config_collection('ipCollect', conf=config)
    coll.drop()
    ip = generate_inst_package(template_list)
    result = coll.insert_one(ip)

    # Create script collection
    print("...generating scripts")
    script_names = {'KCWI_ifu_acq_direct': 'acquisition',
                    'KCWI_ifu_acq_direct': 'acquisition',
                    'KCWI_ifu_sci_stare': 'science',
                    'KCWI_ifu_sci_stare': 'science'}

    coll = papahana_util.config_collection('scriptCollect', conf=config)
    coll.drop()
    for name, stype in script_names.items():
        script_schema = generate_scripts(name, stype)
        result = coll.insert_one(script_schema)


    # Create observer collection
    print("...generating observers")

    coll = papahana_util.config_collection('observerCollect', conf=config)
    coll.drop()
    generate_observer_collection(coll)

    # for idx in range(NOBS):
    #     doc = generate_observer_collection()
    #     result = coll.insert_one(doc)

