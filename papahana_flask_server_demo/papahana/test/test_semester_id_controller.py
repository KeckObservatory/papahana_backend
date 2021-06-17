# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from papahana.models.container import Container  # noqa: E501
from papahana.models.observation_block import ObservationBlock  # noqa: E501
from papahana.models.target import Target  # noqa: E501
from papahana.test import BaseTestCase


class TestSemesterIdController(BaseTestCase):
    """SemesterIdController integration test stubs"""

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

    def test_sem_id_get(self):
        """Test case for sem_id_get

        retrieves all the sem_ids associated with an observer.
        """
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sem_id_ob_get(self):
        """Test case for sem_id_ob_get

        Retrieves the ob_blocks for a sem_id.
        """
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/{sem_id}/ob'.format(sem_id='sem_id_example'),
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

    def test_sem_id_semester_get(self):
        """Test case for sem_id_semester_get

        retrieves all the sem_id associated with an observer for the semester.
        """
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/{semester}/semester/'.format(semester='semester_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sem_id_submit_post(self):
        """Test case for sem_id_submit_post

        
        """
        body = ObservationBlock()
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/{sem_id}/submit'.format(sem_id='sem_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sem_id_submit_put(self):
        """Test case for sem_id_submit_put

        
        """
        body = ObservationBlock()
        query_string = [('obs_id', 56)]
        response = self.client.open(
            '/v0/semesterIds/{sem_id}/submit'.format(sem_id='sem_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
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
