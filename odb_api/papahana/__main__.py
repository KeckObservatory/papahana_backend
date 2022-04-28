from flask import current_app
from flask_cors import CORS, cross_origin
import connexion

from papahana import util


def create_app():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('papahana.yaml')
    CORS(app.app, supports_credentials=True,
         resources={r"*": {"origins": ["https://www3build.keck.hawaii.edu",
                                       "https://www3.keck.hawaii.edu"],
                           "allow_headers": "*", "expose_headers": "*"}})

    mode = util.read_mode()
    print(f"using mode: {mode}")
    urls = util.read_urls()
    config_params = util.read_config(mode)

    api_port = config_params['api_port']

    with app.app.app_context():
        current_app.config_params = config_params
        current_app.urls = urls
        current_app.mode = mode
        current_app.config

    return app, api_port


def main():
    app, api_port = create_app()
    app.run(port=api_port)


if __name__ == '__main__':
    main()
