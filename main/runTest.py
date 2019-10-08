import unittest
import os
from config.getPath import getpath
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from BeautifulReport import BeautifulReport
from utils.getTime import get_time
import sys
print(sys.path)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class AllTest(object):

    def __init__(self):
        # self.report_path = os.path.join(getpath('data', 'report'), '%sreport.html' % get_time())
        self.report_path = os.path.join(getpath('data', 'report'))
        self.test_path = getpath('testcase', '')

    def add_suite_test(self):
        discover = unittest.defaultTestLoader.discover(
            self.test_path,
            pattern='*test.py',
            top_level_dir=None
        )
        return discover

    def run(self):
        # with open(self.report_path, 'wb') as f:
        #     runner = HTMLTestRunner(f,
        #                             description='测试',
        #                             title='测试报告',
        #                             verbosity=2)
        #     runner.run(self.add_suite_test())
        runner = BeautifulReport(self.add_suite_test())
        runner.report(filename='测试报告%s' % get_time(),
                      description='测试接口报告',
                      log_path=self.report_path)


if __name__ == '__main__':
    alltest = AllTest()
    alltest.run()