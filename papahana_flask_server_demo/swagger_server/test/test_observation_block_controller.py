# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.observation_block import ObservationBlock  # noqa: E501
from swagger_server.test import BaseTestCase


class TestObservationBlockController(BaseTestCase):
    """ObservationBlockController integration test stubs"""

    def test_obs_block_delete(self):
        """Test case for obs_block_delete

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obs_block_duplicate(self):
        """Test case for obs_block_duplicate

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/duplicate/{sem_id}'.format(sem_id='sem_id_example'),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obs_block_get(self):
        """Test case for obs_block_get

        
        """
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obs_block_post(self):
        """Test case for obs_block_post

        
        """
        body = ObservationBlock()
        response = self.client.open(
            '/v0/obsBlocks/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obs_block_put(self):
        """Test case for obs_block_put

        
        """
        body = ObservationBlock()
        query_string = [('ob_id', 'ob_id_example')]
        response = self.client.open(
            '/v0/obsBlocks/',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
