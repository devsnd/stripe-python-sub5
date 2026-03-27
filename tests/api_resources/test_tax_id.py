from __future__ import absolute_import, division, print_function

import pytest

import stripe_sub5


TEST_RESOURCE_ID = "txi_123"


class TestTaxId(object):
    def construct_resource(self):
        tax_id_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "tax_id",
            "customer": "cus_123",
        }
        return stripe_sub5.TaxId.construct_from(tax_id_dict, stripe_sub5.api_key)

    def test_has_instance_url(self, request_mock):
        resource = self.construct_resource()
        assert (
            resource.instance_url()
            == "/v1/customers/cus_123/tax_ids/%s" % TEST_RESOURCE_ID
        )

    def test_is_not_retrievable(self, request_mock):
        with pytest.raises(NotImplementedError):
            stripe_sub5.TaxId.retrieve(TEST_RESOURCE_ID)
