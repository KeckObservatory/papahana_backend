from flask import current_app, g, Flask
from flask_cors import CORS, cross_origin
import connexion
import yaml

from papahana import util
from papahana.controllers import authorization_controller as auth_utils


def create_app():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('papahana.yaml')
    CORS(app.app, supports_credentials=True,
         resources={r"*": {"origins": ["https://www3build.keck.hawaii.edu",
                                       "https://www3.keck.hawaii.edu"],
                           "allow_headers": "*", "expose_headers": "*"}})

    mode = util.read_mode()
    urls = util.read_urls()
    config_params = util.read_config(mode)

    with app.app.app_context():
        current_app.config_params = config_params
        current_app.urls = urls
        current_app.mode = mode
        current_app.config

    return app


def main():
    app = create_app()
    
    # @app.app.after_request
    # def update_cookie(response):
    #     try:
    #         response.set_cookie('ODB-API-KEY', max_age=86400)
    #     except:
    #         pass

    app.run(port=50002)




if __name__ == '__main__':
    main()
