#!/usr/bin/env python3
from flask_cors import CORS
import connexion
from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    CORS(app.app, resources={r"https://www3build.keck.hawaii.edu/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})

    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Papahana_demo'}, pythonic_params=True)
    app.run(port=50000)


if __name__ == '__main__':
    main()
