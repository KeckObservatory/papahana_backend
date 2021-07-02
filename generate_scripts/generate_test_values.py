import pymongo

from papahana_flask_server_demo.config import config_collection
import generate_utils as utils


def generate_ob():
    coll = config_collection('obCollect', conf=config)
    ob = list(coll.find({}, sort=[('_id', pymongo.DESCENDING )]))
    print(ob[0])


if __name__=='__main__':
    args = utils.parse_args()
    mode = args.mode
    config = utils.read_config(mode)

    generate_ob()
