from __future__ import absolute_import, division, print_function

import stripe_sub5


TEST_RESOURCE_ID = "fee_123"
TEST_FEEREFUND_ID = "fr_123"


class TestApplicationFee(object):
    def test_is_listable(self, request_mock):
        resources = stripe_sub5.ApplicationFee.list()
        request_mock.assert_requested("get", "/v1/application_fees")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe_sub5.ApplicationFee)


class TestApplicationFeeRefunds(object):
    def test_is_listable(self, request_mock):
        resources = stripe_sub5.ApplicationFee.list_refunds(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/application_fees/%s/refunds" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe_sub5.ApplicationFeeRefund)

    def test_is_retrievable(self, request_mock):
        resource = stripe_sub5.ApplicationFee.retrieve_refund(
            TEST_RESOURCE_ID, TEST_FEEREFUND_ID
        )
        request_mock.assert_requested(
            "get",
            "/v1/application_fees/%s/refunds/%s"
            % (TEST_RESOURCE_ID, TEST_FEEREFUND_ID),
        )
        assert isinstance(resource, stripe_sub5.ApplicationFeeRefund)

    def test_is_creatable(self, request_mock):
        resource = stripe_sub5.ApplicationFee.create_refund(
            TEST_RESOURCE_ID, amount=100
        )
        request_mock.assert_requested(
            "post", "/v1/application_fees/%s/refunds" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe_sub5.ApplicationFeeRefund)

    def test_is_modifiable(self, request_mock):
        resource = stripe_sub5.ApplicationFee.modify_refund(
            TEST_RESOURCE_ID, TEST_FEEREFUND_ID, metadata={"foo": "bar"}
        )
        request_mock.assert_requested(
            "post",
            "/v1/application_fees/%s/refunds/%s"
            % (TEST_RESOURCE_ID, TEST_FEEREFUND_ID),
        )
        assert isinstance(resource, stripe_sub5.ApplicationFeeRefund)
