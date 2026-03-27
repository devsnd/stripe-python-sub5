from __future__ import absolute_import, division, print_function

import stripe_sub5


class TestSetupAttempt(object):
    def test_is_listable(self, request_mock):
        resources = stripe_sub5.SetupAttempt.list(setup_intent="seti_123")
        request_mock.assert_requested("get", "/v1/setup_attempts")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe_sub5.SetupAttempt)
