#!/usr/bin/python
# -*- coding: latin-1 -*-
import yaml

import numpy as np
import os
import pymongo
import random
import string
from itertools import product
import pprint
import pdb
from functools import wraps
import urllib
from getpass import getpass
seed = 1984739
random.seed(seed)
import datetime
from papahana_flask_server_demo.config import config_collection

INST_MAPPING = { 
                 'DEIMOS': {'DE', 'DF'},
                 'ESI': {'EI'},
                 'HIRES': {'HI'},
                 'KCWI': {'KB', 'KF'}, 
                 'LRIS': {'LB', 'LR'},
                 'MOSFIRE': {'MF'},
                 'OSIRIS': {'OI', 'OS'},
                 'NIRES': {'NR', 'NI', 'NS'},
                 'NIRC2': {'N2', 'NC'},
                }

pis = {
    "Michael Bluth": 5555,
    "Lindsay Bluth-Fünke": 7766,
    "Gob Bluth": 8877,
    "George Michael Bluth": 8899,
    "Maeby Fünke": 7799,
    "Buster Bluth": 8765,
    "Tobias Fünke": 9998,
    "George Bluth Sr.": 1144,
    "Lucille Bluth": 7644,
}

observers = [
    "Narrator",
    "Oscar Bluth",
    "Lucille Austero",
    "Barry Zuckerkorn",
    "Kitty Sanchez",
    "Steve Holt",
    "Lupe",
    "Annyong Bluth",
    "Carl Weathers",
    "Maggie Lizer",
    "Stefan Gentles",
    "Marta Estrella",
    "Cindi Lightballoon",
    "John Beard",
    "Ann Veal",
    "Wayne Jarvis",
    "Dr. Fishman",
    "Stan Sitwell",
    "Sally Sitwell",
    "Mort Meyers",
    "Starla",
    "Tony Wonder",
    "Gene Parmesan",
    "Terry Veal",
    "Rita Leeds",
    "Larry Middleman",
    "Bob Loblaw",
    "Ron Howard",
    "DeBrie Bardeaux",
    "Rebel Alley",
    "Herbert Love",
    "Marky Bark",
    "Argyle Austero",
    "Paul 'P-Hound' Huan",
    "Mark Cherry",
    "Murphy Brown Fünke",
    "Lottie Dottie Da",
    "Dusty Radler"
]

comments = [
    "Here?s some money. Go see a star war.",
    "I don?t understand the question and I won?t respond to it.",
    "I am one of the few honest people I have ever known.",
    "I?m a scholar. I enjoy scholarly pursuits.",
    "I?ve made a huge tiny mistake.",
    "I hear the jury?s still out on science.",
]

wrap_str = ['north', 'south']

status = [
    "Started",
    "Executed",
    "Completed",
    "Failed",
    "Terminated",
    "Stopped",
]

timeConstraint = [
    None, ['2021-01-01 08:00:00', '2021-01-01 10:00:00'],
    ['2021-02-02 09:00:00', '2021-02-03 18:00:00'],
    ['2021-05-01 08:00:00', '2021-06-01 10:00:00'],
    ['2021-06-01 08:00:00', '2021-06-07 10:00:00']
]

spectral_types = ['V', 'R', 'I', 'J', 'H', 'K']

sem_ids = [
  "2017A_U033",
  "2017A_U050",
  "2017B_U042",
  "2017B_U043",
  "2018A_U042",
  "2018A_U043",
  "2018A_U044",
  "2018A_U045",
  "2018B_U016",
  "2018B_U064",
  "2019A_N020",
  "2019A_U123",
  "2019A_U124",
  "2019B_U158",
  "2019B_U159",
  "2019B_U160",
  "2020A_N028",
  "2020A_U169",
  "2020B_U048",
  "2020B_U049",
  "2020B_U082",
  "2020B_N133",
  "2021A_U046",
  "2021A_U073",
  "2021A_N140",
  "2021B_U056",
  "2021B_N057"
]

kcwi_science = ['KCWI_ifu_sci_dither', 'KCWI_ifu_sci_stare']

