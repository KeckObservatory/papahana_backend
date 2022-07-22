import yaml
import argparse


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


def read_config(mode, config='config.live.yaml'):
    with open(config) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)[mode]

    return config