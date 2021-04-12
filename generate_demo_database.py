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

observers = ['Butawhiteboy Cantbekhan',
             'Snorkeldink Crackerdong',
             'Blubberwhale Crimpysnitch', 
             'Oscarbait Rivendell',
             'Buckingham Countryside',
             'Beezlebub Vegemite',
             'Wimbledon Crackerjack',
            ]

pis = [
    'Darmond steelbreaker',
    'Thorgarn strongmane',
    'Melkyl kindpast',
    'Brannyl firststone',
    'Thergrun marblebottom',
    'Tornur fobrekahk',
    'Emnir throroguhr',
    'Balmun dekork',
    'Guldram brufdinack',
    'Gulkum rurdurarr',
]

semesters = [str(x)+y for x, y in product(range(2000,2004), ['A', 'B'])]
letters = string.ascii_lowercase

# random generators 
randString = lambda x=4: ''.join(random.choice(letters) for i in range(x))
randFloat = lambda mag=10: mag * random.uniform(0,1)
randBool = lambda: bool(random.choice([0,1, None]))
randArrStr = lambda x=1, y=1: [randString(x) for _ in range(random.randint(1, y)) ]
optionalRandString = lambda x=4: random.choice([None, randString(x)])
optionalRandArrString = lambda x, y=1: random.choice([None, randArrStr(x, y)])
sampleInst = lambda: random.choice(list(INST_MAPPING.keys()))
randPI = lambda: random.choice(pis)
randObserver = lambda: random.choice(observers)
randSemester = lambda: random.choice(semesters)
randPIList = lambda x=1: lambda x=1: list(np.random.choice(pis, size=random.randint(1, x), replace=False))
randObserverList = lambda x=1: list(np.random.choice(observers, size=random.randint(1, x), replace=False))

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
            'obs_id': randObserverList(maxLen)}

def generate_semesters(nSem, nLen=5, maxLen=6):
    return [ generate_semester(sem, nLen, maxLen) for sem in semesters[0:nSem] ]

def generate_mag(nLen=2):
    return {'band': randString(nLen), 'mag': randFloat(nLen)}

@remove_none_values_in_dict
def generate_observation(nLen, maxArr):
    schema = {
        'instrument': sampleInst(),
        'exposure_sequences': randArrStr(nLen, maxArr),
        'associations': randArrStr(nLen, maxArr),
    }
    return schema

@remove_none_values_in_dict
def generate_signature(maxArr):
    schema = {
        'pi': randPI(),
        'semester': randSemester(),
        'program': random.randint(0, 10),
        'observers': randObserverList(maxArr),
        'container': random.randint(0,3) 
    }
    return schema

@remove_none_values_in_dict
def generate_acquisition(nLen, maxArr):
    schema = {
        'instrument_setup': randString(),
        'acquisition_method': randString(),
        'guider_selection': optionalRandString(),
        'ao_modes': optionalRandArrString(nLen, maxArr),
        'offset_stars': optionalRandArrString(nLen, maxArr),
        'slitmasks': optionalRandArrString(nLen, maxArr),
        'position_angles': optionalRandArrString(nLen, maxArr),
    }
    return schema

@remove_none_values_in_dict
def generate_target():
    schema = { 
        'name': randString(), 
        'ra': randString(), 
        'dec': randString(), 
        'equinox': randFloat(), 
        'frame': randString(), 
        'ra_offset': randFloat(), 
        'dec_offset': randFloat(), 
        'pm_ra': randFloat(), 
        'pm_dec': randFloat(), 
        'epoch': randFloat(), 
        'obstime': randFloat(), 
        'mag': generate_mag(), 
        'wrap': optionalRandString(), 
        'd_ra': randFloat(), 
        'd_dec': randFloat(), 
        'comment': optionalRandString(), 
             }
    return schema

@remove_none_values_in_dict
def generate_observation_block(nLen, maxArr, _id=None):
    schema = {
        'signature': generate_signature(maxArr),
        'target': random.choice( [ None, generate_target() ]) ,
        'acquisition': random.choice( [ None, generate_acquisition(nLen, maxArr) ] ) ,
        'observations': [ generate_observation(nLen, maxArr) for _ in range(random.randint(1, maxArr)) ], 
        'associations': randArrStr(nLen, maxArr),
        'priority': randFloat(100)
    }
    if _id:
        schema['_id'] = _id
    return schema

if __name__=='__main__':
    seed = 1984739
    random.seed(seed)
    dbName = 'papahana'
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