import generate_utils as utils
import generate_random_utils as random_utils
import generate_targets as target_utils
from papahana import util as papahana_util
import importlib

from bson.objectid import ObjectId
import random
import datetime

MAX_ARRAY_LEN = 5
NLEN = 5


def generate_obs(config, inst, inst_list, template_list):
    inst = inst.upper()

    try:
        instModule = importlib.import_module(f'{inst.lower()}_items')
    except ModuleNotFoundError as err:
        print(f'{err} for {inst}')

    coll = papahana_util.config_collection('obCollect', conf=config)

    ob_blocks = []

    template_list = utils.parse_template_list(inst, inst_list, template_list)

    for idx in range(random_utils.NOBS):
        try:
            doc = generate_observation_block(template_list, coll,
                                            instModule, inst=inst)
        except Exception as err:
            print('error', err)

        metadata = {"timestamp": datetime.datetime.now()}

        # insert into the difference collection
        result = coll.patch_one(doc, metadata=metadata)
        ob_blocks.append(str(result.inserted_id_obj.inserted_id))

    sem_id_list = []
    for ob in ob_blocks:
        utils.make_status_realistic(ob, config)
        sem_id = get_sem_id(ob, config)
        if sem_id not in sem_id_list:
            sem_id_list.append(sem_id)

    return ob_blocks


def generate_science(filledModule, template_list):
    import copy

    schema = []
    n_templates = random.randint(0, 5)
    for indx in range(0, n_templates):
        filed_sci = filledModule.filled_sci_templates(template_list)
        tmp_list = copy.deepcopy(filed_sci)
        filled_template = random.choice(tmp_list)
        filled_template['metadata']['sequence_number'] = indx+1
        schema.append(filled_template)

    return schema


def generate_acquisition(filledModule):
    schema = filledModule.filled_acq_templates()

    return schema[0]


def generate_metadata(inst):
    pi_name = random_utils.randPI()
    schema = {
        'name': 'standard stars #' + str(random.randint(0, 9)),
        'version': '0.1.0',
        'priority': random_utils.randInt(100),
        'ob_type': 'science',
        'pi_id': random_utils.pis[pi_name],
        'sem_id': random_utils.randSemId(),
        'instrument': inst,
        'tags': [],
        'comment': random_utils.optionalRandComment()
    }
    return schema


def generate_observation_block(template_list, coll, instModule, inst):
    meta = generate_metadata(inst)
    sem_id = meta['sem_id']
    n_ob = coll.count_documents({'metadata.sem_id': sem_id}) + 1

    if inst.upper() == 'KPF':
        target = target_utils.generate_kpf_target()
    else:
        target = random.choice([target_utils.generate_sidereal_target(),
                                 target_utils.generate_nonsidereal_target()])
    schema = {
        '_ob_id': f"{meta['sem_id']}_{str(n_ob).zfill(4)}",
        'metadata': meta,
        'target': target,
        'acquisition': generate_acquisition(instModule),
        'observations': generate_science(instModule, template_list),
        'associations': random_utils.randArrStr(NLEN, MAX_ARRAY_LEN),
        'status': randStatus(inst),
        'common_parameters': instModule.filled_common_parameters(),
        'comment': random_utils.optionalRandComment()
    }

    return schema

def randStatus(inst):
    executions = []
    for x in range(0, random_utils.randInt(0,6)):
        executions.append(generate_random_executions())

    schema = {'state': random_utils.randInt(0,4),
              'priority': random_utils.randInt(0,100),
              'current_seq': random_utils.randInt(0, 6),
              'current_step': random_utils.randInt(0, 4),
              'executions': executions,
              'deleted': False}

    if inst.upper() == 'KPF':
        schema['current_exp_det'] = random_utils.randInt(0, 4)
    else:
        schema['current_exp_det1'] = random_utils.randInt(0, 4)
        schema['current_exp_det2'] = random_utils.randInt(0, 4)

    return schema


def generate_random_executions():
    rdate = random_dates()
    random_time = datetime.datetime.now().replace(hour=random.randint(0, 23),
                                                  minute=random.randint(0, 59))

    random_date = f'{rdate} {random_time.strftime("%H:%M:%S")}'

    return random_date


def random_dates():
    start_date = datetime.date(2018, 1, 1)
    end_date = datetime.date(2021, 2, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date


def get_sem_id(ob, config):
    coll = papahana_util.config_collection('obCollect', conf=config)
    fields = {'metadata.sem_id': 1}

    ob_info = list(coll.find({"_id": ObjectId(ob)}, fields))
    try:
        return ob_info[0]['metadata']['sem_id']
    except:
        return None
