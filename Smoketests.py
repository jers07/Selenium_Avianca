from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from find_test import FindTest
from assertions import AssertionsTest


assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
Search_test = TestLoader().loadTestsFromTestCase(FindTest)

smoke_test = TestSuite([assertions_test, Search_test])

kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)