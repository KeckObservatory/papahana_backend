# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from papahana.models.container import Container  # noqa: E501
from papahana.models.observation_block import ObservationBlock  # noqa: E501
from papahana.models.sem_id_schema import SemIdSchema  # noqa: E501
from papahana.test import BaseTestCase


class TestContainersController(BaseTestCase):
    """ContainersController integration test stubs"""

    def test_containers_append_put(self):
        """Test case for containers_append_put

        
        """
        body = ['body_example']
        query_string = [('container_id', 'container_id_example')]
        response = self.client.open(
            '/v0/containers/append',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_containers_delete(self):
        """Test case for containers_delete

        
        """
        query_string = [('container_id', 'container_id_example')]
        response = self.client.open(
            '/v0/containers',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_containers_execution_times_get(self):
        """Test case for containers_execution_times_get

        
        """
        query_string = [('container_id', 'container_id_example')]
        response = self.client.open(
            '/v0/containers/executionTimes',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_containers_export_get(self):
        """Test case for containers_export_get

        
        """
        query_string = [('container_id', 'container_id_example')]
        response = self.client.open(
            '/v0/containers/export',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_containers_get(self):
        """Test case for containers_get

        
        """
        query_string = [('container_id', 'container_id_example')]
        response = self.client.open(
            '/v0/containers',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_containers_items_get(self):
        """Test case for containers_items_get

        
        """
        query_string = [('container_id', 'container_id_example')]
        response = self.client.open(
            '/v0/containers/items',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_containers_items_summary_get(self):
        """Test case for containers_items_summary_get

        
        """
        query_string = [('container_id', 'container_id_example')]
        response = self.client.open(
            '/v0/containers/items/summary',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_containers_post(self):
        """Test case for containers_post

        
        """
        body = Container()
        response = self.client.open(
            '/v0/containers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_containers_put(self):
        """Test case for containers_put

        
        """
        body = Container()
        query_string = [('container_id', 'container_id_example')]
        response = self.client.open(
            '/v0/containers',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_containers_schedule_too_post(self):
        """Test case for containers_schedule_too_post

        
        """
        body = [Container()]
        response = self.client.open(
            '/v0/containers/scheduleToO',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_containers_verify_get(self):
        """Test case for containers_verify_get

        
        """
        query_string = [('container_id', 'container_id_example')]
        response = self.client.open(
            '/v0/containers/verify',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sem_id_containers_get(self):
        """Test case for sem_id_containers_get

        
        """
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/{sem_id}/containers'.format(sem_id=SemIdSchema()),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
