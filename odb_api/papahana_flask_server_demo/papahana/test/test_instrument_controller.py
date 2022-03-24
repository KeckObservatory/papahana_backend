# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from papahana.models.instrument_enum import InstrumentEnum  # noqa: E501
from papahana.models.instrument_package import InstrumentPackage  # noqa: E501
from papahana.test import BaseTestCase


class TestInstrumentController(BaseTestCase):
    """InstrumentController integration test stubs"""

    def test_instrument_packages(self):
        """Test case for instrument_packages

        
        """
        response = self.client.open(
            '/v0/instrumentPackages/{instrument}'.format(instrument=InstrumentEnum()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_instrument_packages_ip_parameter(self):
        """Test case for instrument_packages_ip_parameter

        
        """
        response = self.client.open(
            '/v0/instrumentPackages/{instrument}/{ip_version}/parameters'.format(instrument=InstrumentEnum(), ip_version=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_instrument_packages_ip_template(self):
        """Test case for instrument_packages_ip_template


        """
        response = self.client.open(
            '/v0/instrumentPackages/{instrument}/{ip_version}/{template_name}'.format(instrument=InstrumentEnum(),
                                                                                      ip_version=1.2,
                                                                                      template_name='template_name_example'),
            method='GET')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
