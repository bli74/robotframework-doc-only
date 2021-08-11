from robot.api import TestSuite
from robot.model import Keywords, Tags
from robot.running.model import TestCase
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
        testsuite.keywords = Keywords()
        testsuite.source = None
        for suite in testsuite.suites:
            self.cleanup_suite(suite)
        for test in testsuite.tests:
            self.cleanup_test(test)

    def cleanup_test(self, testcase: TestCase):
        testcase.keywords = Keywords()
        testcase.tags = Tags()
