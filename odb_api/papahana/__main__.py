from flask import current_app, g
import connexion
import yaml

from papahana import util
from papahana.controllers import authorization_controller as auth_utils


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

    # @app.app.before_request
    # def before_request():
    #     g.user = auth_utils.is_authorized()
    #
    #     print(f'before request - user {g.user}')
    #     print(f'before request - auth {g.authorized}')

    app.run(port=50002)


if __name__ == '__main__':
    main()
