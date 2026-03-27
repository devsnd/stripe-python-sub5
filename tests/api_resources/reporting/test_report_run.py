from __future__ import absolute_import, division, print_function

import stripe_sub5


TEST_RESOURCE_ID = "frr_123"


class TestReportRun(object):
    def test_is_creatable(self, request_mock):
        resource = stripe_sub5.reporting.ReportRun.create(
            parameters={"connected_account": "acct_123"},
            report_type="activity.summary.1",
        )
        request_mock.assert_requested("post", "/v1/reporting/report_runs")
        assert isinstance(resource, stripe_sub5.reporting.ReportRun)

    def test_is_listable(self, request_mock):
        resources = stripe_sub5.reporting.ReportRun.list()
        request_mock.assert_requested("get", "/v1/reporting/report_runs")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe_sub5.reporting.ReportRun)

    def test_is_retrievable(self, request_mock):
        resource = stripe_sub5.reporting.ReportRun.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/reporting/report_runs/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe_sub5.reporting.ReportRun)
