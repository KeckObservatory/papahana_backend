# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.program import Program  # noqa: E501
from swagger_server.models.target import Target  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSemestersAndProgramsController(BaseTestCase):
    """SemestersAndProgramsController integration test stubs"""

    def test_semester_programs_get(self):
        """Test case for semester_programs_get

        retrieves all the programs associated with an observer
        """
        query_string = [('obs_id', None)]
        response = self.client.open(
            '/v0/semesters/{sem_id}'.format(sem_id='sem_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_semesters_get(self):
        """Test case for semesters_get

        retrieves all the programs associated with a PI
        """
        query_string = [('obs_id', None)]
        response = self.client.open(
            '/v0/semesters',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_semesters_groups_get(self):
        """Test case for semesters_groups_get

        
        """
        query_string = [('sem_id', 'sem_id_example')]
        response = self.client.open(
            '/v0/semesters/groups/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_semesters_observing_blocks_get(self):
        """Test case for semesters_observing_blocks_get

        retrieves all the programs associated with an observer
        """
        query_string = [('obs_id', None)]
        response = self.client.open(
            '/v0/semesters/observing_blocks/{sem_id}'.format(sem_id='sem_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_semesters_proposal_get(self):
        """Test case for semesters_proposal_get

        
        """
        query_string = [('obs_id', None)]
        response = self.client.open(
            '/v0/semesters/proposal/{sem_id}'.format(sem_id='sem_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_semesters_submit_post(self):
        """Test case for semesters_submit_post

        
        """
        query_string = [('obs_id', None)]
        response = self.client.open(
            '/v0/semesters/submit/{sem_id}'.format(sem_id='sem_id_example'),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_semesters_submit_put(self):
        """Test case for semesters_submit_put

        
        """
        query_string = [('obs_id', None)]
        response = self.client.open(
            '/v0/semesters/submit/{sem_id}'.format(sem_id='sem_id_example'),
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_semesters_targets_get(self):
        """Test case for semesters_targets_get

        
        """
        query_string = [('obs_id', None)]
        response = self.client.open(
            '/v0/semesters/targets/{sem_id}'.format(sem_id='sem_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
