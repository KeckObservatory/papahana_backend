from flask import current_app
import connexion
import yaml


def read_mode(config='../config.live.yaml'):
    with open(config) as file:
        mode_dict = yaml.load(file, Loader=yaml.FullLoader)['mode']

    if 'config' in mode_dict:
        return mode_dict['config']

    else:
        return 'production'


def read_config(mode, config='config.live.yaml'):
    with open(config) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)[mode]

    return config


def read_urls(config='config.live.yaml'):
    with open(config) as file:
        urls = yaml.load(file, Loader=yaml.FullLoader)['urls']

    return urls


def create_app():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml')
    mode = read_mode()
    urls = read_urls()
    config_params = read_config(mode)
    with app.app.app_context():
        current_app.config_params = config_params
        current_app.urls = urls
        current_app.mode = mode

    return app


def main():
    app = create_app()
    app.run(port=50001)


if __name__ == '__main__':
    main()
