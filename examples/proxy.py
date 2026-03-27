from __future__ import absolute_import, division, print_function

import os

import stripe_sub5


stripe_sub5.api_key = os.environ.get("STRIPE_SECRET_KEY")

print("Attempting charge...")

proxy = {
    "http": "http://<user>:<pass>@<proxy>:<port>",
    "https": "http://<user>:<pass>@<proxy>:<port>",
}

clients = (
    stripe_sub5.http_client.RequestsClient(
        verify_ssl_certs=stripe_sub5.verify_ssl_certs, proxy=proxy
    ),
    stripe_sub5.http_client.PycurlClient(
        verify_ssl_certs=stripe_sub5.verify_ssl_certs, proxy=proxy
    ),
    stripe_sub5.http_client.Urllib2Client(
        verify_ssl_certs=stripe_sub5.verify_ssl_certs, proxy=proxy
    ),
)

for c in clients:
    stripe_sub5.default_http_client = c
    resp = stripe_sub5.Charge.create(
        amount=200,
        currency="usd",
        card="tok_visa",
        description="customer@gmail.com",
    )
    print("Success: %s, %r" % (c.name, resp))
