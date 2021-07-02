# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from papahana.test import BaseTestCase
from papahana.test.test_default_values import ContainerTestDefaults
from papahana.test.test_default_values import ObsBlocksTestDefaults


class TestContainersController(BaseTestCase):
    """ContainersController integration test stubs"""

    def setUp(self):
        """
        Insert a new OB to work with
        """
        self.container_id = self.insert_container(self.container)

    def tearDown(self):
        """
        Remove the OB that was inserted at start of test
        """
        self.delete_container(self.container_id)

    @classmethod
    def setUpClass(cls):
        cls.defaults = ContainerTestDefaults('test')
        cls.ob_defaults = ObsBlocksTestDefaults('test')
        cls.container = cls.defaults.get_example_container(0)
        cls.container_new = cls.defaults.get_example_container(-1)

    # -------------------- HELPERS --------------------
    def insert_container(self, container_body):

        response = self.client.open(
            '/v0/containers',
            method='POST',
            data=json.dumps(container_body),
            content_type='application/json')

        self.assert200(response,
                       'Failed setUp -- did not insert container.')

        container_id = response.data.decode('utf-8').replace("\n", "").replace('"', '')

        return container_id

    def delete_container(self, container_id):
        query_string = [('container_id', container_id)]
        response = self.client.open(
            '/v0/containers',
            method='DELETE',
            query_string=query_string)

        self.assert_status(response, 204,
                           'Failed tearDown -- did not remove inserted container.')

    def ob_id_list(self):
        ob_list = []
        for i in range(0, 3):
            ob_list.append(self.insert_ob(self.ob_defaults.get_example_ob()))

        return ob_list

    # -------------------- TESTS --------------------
    def test_containers_append_put(self):
        """Test case for containers_append_put

        Test appending a list of observation block IDs to a container.
        """
        new_id_list = ['60de13afe025482cc63707ba', '60de13afe025482cc63707be',
                       '60de13afe025482cc63707bf']
        query_string = [('container_id', self.container_id)]
        response = self.client.open(
            '/v0/containers/append',
            method='PUT',
            data=json.dumps(new_id_list),
            content_type='application/json',
            query_string=query_string)

        self.assert_status(response, 204,
                           'Response body is : ' + response.data.decode('utf-8'))

        # confirm the new list is in the container
        response = self.client.open(
            '/v0/containers',
            method='GET',
            query_string=query_string)

        result_dict = json.loads(response.data.decode('utf-8'))
        for id in new_id_list:
            assert(id in result_dict['observation_blocks'])

    def test_containers_delete(self):
        """Test case for containers_delete

        Delete container by id
        """
        query_string = [('container_id', self.container_id)]
        response = self.client.open(
            '/v0/containers',
            method='DELETE',
            query_string=query_string)
        self.assert_status(response, 204,
                       'Response body is : ' + response.data.decode('utf-8'))

        # confirm the container no longer is in the db
        response = self.client.open(
            '/v0/containers',
            method='GET',
            query_string=query_string)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_containers_execution_times_get(self):
        """Test case for containers_execution_times_get

        Test the calculation of the total execution time of a container.
        """
        query_string = [('container_id', self.container_id)]
        response = self.client.open(
            '/v0/containers/executionTimes',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        #TODO add a check on the actual execution time.


    # def test_containers_export_get(self):
    #     """Test case for containers_export_get
    #
    #
    #     """
    #     query_string = [('container_id', self.container_id)]
    #     response = self.client.open(
    #         '/v0/containers/export',
    #         method='GET',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))

    def test_containers_get(self):
        """Test case for containers_get

        Retrieve the container
        """
        query_string = [('container_id', self.container_id)]
        response = self.client.open(
            '/v0/containers',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # check that the response is the same as the inserted container
        result_dict = json.loads(response.data.decode('utf-8'))
        del result_dict['_id']
        assert(result_dict == self.container)

    def test_containers_items_get(self):
        """Test case for containers_items_get

        Retrieves the ordered list of observing blocks in a container.
        """
        # replace ob ids in the container's list,  insert the container
        ob_list = self.ob_id_list()
        self.container['observation_blocks'] = ob_list
        container_id = self.insert_container(self.container)

        query_string = [('container_id', container_id)]
        response = self.client.open(
            '/v0/containers/items',
            method='GET',
            query_string=query_string)

        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        result = json.loads(response.data.decode('utf-8'))

        # confirm the IDs of the returned OBs match the inserted IDs.
        for i in range(0, len(result)):
            ob = result[i]
            assert(ob['_id'] == ob_list[i])

    def test_containers_items_summary_get(self):
        """Test case for containers_items_summary_get

        Retrieves a summary of container information
        """
        query_string = [('container_id', self.container_id)]
        response = self.client.open(
            '/v0/containers/items/summary',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # check that the response is the same as the inserted container
        result_dict = json.loads(response.data.decode('utf-8'))
        del result_dict['_id']
        assert(result_dict == self.container)

    def test_containers_post(self):
        """Test case for containers_post

        Inserts a new container
        """
        body = self.container
        response = self.client.open(
            '/v0/containers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # confirm that the new container exists in the db
        new_container_id = json.loads(response.data.decode('utf-8'))
        query_string = [('container_id', new_container_id)]
        response = self.client.open(
            '/v0/containers',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_containers_put(self):
        """Test case for containers_put

        Overwrites a container
        """
        body = self.container_new
        query_string = [('container_id', self.container_id)]
        response = self.client.open(
            '/v0/containers',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert_status(response, 204,
                           'Response body is : ' + response.data.decode('utf-8'))

        # confirm the new container is there
        response = self.client.open(
            '/v0/containers',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        result_dict = json.loads(response.data.decode('utf-8'))
        del result_dict['_id']
        assert(result_dict == self.container_new)

    # def test_containers_schedule_too_post(self):
    #     """Test case for containers_schedule_too_post
    #
    #
    #     """
    #     body = [Container()]
    #     response = self.client.open(
    #         '/v0/containers/scheduleToO',
    #         method='POST',
    #         data=json.dumps(body),
    #         content_type='application/json')
    #     self.assert_status(response, 204,
    #                    'Response body is : ' + response.data.decode('utf-8'))

    # def test_containers_verify_get(self):
    #     """Test case for containers_verify_get
    #
    #
    #     """
    #     query_string = [('container_id', self.container_id)]
    #     response = self.client.open(
    #         '/v0/containers/verify',
    #         method='GET',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
