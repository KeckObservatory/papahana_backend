# coding: utf-8

from __future__ import absolute_import
import warnings

from papahana.test import BaseTestCase
from papahana.test.test_default_values import ObsBlocksTestDefaults


class TestSemesterIdController(BaseTestCase):
    """SemesterIdController integration test stubs"""
    def setUp(self):
        """
        Insert a new OB to work with
        """
        self.set_api_cookie()
        self.container_id = self.insert_container(self.container)

    # def tearDown(self):
    #     """
    #     Remove the OB that was inserted at start of test
    #     """
    #     self.delete_container(self.container_id)

    @classmethod
    def setUpClass(cls):
        #TODO find the socket warning!
        warnings.simplefilter("ignore")
        cls.ob_defaults = ObsBlocksTestDefaults('test')
        cls.sem_id = '2020A_U169'
        cls.obs_id = 2003
        cls.semester = '2021A'

    def test_sem_id_containers_get(self):
        """Test case for sem_id_containers_get

        Retrieves all containers associated with a program.
        """
        response = self.client.open(
            '/semesterIds/',
            method='GET')
        sem_id = response['associations'][0]

        response = self.client.open(
            f'/semesterIds/{sem_id}/containers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sem_id_get(self):
        """Test case for sem_id_get

        retrieves all the sem_ids associated with an observer.
        """
        response = self.client.open(
            '/semesterIds/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
    #
    # def test_sem_id_ob_get(self):
    #     """Test case for sem_id_ob_get
    #
    #     retrieves the ob_blocks for a sem_id.
    #     """
    #     query_string = [('obs_id', self.obs_id)]
    #     response = self.client.open(
    #         f'/semesterIds/{self.sem_id}/ob',
    #         method='GET',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))

    # def test_sem_id_proposal_get(self):
    #     """Test case for sem_id_proposal_get
    #
    #     retrieves the proposal associated with the program.
    #     """
    #     query_string = [('obs_id', self.obs_id)]
    #     response = self.client.open(
    #         f'/semesterIds/{self.sem_id}/proposal',
    #         method='GET',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))
    #
    # def test_sem_id_semester_get(self):
    #     """Test case for sem_id_semester_get
    #
    #     retrieves all the sem_id associated with an observer for the semester.
    #     """
    #     query_string = [('obs_id', self.obs_id)]
    #     response = self.client.open(
    #         f'/semesterIds/{self.semester}/semester/',
    #         method='GET',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))

    # def test_sem_id_submit_post(self):
    #     """Test case for sem_id_submit_post
    #
    #     Submits OBs for a program.  Uses the obsid in the authentication
    #     header and provided semId to retrieve the proposal file
    #     associated with the program
    #     """
    #     ob = self.ob_defaults.get_example_ob()
    #     query_string = [('obs_id', self.obs_id)]
    #     response = self.client.open(
    #         f'/semesterIds/{self.sem_id}/submit',
    #         method='POST',
    #         data=json.dumps(ob),
    #         content_type='application/json',
    #         query_string=query_string)
    #     self.assert_status(response, 204,
    #                        'Response body is : ' + response.data.decode('utf-8'))
    #
    # def test_sem_id_submit_put(self):
    #     """Test case for sem_id_submit_put
    #
    #     """
    #     ob = self.ob_defaults.get_example_ob()
    #     query_string = [('obs_id', self.obs_id)]
    #     response = self.client.open(
    #         f'/semesterIds/{self.sem_id}/submit',
    #         method='PUT',
    #         data=json.dumps(ob),
    #         content_type='application/json',
    #         query_string=query_string)
    #     self.assert_status(response, 204,
    #                        'Response body is : ' + response.data.decode('utf-8'))
    #
    # def test_sem_id_targets_get(self):
    #     """Test case for sem_id_targets_get
    #
    #     """
    #     query_string = [('obs_id', self.obs_id)]
    #     response = self.client.open(
    #         f'/semesterIds/{self.sem_id}/targets',
    #         method='GET',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    import tracemalloc

    tracemalloc.start()

    unittest.main()

    snapshot1 = tracemalloc.take_snapshot()
    snapshot2 = tracemalloc.take_snapshot()

    top_stats = snapshot2.compare_to(snapshot1, 'lineno')

    print("[ Top 10 differences ]")
    for stat in top_stats[:10]:
        print(stat)

