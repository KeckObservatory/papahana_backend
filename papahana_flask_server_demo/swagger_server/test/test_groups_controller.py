# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.group import Group  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGroupsController(BaseTestCase):
    """GroupsController integration test stubs"""

    def test_groups_delete(self):
        """Test case for groups_delete

        
        """
        query_string = [('group_id', 'group_id_example')]
        response = self.client.open(
            '/v0/groups',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_get(self):
        """Test case for groups_get

        
        """
        query_string = [('group_id', 'group_id_example')]
        response = self.client.open(
            '/v0/groups',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_post(self):
        """Test case for groups_post

        
        """
        body = Group()
        response = self.client.open(
            '/v0/groups',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_put(self):
        """Test case for groups_put

        
        """
        body = Group()
        query_string = [('group_id', 'group_id_example')]
        response = self.client.open(
            '/v0/groups',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
