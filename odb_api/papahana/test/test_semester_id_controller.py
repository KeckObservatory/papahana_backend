# coding: utf-8

from __future__ import absolute_import
import warnings
import ast

from papahana.test import BaseTestCase
from papahana.test.test_default_values import ObsBlocksTestDefaults

from papahana.models.container import Container 
from papahana.models.instrument_enum import InstrumentEnum 
from papahana.models.observation_block import ObservationBlock 
from papahana.models.ra_schema import RASchema 
from papahana.models.sem_id_schema import SemIdSchema 
from papahana.models.target import Target 
from papahana.test import BaseTestCase


class TestSemesterIdController(BaseTestCase):
    """SemesterIdController integration test stubs"""
    def setUp(self):
        """
        Insert a new OB to work with
        """
        self.set_api_cookie()
    #
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


    # ------
    # TESTS
    # ------
    def test_sem_id_ob_metadata(self):
        """Test case for sem_id_ob_metadata
        """
        sem_id = self.get_sem_id()
        assert(sem_id)

        min_ra = '00:00:00.0'
        max_ra = '24:00:00.0'


        # query_string = [('min_ra', min_ra), ('max_ra', max_ra),
        #                 ('instrument', 'KCWI'), ('ob_priority', 8),
        #                 ('min_priority', 1), ('max_priority', 100),
        #                 ('min_duration', 1.2), ('max_duration', 1.2),
        #                 ('observable', True),
        #                 ('completed', False),
        #                 ('container_id', 'container_id_example')]

        # test ra range
        query_string = [('min_ra', min_ra), ('max_ra', max_ra)]

        response = self.client.open(
            f'/semesterIds/{sem_id}/ob/metadata', method='GET',
            query_string=query_string)

        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # test container id
        container_id = self.get_container_id(sem_id)
        query_string = [('container_id', container_id)]

        response = self.client.open(
            f'/semesterIds/{sem_id}/ob/metadata', method='GET',
            query_string=query_string)

        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    def test_sem_id_containers_get(self):
        """Test case for sem_id_containers_get
        /semesterIds/{sem_id}/containers

        Retrieves all containers associated with a program.
        """
        sem_id = self.get_sem_id()
        assert(sem_id)

        response = self.client.open(
            f'/semesterIds/{sem_id}/containers', method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sem_id_get(self):
        """Test case for sem_id_get

        retrieves all the sem_ids associated with an observer.
        """
        response = self.client.open(
            '/semesterIds',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    # -------
    # Helpers
    # -------

    def make_default_response(self, route):
        response = self.client.open(route, method='GET')
        info = response.data.decode('utf-8')
        info = ast.literal_eval(info)

        return info

    def get_sem_id(self):
        sem_ids = self.make_default_response('/semesterIds')

        if not sem_ids:
            return None

        sem_id = sem_ids['associations'][0]

        return sem_id

    def get_container_id(self, sem_id):
        container_ids = self.make_default_response(
            f'/semesterIds/{sem_id}/containers')

        print(f'ont {container_ids}')
        if not container_ids:
            return None

        return container_ids[0]['_id']

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

