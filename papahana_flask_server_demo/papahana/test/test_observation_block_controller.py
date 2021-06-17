# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from papahana.models.body import Body  # noqa: E501
from papahana.models.body1 import Body1  # noqa: E501
from papahana.models.observation import Observation  # noqa: E501
from papahana.models.observation_block import ObservationBlock  # noqa: E501
from papahana.models.template_id import TemplateId  # noqa: E501
from papahana.test import BaseTestCase

from papahana import util
from config import config_collection
import pymongo


class TestObservationBlockController(BaseTestCase):
    """ObservationBlockController integration test stubs"""

    def __init__(self):
        mode = util.read_mode()
        conf = util.read_config(mode)
        coll = config_collection('obCollect', mode=mode, conf=conf)

        self.ob_id = coll.find_one()

    def test_ob_delete(self):
        """Test case for ob_delete

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_duplicate(self):
        """Test case for ob_duplicate

        
        """
        query_string = [('ob_id', 'ob_id_example'),
                        ('sem_id', '')]
        response = self.client.open(
            '/v0/obsBlocks/duplicate',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_execution_time(self):
        """Test case for ob_execution_time

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/executionTime',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_executions(self):
        """Test case for ob_executions

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/executions',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_export(self):
        """Test case for ob_export

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/export',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_get(self):
        """Test case for ob_get

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_post(self):
        """Test case for ob_post

        
        """
        body = ObservationBlock()
        response = self.client.open(
            '/v0/obsBlocks',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_put(self):
        """Test case for ob_put

        
        """
        body = ObservationBlock()
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_schedule_get(self):
        """Test case for ob_schedule_get

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/schedule',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_schedule_put(self):
        """Test case for ob_schedule_put

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/schedule',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_duplicate(self):
        """Test case for ob_template_duplicate

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/template/duplicate/{template_id}'.format(template_id=TemplateId()),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_filled(self):
        """Test case for ob_template_filled

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/completelyFilledIn',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_get(self):
        """Test case for ob_template_get

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/template',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_id_delete(self):
        """Test case for ob_template_id_delete

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/template/{template_id}'.format(template_id=TemplateId()),
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_id_file_get(self):
        """Test case for ob_template_id_file_get

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/template/{template_id}/{file_parameter}'.format(template_id=TemplateId(), file_parameter='file_parameter_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_id_file_put(self):
        """Test case for ob_template_id_file_put

        
        """
        body = Object()
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/template/{template_id}/{file_parameter}'.format(template_id=TemplateId(), file_parameter='file_parameter_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='text/plain',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_id_get(self):
        """Test case for ob_template_id_get

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/template/{template_id}'.format(template_id=TemplateId()),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_id_put(self):
        """Test case for ob_template_id_put

        
        """
        body = Observation()
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/template/{template_id}'.format(template_id=TemplateId()),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_post(self):
        """Test case for ob_template_post

        
        """
        body = Body1()
        query_string = [('ob_id', 'ob_id_example'),
                        ('template_type', 'template_type_example')]
        response = self.client.open(
            '/v0/obsBlocks/template',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_put(self):
        """Test case for ob_template_put

        
        """
        body = Body()
        query_string = [('ob_id', 'ob_id_example'),
                        ('template_type', 'template_type_example')]
        response = self.client.open(
            '/v0/obsBlocks/template',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_supplement(self):
        """Test case for ob_template_supplement

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/supplementFiles',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_time_constraint_get(self):
        """Test case for ob_time_constraint_get

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/timeConstraints',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_time_constraint_put(self):
        """Test case for ob_time_constraint_put

        
        """
        body = ['body_example']
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/timeConstraints',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_upgrade(self):
        """Test case for ob_upgrade

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/upgrade',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
