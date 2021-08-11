from robot.model import Tags
from robot.running.model import Body, Keyword, TestCase, TestSuite
from robot.testdoc import TestDoc, TestSuiteFactory
from robot.utils import abspath


class TestDocSmall(TestDoc):

    def main(self, datasources, title=None, **options):
        outfile = abspath(datasources.pop())
        suite = TestSuiteFactory(datasources, **options)
        self.cleanup_suite(suite)
        self._write_test_doc(suite, outfile, title)
        self.console(outfile)

    def cleanup_suite(self, testsuite: TestSuite):
        testsuite.setup = None
        testsuite.teardown = None
        testsuite.source = None
        for suite in testsuite.suites:
            self.cleanup_suite(suite)
        for test in testsuite.tests:
            self.cleanup_test(test)


    def cleanup_test(self, testcase: TestCase):
        testcase.setup = None
        testcase.body = None
        testcase.teardown = None
        testcase.tags = None