filled_sci_templates = [
    {
        "metadata": {
            "name": "KCWI_ifu_sci_stare", "ui_name": "KCWI stare",
              "instrument": "KCWI", "type": "science", "version": 0.1,
              "script": "KCWI_ifu_sci_stare"
        },
        "properties": {
            "det1_exptime": 30,
            "det1_nexp": 4,
            "det2_exptime": 24,
            "det2_nexp": 6
        }
    },
    {
        "metadata": {
            "name": "KCWI_ifu_sci_dither",
            "ui_name": "KCWI dither",
            "instrument": "KCWI",
            "type": "science",
            "version": 0.1,
            "script": "KCWI_ifu_sci_stare"
        },
        "properties": {
            "det1_exptime": 60.0,
            "det1_nexp": 2,
            "det2_exptime": 121.0,
            "det2_nexp": 4,
            "seq_ndither": 4,
            "seq_ditarray": [
                [0, 0, 'T', True], [5, 5, 'S', False],
                [0, 0, 'T', True], [5, 5, 'S', False]
            ]
        }
    }
]

filled_acq_templates = [{
    "metadata": {
        "name": "KCWI_ifu_acq_direct",
        "ui_name": "KCWI direct",
        "instrument": "KCWI",
        "type": "acquisition",
        "version": 0.1,
        "script": "KCWI_ifu_acq_direct"},
    "properties": {
        "wrap": "auto",
        "rotmode": "PA",
        "guider_po": "IFU",
        "guider_gs_ra": "12:44:55.6",
        "guider_gs_dec": '55:22:19.9',
        "guider_gs_mode": "auto"}
}]

containers = ['Army', 'The Alliance of Magicians', 'Tantamount Studios', 'Orange County Prison', 'Milford School', 'Dr. Fünke\'s 100% Natural Good-Time Family-Band Solution']
NOBS = 100 # number of observation blocks
randContainerName = lambda: random.choice(containers)
randOBIds = lambda x=5: [int(x) for x in list(np.random.choice( range(0,NOBS+1), size=random.randint(0, x), replace=False))]


semesters = [str(x)+y for x, y in product(range(2019,2022), ['A', 'B'])]
letters = string.ascii_lowercase

# random generators 
randString = lambda x=4: ''.join(random.choice(letters) for i in range(x))
randFloat = lambda mag=10: mag * random.uniform(0,1)
randBool = lambda: bool(random.choice([0,1, None]))
randInt = lambda lr=0, ur=100: random.randint(lr, ur)
randArrStr = lambda x=1, y=1: [randString(x) for _ in range(random.randint(1, y)) ]
optionalRandString = lambda x=4: random.choice([None, randString(x)])
optionalRandArrString = lambda x, y=1: random.choice([None, randArrStr(x, y)])
sampleInst = lambda: random.choice(list(INST_MAPPING.keys()))
randPI = lambda: random.choice(list(pis))
randObserver = lambda: random.choice(observers)
randSemester = lambda: random.choice(semesters)
randSemId = lambda: random.choice(sem_ids)
randPIList = lambda x=1: lambda x=1: list(np.random.choice(list(pis), size=random.randint(1, x), replace=False))
randObserverList = lambda x=1: list(np.random.choice(observers, size=random.randint(1, x), replace=False))
randComment = lambda: random.choice(comments)
optionalRandComment = lambda: random.choice([None, randComment()])
randSemesterList = lambda x=3: list(np.random.choice(semesters, size=random.randint(0, x), replace=False))
# randStatus = lambda: random.choice(status)
rand_kcwi_science = lambda: random.choice(kcwi_science)
z_fill_number = lambda x, zf=2: str(x).zfill(2)
raDeg = z_fill_number(randInt(0, 360))
arcMinutes = z_fill_number(randInt(0, 60))
arcSeconds = z_fill_number(randInt(0, 60))

decDeg = z_fill_number(randInt(0, 90))
elevation = random.choice(['+', '-'])

def randStatus():
    rstat = random.choice(status)
    executions = []
    for x in range(0, randInt(0,6)):
        executions.append(generate_random_executions())

    schema = {'state': rstat, 'executions': executions}
    return schema


def randTimeConstraint():
    return random.choice(timeConstraint)


def generate_container(ob_blocks):
    ob_set = set()
    n_ob = random.randint(0, 9)
    for indx in range(0, n_ob):
        ob_val = random.randint(0, len(ob_blocks)-1)
        ob_set.update({ob_blocks[ob_val]})

    schema = {
        "sem_id": randSemId(),
        "name": randContainerName(),
        "observation_blocks": list(ob_set),
        "comment": randComment()
    }

    return schema


