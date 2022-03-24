from flask import current_app
import connexion
import yaml

from papahana import util


def create_app():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('papahana.yaml')
    mode = util.read_mode()
    urls = util.read_urls()
    config_params = util.read_config(mode)

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
