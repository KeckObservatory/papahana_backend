# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.instrument_package import InstrumentPackage  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTemplatesController(BaseTestCase):
    """TemplatesController integration test stubs"""

    def test_instrument_packages_ip_template(self):
        """Test case for instrument_packages_ip_template

        
        """
        response = self.client.open(
            '/v0/instrumentPackages/{instrument}/{ip_version}/{template_name}'.format(instrument='instrument_example', ip_version=56, template_name='template_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