def generate_inst_package():

    schema = {
        "instrument": "KCWI",
        "version": 0.1,
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
            }],
        "templates": {
            "acquisition": [
                {"name": "KCWI_ifu_acq_direct",
                 "version": "0.1"},
                {"name": "KCWI_ifu_acq_offsetStar",
                 "version": 0.1}],
            "science": [
                {"name": "KCWI_ifu_sci_stare",
                 "version": "0.1"},
                {"name": "KCWI_ifu_sci_dither",
                 "version": 0.1}]
        },
        "configuration_parameters": [
            {"parameter": "CFG.CAM1.GRATING",
             "ui_string": "Blue Grating",
             "values": ["BL","BM","BH1","BH2"],
             "range": None,
             "type": "dropdown",
             "required": True},
            {"parameter": "CFG.CAM1.CWAVE",
             "ui_string": "Blue Central Wavelength",
             "values": None,
             "range": [3500,6500],
             "type": "continuum",
             "required": True},
            {"parameter": "CFG.CAM2.GRATING",
             "ui_string": "Red Grating",
             "values": ["RL","RM","RH1","RH2"],
             "range": None,
             "type": "dropdown",
             "required": False},
            {"parameter": "CFG.CAM2.CWAVE",
             "ui_string": "Red Central Wavelength",
             "values": None,
             "range": [6500,10000],
             "type": "continuum",
             "required": False},
            {"parameter": "CFG.SLICER",
             "ui_string": "Image Slicer",
             "values": ["Small", "Medium", "Large"],
             "range": None,
             "type": "dropdown",
             "required": True}]
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
    raDeg = z_fill_number(randInt(0, 24))
    arcMinutes = z_fill_number(randInt(0, 60))
    arcSeconds = z_fill_number(randInt(0, 60))
    ra = ":".join([raDeg, arcMinutes, arcSeconds])
    return ra


def generate_dec():
    arcMinutes = z_fill_number(randInt(0, 60))
    arcSeconds = z_fill_number(randInt(0, 60))
    decDeg = z_fill_number(randInt(0, 90))
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
            'obs_id': randObserverList(maxLen), 
            'comment': optionalRandComment()
           }


def generate_semesters(nSem, nLen=5, maxLen=6):
    return [ generate_semester(sem, nLen, maxLen) for sem in semesters[0:nSem] ]


def generate_mag(nLen=2):
    return {'band': spectral_types[random.randint(0, len(spectral_types)-1)],
            'mag': randFloat(nLen)}


def generate_mags(maxMags=2):
    return [ generate_mag() for _ in range( random.randint( 1, maxMags ) ) ]


@remove_none_values_in_dict
def generate_observation(nLen, maxArr):
    '''not used atm'''
    schema = {
        'instrument': sampleInst(),
        'exposure_sequences': randArrStr(nLen, maxArr),
        'associations': randArrStr(nLen, maxArr),
        'comment': optionalRandComment()
    }
    return schema


@remove_none_values_in_dict
def generate_metadata(maxArr):
    pi_name = randPI()
    schema = {
        'name': 'standard stars #' + str(random.randint(0, 9)),
        'pi_id': pis[pi_name],
        'sem_id': str(randSemId()),
        'instrument': 'KCWI',
        'comment': optionalRandComment()
    }
    return schema


