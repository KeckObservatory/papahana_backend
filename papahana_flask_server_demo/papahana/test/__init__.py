import logging
import json

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
        app.add_api('papahana.yaml')

        mode = 'test'
        urls = util.read_urls()
        config_params = util.read_config(mode)

        with app.app.app_context():
            current_app.config_params = config_params
            current_app.urls = urls
            current_app.mode = mode

        return app.app

    def insert_ob(self, ob_body):
        response = self.client.open(
            '/v0/obsBlocks',
            method='POST',
            data=json.dumps(ob_body),
            content_type='application/json')

        self.assert200(response,
                       'Failed __init__ insert_ob -- did not insert OB.')

        ob_id = response.data.decode('utf-8').replace("\n", "").replace('"', '')

        return ob_id

    def delete_ob(self, ob_id):
        query_string = [('ob_id', ob_id)]
        response = self.client.open(
            '/v0/obsBlocks',
            method='DELETE',
            query_string=query_string)

        self.assert_status(response, 204,
                           'Failed __init__ delete_ob,  did not delete OB')



