# coding: utf-8

from __future__ import absolute_import

import json
from six import BytesIO

from papahana.models.instrument_enum import InstrumentEnum  # noqa: E501
from papahana.models.instrument_package import InstrumentPackage  # noqa: E501
from papahana.test import BaseTestCase


class TestInstrumentController(BaseTestCase):
    """InstrumentController integration test stubs"""
    def setUp(self):
        """
        Insert a new OB to work with
        """
        self.set_api_cookie()
        self.inst = 'KCWI'

    def test_instrument_packages(self):
        """Test case for instrument_packages

        
        """
        response = self.client.open(
            f'/instrumentPackages/{self.inst}',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_instrument_packages_templates(self):
        """Test case for instrument_packages_template


        """
        response = self.client.open(
            f'/instrumentPackages/{self.inst}/templates',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    # def test_instrument_packages_ip_parameter(self):
    #     """Test case for instrument_packages_ip_parameter
    #
    #
    #     """
    #     response = self.client.open(
    #         '/instrumentPackages/{instrument}/parameters'.format(instrument=InstrumentEnum(), ip_version=1.2),
    #         method='GET')
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))
    #
    # def test_instrument_packages_ip_template(self):
    #     """Test case for instrument_packages_ip_template
    #
    #
    #     """
    #     response = self.client.open(
    #         '/instrumentPackages/{instrument}/{template_name}'.format(instrument=InstrumentEnum(),
    #                                                                                   ip_version=1.2,
    #                                                                                   template_name='template_name_example'),
    #         method='GET')
    #     self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
