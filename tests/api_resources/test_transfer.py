from __future__ import absolute_import, division, print_function

import stripe_sub5


TEST_RESOURCE_ID = "tr_123"
TEST_REVERSAL_ID = "trr_123"


class TestTransfer(object):
    def test_is_listable(self, request_mock):
        resources = stripe_sub5.Transfer.list()
        request_mock.assert_requested("get", "/v1/transfers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe_sub5.Transfer)

    def test_is_retrievable(self, request_mock):
        resource = stripe_sub5.Transfer.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/transfers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe_sub5.Transfer)

    def test_is_creatable(self, request_mock):
        resource = stripe_sub5.Transfer.create(
            amount=100, currency="usd", destination="acct_123"
        )
        request_mock.assert_requested("post", "/v1/transfers")
        assert isinstance(resource, stripe_sub5.Transfer)

    def test_is_saveable(self, request_mock):
        resource = stripe_sub5.Transfer.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/transfers/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe_sub5.Transfer.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/transfers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe_sub5.Transfer)


class TestTransferReversals:
    def test_is_listable(self, request_mock):
        resources = stripe_sub5.Transfer.list_reversals(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/transfers/%s/reversals" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe_sub5.Reversal)

    def test_is_retrievable(self, request_mock):
        resource = stripe_sub5.Transfer.retrieve_reversal(
            TEST_RESOURCE_ID, TEST_REVERSAL_ID
        )
        request_mock.assert_requested(
            "get",
            "/v1/transfers/%s/reversals/%s"
            % (TEST_RESOURCE_ID, TEST_REVERSAL_ID),
        )
        assert isinstance(resource, stripe_sub5.Reversal)

    def test_is_creatable(self, request_mock):
        resource = stripe_sub5.Transfer.create_reversal(
            TEST_RESOURCE_ID, amount=100
        )
        request_mock.assert_requested(
            "post", "/v1/transfers/%s/reversals" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe_sub5.Reversal)

    def test_is_modifiable(self, request_mock):
        resource = stripe_sub5.Transfer.modify_reversal(
            TEST_RESOURCE_ID, TEST_REVERSAL_ID, metadata={"foo": "bar"}
        )
        request_mock.assert_requested(
            "post",
            "/v1/transfers/%s/reversals/%s"
            % (TEST_RESOURCE_ID, TEST_REVERSAL_ID),
        )
        assert isinstance(resource, stripe_sub5.Reversal)
