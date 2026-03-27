from __future__ import absolute_import, division, print_function

import stripe_sub5


class TestBalance(object):
    def test_is_retrievable(self, request_mock):
        resource = stripe_sub5.Balance.retrieve()
        request_mock.assert_requested("get", "/v1/balance")
        assert isinstance(resource, stripe_sub5.Balance)
