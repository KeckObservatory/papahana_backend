import yaml
import argparse

from papahana import util as papahana_util

import generate_random_utils as random_utils
from bson.objectid import ObjectId


def parse_args():
    """
    Parse the command line arguments.

    :return: <obj> commandline arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--mode", "-m", type=str,
                        default=None, required=True,
                        help="The configuration to read")

    parser.add_argument("--generate_observers", "-o", type=bool,
                        default=False,
                        help="The configuration to read")

    return parser.parse_args()


def read_config(mode, config):
    with open(config) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)[mode]

    return config


def make_status_realistic(ob, config):
    coll = papahana_util.config_collection('obCollect', conf=config)
    fields = {'observations.metadata.sequence_number': 1}

    ob_info = list(coll.find({"_id": ObjectId(ob)}, fields))

    for ob_seq in ob_info:
        oid = ob_seq['_id']
        seq_n = 0
        for seq in ob_seq['observations']:
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


def parse_templates_version(template_list):
    schema = {}
    for template in template_list:
        version = template["metadata"]["version"]
        schema[template["metadata"]["name"]] = version

    return schema


def non_inst_templates(inst_list, template_list):
    return list(filter(lambda template: [inst for inst in inst_list if inst[0].lower() not in template['metadata']['name']], template_list))


def inst_template_list(inst, template_list):
    return list(filter(lambda template: inst.lower() in template['metadata']['name'], template_list))


def parse_template_list(inst, inst_list, template_list):
    return non_inst_templates(inst_list, template_list) + inst_template_list(inst, template_list)

