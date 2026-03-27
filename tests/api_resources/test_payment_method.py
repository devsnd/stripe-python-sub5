from __future__ import absolute_import, division, print_function

import stripe_sub5


TEST_RESOURCE_ID = "pm_123"


class TestPaymentMethod(object):
    def test_is_listable(self, request_mock):
        resources = stripe_sub5.PaymentMethod.list(customer="cus_123", type="card")
        request_mock.assert_requested("get", "/v1/payment_methods")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe_sub5.PaymentMethod)

    def test_is_retrievable(self, request_mock):
        resource = stripe_sub5.PaymentMethod.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/payment_methods/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe_sub5.PaymentMethod)

    def test_is_creatable(self, request_mock):
        resource = stripe_sub5.PaymentMethod.create(
            type="card", card={"token": "tok_123"}
        )
        request_mock.assert_requested("post", "/v1/payment_methods")
        assert isinstance(resource, stripe_sub5.PaymentMethod)

    def test_is_saveable(self, request_mock):
        resource = stripe_sub5.PaymentMethod.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/payment_methods/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe_sub5.PaymentMethod.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/payment_methods/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe_sub5.PaymentMethod)

    def test_can_attach(self, request_mock):
        resource = stripe_sub5.PaymentMethod.retrieve(TEST_RESOURCE_ID)
        resource = resource.attach(customer="cus_123")
        request_mock.assert_requested(
            "post", "/v1/payment_methods/%s/attach" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe_sub5.PaymentMethod)

    def test_can_attach_classmethod(self, request_mock):
        resource = stripe_sub5.PaymentMethod.attach(
            TEST_RESOURCE_ID, customer="cus_123"
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_methods/%s/attach" % TEST_RESOURCE_ID,
            {"customer": "cus_123"},
        )
        assert isinstance(resource, stripe_sub5.PaymentMethod)

    def test_can_detach(self, request_mock):
        resource = stripe_sub5.PaymentMethod.retrieve(TEST_RESOURCE_ID)
        resource = resource.detach()
        request_mock.assert_requested(
            "post", "/v1/payment_methods/%s/detach" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe_sub5.PaymentMethod)

    def test_can_detach_classmethod(self, request_mock):
        resource = stripe_sub5.PaymentMethod.detach(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/payment_methods/%s/detach" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe_sub5.PaymentMethod)
