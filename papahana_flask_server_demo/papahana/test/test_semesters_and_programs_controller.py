# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.container import Container  # noqa: E501
from swagger_server.models.program import Program  # noqa: E501
from swagger_server.models.target import Target  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSemestersAndProgramsController(BaseTestCase):
    """SemestersAndProgramsController integration test stubs"""

    def test_program_semester_get(self):
        """Test case for program_semester_get

        retrieves all the programs associated with an observer for the semester.
        """
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/{semester}/semester/'.format(semester='semester_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_program_semid_get(self):
        """Test case for program_semid_get

        Retrieves the specified program.
        """
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/{sem_id}/semid'.format(sem_id='sem_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_program_submit_post(self):
        """Test case for program_submit_post

        
        """
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/{sem_id}/submit'.format(sem_id='sem_id_example'),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_program_submit_put(self):
        """Test case for program_submit_put

        
        """
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/{sem_id}/submit'.format(sem_id='sem_id_example'),
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_programs_get(self):
        """Test case for programs_get

        retrieves all the programs associated with an observer.
        """
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sem_id_containers_get(self):
        """Test case for sem_id_containers_get

        
        """
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/{sem_id}/containers'.format(sem_id='sem_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sem_id_proposal_get(self):
        """Test case for sem_id_proposal_get

        
        """
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/{sem_id}/proposal'.format(sem_id='sem_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sem_id_targets_get(self):
        """Test case for sem_id_targets_get

        
        """
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/{sem_id}/targets'.format(sem_id='sem_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
