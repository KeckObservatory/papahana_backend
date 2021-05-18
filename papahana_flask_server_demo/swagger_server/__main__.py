#!/usr/bin/env python3
from flask_cors import CORS
from flask import current_app
import connexion
from swagger_server import encoder
import yaml

def read_mode(config='../config.live.yaml'):
    with open(config) as file:
        mode_dict = yaml.load(file, Loader=yaml.FullLoader)['mode']

    mode = mode_dict['config']

    return mode


def read_config(mode, config='../config.live.yaml'):
    with open(config) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)[mode]

    return config


def create_app():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml')
    mode = read_mode()
    config_params = read_config(mode)
    with app.app.app_context():
        current_app.config_params = config_params
        current_app.mode = mode

    return app

def main():
    app = create_app()
    CORS(app.app)
    app.run(port=50000)


if __name__ == '__main__':
    main()
