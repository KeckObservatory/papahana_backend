# coding: utf-8
from six import BytesIO

# from __future__ import absolute_import
from flask import json
from papahana.test import BaseTestCase
from papahana.test.test_default_values import ObsBlocksTestDefaults


class TestObservationBlockController(BaseTestCase):
    """ObservationBlockController integration test stubs"""

    def setUp(self):
        """
        Insert a new OB to work with
        """
        self.ob_id = self.insert_ob(self.ob)

    def tearDown(self):
        """
        Remove the OB that was inserted at start of test
        """
        self.delete_ob(self.ob_id)

    @classmethod
    def setUpClass(cls):
        """
        called once before running all test methods
        """
        cls.defaults = ObsBlocksTestDefaults('test')
        cls.template_id = 'sci0'
        cls.file_parameter = "json"
        cls.ob = cls.defaults.get_example_ob(0)
        cls.filled_template = cls.defaults.get_filled_template()

    def get_ob(self, ob_id):
        query_string = [('ob_id', ob_id)]
        response = self.client.open(
            '/v0/obsBlocks',
            method='GET',
            query_string=query_string)

        return response

    def parse_id(self, response):
        return response.data.decode('utf-8').replace("\n", "").replace('"', '')

    def check_template(self, new_template, template_id):
        orig_template = None

        id_map = {'acq': 'acquisition', 'sci': 'science',
                  'cal': 'calibration', 'eng': 'engineering'}

        orig_templates = self.ob[id_map[template_id[:3]]]
        if type(orig_templates) is not list:
            orig_templates = [orig_templates]

        for template in orig_templates:
            if template['template_id'] == template_id:
                orig_template = template
                break

        assert orig_template
        assert(new_template.keys() == orig_template.keys())
        for key in orig_template:
            assert(new_template[key] == orig_template[key])

    # TESTS
    def test_ob_post(self):
        """Test case for ob_post

        Test Inserting an ob,  then delete it to clean up.
        """
        body = self.ob
        response = self.client.open(
            '/v0/obsBlocks',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')

        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # confirm the OB exists in the db
        self.assert200(self.get_ob(self.parse_id(response)),
                       'Response body is : ' + response.data.decode('utf-8'))

        self.delete_ob(self.parse_id(response))

    def test_ob_delete(self):
        """Test case for ob_delete

        Insert an OB and then delete it.  Checks it returns status 204.
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks',
            method='DELETE',
            query_string=query_string)
        self.assert_status(response, 204,
                           'Response body is : ' + response.data.decode('utf-8'))

        # confirm the OB does not exist in the db
        self.assert404(self.get_ob(self.parse_id(response)),
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_duplicate(self):
        """Test case for ob_duplicate

        Insert an OB to get the id,  test duplicating it,  delete to clean up.
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks/duplicate',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # confirm the new OB exists in the db
        self.assert200(self.get_ob(self.parse_id(response)),
                       'Response body is : ' + response.data.decode('utf-8'))

        self.delete_ob(self.parse_id(response))

    def test_ob_execution_time(self):
        """Test case for ob_execution_time

        Insert, check execution time,  delete.
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks/executionTime',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # TODO add check for the execution times

    def test_ob_executions(self):
        """Test case for ob_executions

        ob_executions - Retrieves the list of execution attempts for
        a specific OB.

        Insert,  check,  delete
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks/executions',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # TODO add check for the execution times

    def test_ob_export(self):
        """Test case for ob_export

        get OB,  confirm it is the same as inserted
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks/export',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # confirm the retrieve OB is the same as inserted
        result_ob = json.loads(response.data.decode('utf-8'))
        del result_ob['_id']
        assert(result_ob == self.ob)

    def test_ob_get(self):
        """Test case for ob_get

        get OB,  confirm it is the same as inserted
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # confirm the retrieve OB is the same as inserted
        result_ob = json.loads(response.data.decode('utf-8'))
        del result_ob['_id']
        assert(result_ob == self.ob)

    def test_ob_put(self):
        """Test case for ob_put

        update it with the inserted OB, confirm the update
        """
        query_string = [('ob_id', self.ob_id)]
        new_ob = self.defaults.get_example_ob(1)
        response = self.client.open(
            '/v0/obsBlocks',
            method='PUT',
            data=json.dumps(new_ob),
            content_type='application/json',
            query_string=query_string)
        self.assert_status(response, 204,
                       'Response body is : ' + response.data.decode('utf-8'))

        # confirm the new OB was inserted
        response = self.get_ob(self.ob_id)
        result_ob = json.loads(response.data.decode('utf-8'))
        del result_ob['_id']
        assert(result_ob == new_ob)

    def test_ob_template_duplicate(self):
        """ Test case for ob_template_duplicate

        duplicate template in ob,  check to see the list increased by one.
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            f'/v0/obsBlocks/template/duplicate/{self.template_id}',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # confirm the number of templates increased by one
        response = self.get_ob(self.ob_id)
        result_ob = json.loads(response.data.decode('utf-8'))

        orig_ob = self.defaults.get_example_ob(0)
        assert(len(orig_ob['science'])+1 == len(result_ob['science']))

    def test_ob_template_filled(self):
        """Test case for ob_template_filled

        insert OB,  check all required parameters are filled, delete
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks/completelyFilledIn',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # TODO check broken OBs for false
        # check that parameters have been filled
        assert('true' in response.data.decode('utf-8'))

    def test_ob_templates_get(self):
        """Test case for ob_templates_get

        insert OB,  get template, delete
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks/template',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # check the templates against the originals
        template_list = json.loads(response.data.decode('utf-8'))
        for i in range(0, len(template_list)):
            template = template_list[i]
            self.check_template(template, template['template_id'])

    def test_ob_template_id_delete(self):
        """Test case for ob_template_id_delete

        remove specific template,  confirm the template list decreased by 1
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            f'/v0/obsBlocks/template/{self.template_id}',
            method='DELETE',
            query_string=query_string)

        self.assert_status(response, 204,
                           'Response body is : ' + response.data.decode('utf-8'))

        # confirm the number of templates decreased by one
        response = self.get_ob(self.ob_id)
        result_ob = json.loads(response.data.decode('utf-8'))

        orig_ob = self.defaults.get_example_ob(0)
        assert(len(orig_ob['science'])-1 == len(result_ob['science']))

    def test_ob_template_id_get(self):
        """Test case for ob_template_id_get

        get specific template, confirm it is the correct template
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            f'/v0/obsBlocks/template/{self.template_id}',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        #confirm it is the correct template
        new_template = json.loads(response.data.decode('utf-8'))
        self.check_template(new_template, self.template_id)
        # for template in self.ob['science']:
        #     if template['template_id'] == self.template_id:
        #         orig_template = template
        #         break
        #
        # template = json.loads(response.data.decode('utf-8'))
        # assert(template.keys() == orig_template.keys())
        # for key in orig_template:
        #     assert(template[key] == orig_template[key])

    def test_ob_template_id_put(self):
        """Test case for ob_template_id_put

        insert OB, updates the specified template in OB, delete OB
        """
        body = self.filled_template

        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            f'/v0/obsBlocks/template/{self.template_id}',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert_status(response, 204,
                       'Response body is : ' + response.data.decode('utf-8'))

        #TODO confirm the template matches the filled_template

    def test_ob_template_post(self):
        """Test case for ob_template_post

        insert template list
        """
        body = [self.filled_template, self.filled_template]

        query_string = [('ob_id', self.ob_id),
                        ('template_type', 'science')]
        response = self.client.open(
            '/v0/obsBlocks/template',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert_status(response, 204,
                           'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_put(self):
        """Test case for ob_template_put

        create ob,  insert template,  delete ob
        """
        body = self.filled_template
        query_string = [('ob_id', self.ob_id),
                        ('template_type', 'science')]
        response = self.client.open(
            '/v0/obsBlocks/template',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert_status(response, 204,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_id_file_get(self):
        """Test case for ob_template_id_file_get

        insert ob,  retrieve the file with template,  delete ob
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            f'/v0/obsBlocks/template/{self.template_id}/{self.file_parameter}',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    # def test_ob_template_id_file_put(self):
    #     """Test case for ob_template_id_file_put
    #
    #
    #     """
    #     filename = 'test_template_file.json'
    #     body = open(filename)
    #     # file = (BytesIO(b'my file contents'), "file_name.jpg")
    #     query_string = [('ob_id', self.ob_id)]
    #
    #     response = self.client.open(
    #         f'/v0/obsBlocks/template/{self.template_id}/{self.file_parameter}',
    #         method='PUT',
    #         data=json.dumps(body),
    #         content_type='text/plain',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_time_constraint_get(self):
        """Test case for ob_time_constraint_get

        create ob,  retrieve the time constraints, delete ob
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks/timeConstraints',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        time_constraints = json.loads(response.data.decode('utf-8'))
        assert(time_constraints == self.ob['time_constraints'])

    def test_ob_time_constraint_put(self):
        """Test case for ob_time_constraint_put

        create ob,  replace the time constraints, delete ob
        """
        new_time_constraints = self.defaults.get_example_time_constraints(-1)

        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks/timeConstraints',
            method='PUT',
            data=json.dumps(new_time_constraints),
            content_type='application/json',
            query_string=query_string)
        self.assert_status(response, 204,
                           'Response body is : ' + response.data.decode('utf-8'))

        # confirm the new constraints are in the ob
        response = self.get_ob(self.ob_id)
        result_ob = json.loads(response.data.decode('utf-8'))
        assert(result_ob['time_constraints'] == new_time_constraints)

    # def test_ob_upgrade(self):
    #     """Test case for ob_upgrade
    #
    #
    #     """
    #     query_string = [('ob_id', 'ob_id_example'),
    #                     ('sem_id', SemIdSchema())]
    #     response = self.client.open(
    #         '/v0/obsBlocks/upgrade',
    #         method='POST',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))
    #


    # def test_ob_template_supplement(self):
    #     """Test case for ob_template_supplement
    #
    #
    #     """
    #     query_string = [('ob_id', 'ob_id_example')]
    #     response = self.client.open(
    #         '/v0/obsBlocks/supplementFiles',
    #         method='GET',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))

    # def test_ob_schedule_get(self):
    #     """Test case for ob_schedule_get
    #
    #
    #     """
    #     query_string = [('ob_id', 'ob_id_example')]
    #     response = self.client.open(
    #         '/v0/obsBlocks/schedule',
    #         method='GET',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))
    #
    # def test_ob_schedule_put(self):
    #     """Test case for ob_schedule_put
    #
    #
    #     """
    #     query_string = [('ob_id', 'ob_id_example')]
    #     response = self.client.open(
    #         '/v0/obsBlocks/schedule',
    #         method='PUT',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
