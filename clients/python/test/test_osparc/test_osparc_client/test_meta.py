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
from osparc import Meta  # noqa: E501
from osparc import ApiException


class TestMeta(unittest.TestCase):
    """Meta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Meta
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = osparc.models.meta.Meta()  # noqa: E501
        if include_optional:
            return Meta(
                name="0",
                version="0.5.0",
                released={"key": "a"},
                docs_url="https://docs.osparc.io",
                docs_dev_url="https://api.osparc.io/dev/docs",
            )
        else:
            return Meta(
                name="0",
                version="0.5.0",
                docs_url="https://docs.osparc.io",
                docs_dev_url="https://api.osparc.io/dev/docs",
            )

    def testMeta(self):
        """Test Meta"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()