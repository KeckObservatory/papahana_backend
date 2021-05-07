import numpy as np
from controller_helper import *
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

pis = [
"Michael Bluth",
"Lindsay Bluth-Fünke",
"Gob Bluth",
"George Michael Bluth",
"Maeby Fünke",
"Buster Bluth",
"Tobias Fünke",
"George Bluth Sr.",
"Lucille Bluth",
]

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
"Here’s some money. Go see a star war.",
"I don’t understand the question and I won’t respond to it.",
"I am one of the few honest people I have ever known.",
"I’m a scholar. I enjoy scholarly pursuits.",
"I’ve made a huge tiny mistake.",
"I hear the jury’s still out on science.",
]

status = [
    "undefined", 
    "its complicated",
    "completed", 
    "broken",
    "invalid",
    "progressing",
    "inqueue",
]

groups = ['Army', 
          'The Alliance of Magicians', 
          'Tantamount Studios', 
          'Orange County Prison', 
          'Milford School', 
          'Dr. Fünke\'s 100% Natural Good-Time Family-Band Solution'
]


kcwi_science = ['KCWI_ifu_sci_dither', 'KCWI_ifu_sci_stare']
semesters = [str(x)+y for x, y in product(range(2000,2004), ['A', 'B'])]
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
randPI = lambda: random.choice(pis)
randObserver = lambda: random.choice(observers)
randSemester = lambda: random.choice(semesters)
randPIList = lambda x=1: lambda x=1: list(np.random.choice(pis, size=random.randint(1, x), replace=False))
randObserverList = lambda x=1: list(np.random.choice(observers, size=random.randint(1, x), replace=False))
randComment = lambda: random.choice(comments)
optionalRandComment = lambda: random.choice([None, randComment()])
randStatus = lambda: random.choice(status)
rand_kcwi_science = lambda: random.choice(status)
z_fill_number = lambda x, zf=2: str(x).zfill(2)
raDeg = z_fill_number(randInt(0, 360))
arcMinutes = z_fill_number(randInt(0, 60))
arcSeconds = z_fill_number(randInt(0, 60))

decDeg = z_fill_number(randInt(0, 90))
elevation = random.choice(['+', '-'])
randGroupName = lambda: random.choice(groups)
randOBIds = lambda x=5: [int(x) for x in list(np.random.choice( range(0,nOb+1), size=random.randint(0, x), replace=False))]

def generate_group(_id=None):
    schema = {
        "semester": randSemester(),
        "name": randGroupName(),
        "comment": randComment(),
        "observation_blocks": randOBIds()
    }
    if _id:
        schema['_id'] = _id
    return schema

def generate_ra():
    raDeg = z_fill_number(randInt(0, 360))
    arcMinutes = z_fill_number(randInt(0, 60))
    arcSeconds = z_fill_number(randInt(0, 60))
    ra = " ".join([raDeg, arcMinutes, arcSeconds])
    return ra

def generate_dec():
    arcMinutes = z_fill_number(randInt(0, 60))
    arcSeconds = z_fill_number(randInt(0, 60))
    decDeg = z_fill_number(randInt(0, 90))
    elevation = random.choice(['+', '-'])
    dec = elevation+" ".join([decDeg, arcMinutes, arcSeconds])
    return dec

def remove_none_values_in_dict(method):
    '''None values in dict returned by method are removed
    '''
    @wraps(method)
    def remove_none(*args, **kw):
        result = method(*args, **kw)
        return {key: val for key, val in result.items() if val is not None}
    return remove_none

def generate_semester(sem, nLen, maxLen=6):
    return {'_id': sem,
            'semester': sem,
            'obs_id': randObserverList(maxLen), 
            'comment': optionalRandComment()
           }

def generate_semesters(nSem, nLen=5, maxLen=6):
    return [ generate_semester(sem, nLen, maxLen) for sem in semesters[0:nSem] ]

@remove_none_values_in_dict
def generate_mag(nLen=2):
    return {'band': randString(nLen), 'mag': randFloat(nLen), 'comment': optionalRandComment()}

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
def generate_signature(maxArr):
    schema = {
        'pi': randPI(),
        'semester': randSemester(),
        'program': random.randint(0, 10),
        'observers': randObserverList(maxArr),
        'group': random.randint(0,3),
        'comment': optionalRandComment()
    }
    return schema

