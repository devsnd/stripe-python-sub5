from __future__ import absolute_import, division, print_function

import stripe_sub5


TEST_INVOICE_ID = "in_123"


class TestInvoiceLineItem(object):
    def test_deserialize(self, request_mock):
        invoice = stripe_sub5.Invoice.retrieve(TEST_INVOICE_ID)
        assert isinstance(invoice.lines.data, list)
        assert isinstance(invoice.lines.data[0], stripe_sub5.InvoiceLineItem)
