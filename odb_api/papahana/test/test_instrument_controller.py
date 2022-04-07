# coding: utf-8

from __future__ import absolute_import

import ast

from papahana.models.instrument_package import InstrumentPackage
from papahana.test import BaseTestCase


class TestInstrumentController(BaseTestCase):
    """InstrumentController integration test stubs"""
    def setUp(self):
        """
        Insert a new OB to work with
        """
        self.set_api_cookie()

    @classmethod
    def setUpClass(cls):
        """
        called once before running all test methods
        """
        cls.inst = 'KCWI'


    def test_instrument_packages(self):
        """Test case for instrument_packages

        
        """
        response = self.client.open(
            f'/instrumentPackages/{self.inst}',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        ip_dict = ast.literal_eval(response.data.decode('utf-8'))

        assert(InstrumentPackage.from_dict(ip_dict))

    def test_instrument_packages_templates(self):
        """Test case for instrument_packages_template


        """
        response = self.client.open(
            f'/instrumentPackages/{self.inst}/templates',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_instrument_packages_scripts(self):
        """Test case for instrument_packages_parameter


        """
        response = self.client.open(
            f'/instrumentPackages/{self.inst}/parameters',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_instrument_packages_template_metadata(self):
        """Test case for instrument_packages_template_metadata


        """
        response = self.client.open(
            f'/instrumentPackages/{self.inst}/templates/metadata', method='GET')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_instrument_packages_scripts(self):
        """Test case for instrument_packages_ip_template


        """
        response = self.client.open(
            f'/instrumentPackages/{self.inst}/templates', method='GET')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
