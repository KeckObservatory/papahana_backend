import logging

import connexion
from flask_testing import TestCase
from flask import current_app, Response

from papahana.encoder import JSONEncoder
from papahana import util


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')

        mode = util.read_mode()
        urls = util.read_urls()
        config_params = util.read_config(mode)

        with app.app.app_context():
            current_app.config_params = config_params
            current_app.urls = urls
            current_app.mode = mode

        return app.app

