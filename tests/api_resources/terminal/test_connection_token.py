from __future__ import absolute_import, division, print_function

import stripe_sub5


TEST_RESOURCE_ID = "rdr_123"


class TestConnectionToken(object):
    def test_is_creatable(self, request_mock):
        resource = stripe_sub5.terminal.ConnectionToken.create()
        request_mock.assert_requested("post", "/v1/terminal/connection_tokens")
        assert isinstance(resource, stripe_sub5.terminal.ConnectionToken)
