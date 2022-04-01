from flask import current_app, g, Flask
from flask_cors import CORS, cross_origin
import connexion
import yaml

from papahana import util
from papahana.controllers import authorization_controller as auth_utils


def create_app():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('papahana.yaml')
    # _ = CORS(app.app, allow_credentials=True)

    CORS(app.app, supports_credentials=True,
         resources={r"*": {"origins": ["https://www3build.keck.hawaii.edu", "https://www3.keck.hawaii.edu"],
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
    # def allow_cors_reponse(response):
    #     print('coring')
    #     # response.headers.set("Content-Type", "application/json")
    #     response.headers.set('Access-Control-Allow-Credentials', 'true')
    #     # response.headers.set('Access-Control-Allow-Origin', 'https://www3build.keck.hawaii.edu')
    #     # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    #     # response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
    #     # response.headers.set('Access-Control-Allow-Methods', 'GET, POST', 'PUT', 'DELETE')
    #     return response

    app.run(port=50002)




if __name__ == '__main__':
    main()
