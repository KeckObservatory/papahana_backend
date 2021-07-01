# coding: utf-8

from __future__ import absolute_import
from flask import json
from papahana.test import BaseTestCase


class TestObservationBlockController(BaseTestCase):
    """ObservationBlockController integration test stubs"""

    def setUp(self):
        """
        Insert a new OB to work with
        """
        self.ob_id = self.insert_ob()

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
        cls.template_id = 'sci0'
        cls.date_schema_1 = "2021-04-22 13:22:36"
        cls.date_schema_2 = "2021-12-07 07:07:24"
        cls.file_parameter = "json"

        cls.ob = {"metadata":
                      {"name": "standard stars #9",
                       "version": 0.1,
                       "priority": 70.8112646283874,
                       "ob_type": "science",
                       "pi_id": 7766,
                       "sem_id": "2019A_U124",
                       "instrument": "KCWI"},
                  "acquisition": {
                      "metadata": {
                          "name": "KCWI_ifu_acq_direct",
                          "ui_name": "KCWI direct",
                          "instrument": "KCWI",
                          "type": "acquisition",
                          "version": 0.1,
                          "script": "KCWI_ifu_acq_direct"},
                      "parameters": {
                          "wrap": "auto",
                           "rotmode": "PA",
                           "guider_po": "IFU",
                           "guider_gs_ra": "12:44:55.6",
                           "guider_gs_dec": "55:22:19.9",
                           "guider_gs_mode": "auto"},
                      "template_id": "acq0"
                  },
                  "science": [
                      {"metadata": {
                          "name": "KCWI_ifu_sci_dither",
                          "ui_name": "KCWI dither",
                          "instrument": "KCWI",
                          "type": "science",
                          "version": 0.1,
                          "script": "KCWI_ifu_sci_stare"
                      },
                       "parameters": {
                           "det1_exptime": 60,
                           "det1_nexp": 2,
                           "det2_exptime": 121,
                           "det2_nexp": 4,
                           "seq_ndither": 4,
                           "seq_ditarray": [{"ra_offset": 0.0, "dec_offset": 0.0, "position": "T", "guided": True}, {"ra_offset": 5.0, "dec_offset": 5.0, "position": "T", "guided": True}, {"ra_offset": 5.0, "dec_offset": 5.0, "position": "T", "guided": True}, {"ra_offset": 0.0, "dec_offset": 0.0, "position": "T", "guided": True}]},
                       "template_id": "sci0"
                       },
                      {"metadata": {
                          "name": "KCWI_ifu_sci_dither",
                          "ui_name": "KCWI dither",
                          "instrument": "KCWI",
                          "type": "science",
                          "version": 0.1,
                          "script": "KCWI_ifu_sci_stare"},
                       "parameters": {
                           "det1_exptime": 60,
                           "det1_nexp": 2,
                           "det2_exptime": 121,
                           "det2_nexp": 4,
                           "seq_ndither": 4,
                           "seq_ditarray": [
                               {"ra_offset": 0.0, "dec_offset": 0.0, "position": "T", "guided": True},
                               {"ra_offset": 5.0, "dec_offset": 5.0, "position": "T", "guided": True},
                               {"ra_offset": 5.0, "dec_offset": 5.0, "position": "T", "guided": True},
                               {"ra_offset": 0.0, "dec_offset": 0.0, "position": "T", "guided": True}
                           ]},
                       "template_id": "sci1"}
                  ],
                  "associations": ["TBD"],
                  "status": {
                      "state": "Started",
                      "executions": ["2018-04-13 16:38:13", "2020-03-22 07:05:13"],
                      "deleted": False
                  },
                  "time_constraints": ["2021-05-01 08:00:00", "2021-06-01 10:00:00"],
                  "comment": "This is a Test!  Only a Test!"
                  }

        cls.filled_template = {
            "metadata": {
                "name": "KCWI_ifu_sci_stare",
                "ui_name": "KCWI stare",
                "instrument": "KCWI",
                "template_type": "science",
                "version": 0.1,
                "script": "KCWI_ifu_sci_stare"},
            "parameters": {
                "det1_exptime": 30.2,
                "det1_nexp": 4,
                "det2_exptime": 40.1,
                "det2_nexp": 5
            }
        }

        cls.unfilled_template = {
            "metadata": {
                "name": "KCWI_ifu_sci_stare",
                "ui_name": "KCWI stare",
                "instrument": "KCWI",
                "template_type": "science",
                "version": 0.1,
                "script": "KCWI_ifu_sci_stare"},
            "parameters": {
                "det1_exptime": {
                    "ui_name": "Blue exposure time",
                    "option": "range",
                    "allowed": [0, 3600],
                    "default": None,
                    "optionality": "required",
                    "type": "float"
                },
                "det1_nexp": {
                    "ui_name": "Blue number of exposures",
                    "option": "range",
                    "allowed": [0, 3600],
                    "default": None,
                    "optionality": "required",
                    "type": "integer"
                },
                "det2_exptime": {
                    "ui_name": "Red exposure time",
                    "option": "range",
                    "allowed": [0, 3600],
                    "default": None,
                    "optionality": "optional",
                    "type": "float"
                },
                "det2_nexp": {
                    "ui_name": "Blue number of exposures",
                    "option": "range",
                "allowed": [0, 3600],
                "default": None,
                "optionality": "optional",
                "type": "integer"
                }
            }
        }
        
    # Helpers
    def insert_ob(self):
        body = self.ob
        response = self.client.open(
            '/v0/obsBlocks',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')

        ob_id = response.data.decode('utf-8').replace("\n", "").replace('"', '')

        return ob_id

    def delete_ob(self, ob_id):
        query_string = [('ob_id', ob_id)]
        response = self.client.open(
            '/v0/obsBlocks',
            method='DELETE',
            query_string=query_string)

    def delete_ob_by_reponse(self, response):
        ob_id = response.data.decode('utf-8').replace("\n", "").replace('"', '')

        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks',
            method='DELETE',
            query_string=query_string)

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

        self.delete_ob_by_reponse(response)

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

        self.delete_ob_by_reponse(response)

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

    def test_ob_export(self):
        """Test case for ob_export

        insert,  get,  and delete and OB.
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks/export',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_get(self):
        """Test case for ob_get

        Insert,  retrieve,  delete for cleanup
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_put(self):
        """Test case for ob_put

        insert an OB,  update it with the new one, delete ob
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks',
            method='PUT',
            data=json.dumps(self.ob),
            content_type='application/json',
            query_string=query_string)
        self.assert_status(response, 204,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ob_template_duplicate(self):
        """ Test case for ob_template_duplicate

        insert ob,  duplicate template in ob,  delete ob
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            f'/v0/obsBlocks/template/duplicate/{self.template_id}',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))



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



    def test_ob_template_get(self):
        """Test case for ob_template_get
        insert OB,  get template, delete
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks/template',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))



    def test_ob_template_id_delete(self):
        """Test case for ob_template_id_delete

        insert ob,  remove specific template,  delete ob
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            f'/v0/obsBlocks/template/{self.template_id}',
            method='DELETE',
            query_string=query_string)

        self.assert_status(response, 204,
                           'Response body is : ' + response.data.decode('utf-8'))



    def test_ob_template_id_get(self):
        """Test case for ob_template_id_get

        insert ob,  get specific template,  delete ob
        """
        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            f'/v0/obsBlocks/template/{self.template_id}',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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

    def test_ob_template_post(self):
        """Test case for ob_template_post

        create ob,  insert template list,  delete ob
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

    def test_ob_template_id_file_put(self):
        """Test case for ob_template_id_file_put


        """
        filename = 'test_template_file.json'
        body = open(filename)
        # file = (BytesIO(b'my file contents'), "file_name.jpg")
        query_string = [('ob_id', self.ob_id)]

        response = self.client.open(
            f'/v0/obsBlocks/template/{self.template_id}/{self.file_parameter}',
            method='PUT',
            data=json.dumps(body),
            content_type='text/plain',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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

    def test_ob_time_constraint_put(self):
        """Test case for ob_time_constraint_put

        create ob,  replace the time constraints, delete ob
        """
        body = [self.date_schema_1, self.date_schema_2]

        query_string = [('ob_id', self.ob_id)]
        response = self.client.open(
            '/v0/obsBlocks/timeConstraints',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert_status(response, 204,
                           'Response body is : ' + response.data.decode('utf-8'))

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
