# coding: utf-8

"""
    osparc.io web API

    osparc-simcore public web API specifications  # noqa: E501

    The version of the OpenAPI document: 0.4.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import datetime
import unittest

import osparc
from osparc import ProfileUpdate  # noqa: E501
from osparc import ApiException


class TestProfileUpdate(unittest.TestCase):
    """ProfileUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProfileUpdate
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = osparc.models.profile_update.ProfileUpdate()  # noqa: E501
        if include_optional:
            return ProfileUpdate(first_name="James", last_name="Maxwell")
        else:
            return ProfileUpdate()

    def testProfileUpdate(self):
        """Test ProfileUpdate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()