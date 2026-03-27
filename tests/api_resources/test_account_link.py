from __future__ import absolute_import, division, print_function

import stripe_sub5


class TestAccountLink(object):
    def test_is_creatable(self, request_mock):
        resource = stripe_sub5.AccountLink.create(
            account="acct_123",
            refresh_url="https://stripe.com/failure",
            return_url="https://stripe.com/success",
            type="account_onboarding",
        )
        request_mock.assert_requested("post", "/v1/account_links")
        assert isinstance(resource, stripe_sub5.AccountLink)
