from __future__ import absolute_import, division, print_function

import stripe_sub5


TEST_RESOURCE_ID = "usd"


class TestExchangeRate(object):
    def test_is_listable(self, request_mock):
        resources = stripe_sub5.ExchangeRate.list()
        request_mock.assert_requested("get", "/v1/exchange_rates")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe_sub5.ExchangeRate)

    def test_is_retrievable(self, request_mock):
        resource = stripe_sub5.ExchangeRate.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/exchange_rates/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe_sub5.ExchangeRate)