@remove_none_values_in_dict
def generate_program(container_list):
    observers = []
    for i in range(0, random.randint(0, 9)):
        pi_name = randPI()
        observers.append(pis[pi_name])

    pi_name = str(randPI())
    while pi_name in observers:
        observers.remove(pi_name)

    ob_set = set()
    n_ob = random.randint(0, 9)
    for indx in range(0, n_ob):
        ob_val = random.randint(0, len(container_list)-1)
        ob_set.update({container_list[ob_val]})

    schema = {
        'name': 'Program #' + str(random.randint(0, 99)),
        'sem_id': str(randSemId()),
        'container_list': list(ob_set),
        'comment': optionalRandComment()
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


def generate_kcwi_science():
    import copy

    schema = []
    n_templates = random.randint(0, 5)
    for indx in range(1, n_templates):
        tmp_list = copy.deepcopy(filled_sci_templates)
        filled_template = random.choice(tmp_list)
        filled_template['template_index'] = indx
        schema.append(filled_template)

    return schema


def generate_kcwi_acquisiton(nLen, maxArr):
    acq = random.choice(filled_acq_templates)
    acq['template_index'] = 0
    return acq


def generate_science(inst='KCWI'):
    if inst=='KCWI':
        schema = generate_kcwi_science()
    else:
        schema = generate_kcwi_science() # fill this in later
    return schema


def generate_acquisition(nLen, maxArr, inst='KCWI'):
    if inst=='KCWI':
        schema = generate_kcwi_acquisiton(nLen, maxArr)
    else:
        schema = {
            'instrument_setup': randString(),
            'acquisition_method': randString(),
            'guider_selection': optionalRandString(),
            'ao_modes': optionalRandArrString(nLen, maxArr),
            'offset_stars': optionalRandArrString(nLen, maxArr),
            'slitmasks': optionalRandArrString(nLen, maxArr),
            'position_angles': optionalRandArrString(nLen, maxArr),
            'comment': optionalRandComment()
        }
    return schema


def generate_random_executions():
    rdate = random_dates()
    random_time = datetime.datetime.now().replace(hour=random.randint(0, 23),
                                                  minute=random.randint(0, 59))

    random_date = f'{(rdate)} {random_time.strftime("%H:%M:%S")}'

    return random_date


@remove_none_values_in_dict
def generate_target():
    schema = {
        'name': randString(), 
        'ra': generate_ra(), 
        'dec': generate_dec(), 
        'equinox': randFloat(), 
        'frame': randString(), 
        'ra_offset': randFloat(), 
        'dec_offset': randFloat(),
        'pa': randFloat(),
        'pm_ra': randFloat(), 
        'pm_dec': randFloat(), 
        'epoch': randFloat(), 
        'obstime': randFloat(), 
        'mag': generate_mags(), 
        'wrap': wrap_str[random.randint(0, 1)],
        'd_ra': randFloat(), 
        'd_dec': randFloat(), 
        'comment': optionalRandComment()
    }
    return schema


@remove_none_values_in_dict
def generate_observation_block(nLen, maxArr, inst='KCWI', _id=None):
    schema = {
        'metadata': generate_metadata(maxArr),
        'version': 0.1,
        'target': random.choice([None, generate_target()]),
        'acquisition': generate_acquisition(nLen, maxArr, inst),
        'science': generate_science(inst),
        'associations': randArrStr(nLen, maxArr),
        'priority': randFloat(100),
        'status': randStatus(),
        'time_constraints': randTimeConstraint(),
        'comment': optionalRandComment()
    }
    if _id:
        schema['_id'] = _id
    return schema


def read_mode(config='config.live.yaml'):
    with open(config) as file:
        mode_dict = yaml.load(file, Loader=yaml.FullLoader)['mode']

    mode = mode_dict['config']

    return mode


def read_config(mode, config='config.live.yaml'):
    with open(config) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)[mode]

    return config


if __name__=='__main__':
    seed = 1984739
    random.seed(seed)
    dbName = 'papahana'
    mode = 'dev'
    
    # Create ob_blocks collection
    collName = 'ob_blocks'
    remote = True # run on remote server (n)
    mode = read_mode()
    config = read_config(mode)
    coll = config_collection('obCollect', mode=mode, conf=config)
    coll.drop()
    coll.create_index([('metadata.pi', pymongo.DESCENDING)])
    coll.create_index([('metadata.semester', pymongo.DESCENDING)])
    coll.create_index([('metadata.program', pymongo.DESCENDING)])
    nLen = 5
    maxArr = 5
    inst = 'KCWI'
    ob_blocks = []
    print("...generating OBs")
    for idx in range(NOBS):
        doc = generate_observation_block(nLen, maxArr, inst)
        result = coll.insert_one(doc)
        ob_blocks.append(str(result.inserted_id))

    # Create containers collection
    collName = 'containers'
    remote = True # run on remote server (n)
    coll = config_collection('containerCollect', mode=mode, conf=config)
    coll.drop()
    print("...generating containers")
    nContainers = 20
    container_list = []
    for idx in range(nContainers):
        doc = generate_container(ob_blocks)
        result = coll.insert_one(doc)

        container_list.append(str(result.inserted_id))

    # # create Template collection
    # collName = 'templates'
    # remote = True # run on remote server (n)
    # coll = config_collection('templateCollect', mode=mode, conf=config)
    # coll.drop()
    # print("...generating templates")
    # for template in science_templates:
    #     result = coll.insert_one(template)
    #
    # for template in acquisition_templates:
    #     result = coll.insert_one(template)

    colName = 'instrument_packages'
    coll = config_collection('instCollect', mode=mode, conf=config)
    coll.drop()
    print("...generating instrument package")
    ip = generate_inst_package()
    result = coll.insert_one(ip)