def generate_dither():
    dmin, dmax = [random.randint(-15, 15), random.randint(-15, 15)].sort()
    schema = {
        'min': dmin,
        'max': dmax,
        'letter': random.choice(string.lower_case).upper(),
        'guide': 'Guided'
    }
    return schema

@remove_none_values_in_dict
def generate_kcwi_science(nLen, maxArr):
    name = rand_kcwi_science()
    cam = random.choice([ "BL","BM","BH1","BH2", "RL","RM","RH1","RH2"])
    camIsBlue = cam[0] is 'B'
    cwave = random.randint(3500, 6500) if camIsBlue else random.randint(6500, 10000)
    schema = {
        "name": name,
        "version": "0.1",
        "det1_exptime": random.randint(0,3600),
        "det1_nexp": random.randint(0,99),
        "det2_exptime": random.randint(0,3600),
        "det2_next": random.randint(0,99),
        "cfg_cam_grating": random.choice([ "BL","BM","BH1","BH2", "RL","RM","RH1","RH2" ]),
        "cfg_cam_cwave": random.randint(6500,10000),
        "cfg_slicer": random.choice(["Small", "Medium", "Large"])
    }
    if 'dither' in name:
        schema["SEQ.DITARRAY"] = generate_dither()
        schema["SEQ.NDITHER"] = random.randint(0,99)
    return schema


def generate_kcwi_acquisiton(nLen, maxArr):
    schema = {
        "name": "KCWI_ifu_acq_direct",
        "version": "0.1",
        "script": "KCWI_ifu_acq_direct",
        "guider_po": random.choice( ["REF","IFU"] ),
        "guider_gs_ra": random.uniform(0, 24) % 1000,
        "guider_gs_dec": random.uniform(-90, 90) % 1000,
        "guider_gs_mode": random.choice(["Automatic", "Operator", "User"])
    }
    return schema

def generate_science(nLen, maxArr, inst='KCWI'):
    if inst=='KCWI':
        schema = generate_kcwi_science(nLen, maxArr)
    else:
        schema = generate_kcwi_science(nLen, maxArr) # fill this in later
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
        'pa': randInt(),
        'pm_ra': randFloat(), 
        'pm_dec': randFloat(), 
        'epoch': randFloat(), 
        'obstime': randFloat(), 
        'mag': generate_mags(), 
        'wrap': optionalRandString(), 
        'd_ra': randFloat(), 
        'd_dec': randFloat(), 
        'comment': optionalRandComment()
    }
    return schema

@remove_none_values_in_dict
def generate_observation_block(nLen, maxArr, _id=None, inst='KCWI'):
    schema = {
        'signature': generate_signature(maxArr),
        'version': "0.1",
        'target': random.choice( [ None, generate_target() ] ),
        'acquisition': random.choice( [ None, generate_acquisition( nLen, maxArr, inst ) ] ),
        'science': random.choice( [None, generate_science( nLen, maxArr, inst ) ] ),
        'associations': randArrStr( nLen, maxArr ),
        'priority': randFloat(100),
        'status': randStatus(),
        'comment': optionalRandComment()
    }

    schema['_id'] = _id if _id else None
    return schema

if __name__=='__main__':
    seed = 1984739
    random.seed(seed)
    dbName = 'papahana'
    
    # Create ob_block collection
    collName = 'ob_block'
    remote=True # run on remote server (n)
    coll = create_collection(dbName, collName, port=27017, remote=False)
    coll.drop()
    coll.create_index([('signature.pi', pymongo.DESCENDING)])
    coll.create_index([('signature.semester', pymongo.DESCENDING)])
    coll.create_index([('signature.program', pymongo.DESCENDING)])
    nLen = 5
    maxArr = 5
    nOb = 100
    for idx in range(nOb):
        doc = generate_observation_block(nLen, maxArr, str(idx))
        result = coll.insert_one(doc)
        assert result.inserted_id == str(idx), 'check that idx was sed properly'
    # Create groups collection
    collName = 'groups'
    remote=True # run on remote server (n)
    coll = create_collection(dbName, collName, port=27017, remote=False)
    coll.drop()
    nGroups = 20
    for idx in range(nGroups):
        doc = generate_group(str(idx))
        result = coll.insert_one(doc)
        assert result.inserted_id == str(idx), 'check that idx was sed properly'
