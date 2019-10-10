import unittest
import sys
import os
import time
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
print(rootPath)
from config.getPath import getpath
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from BeautifulReport import BeautifulReport
from utils.getTime import get_time
from utils.sendMail import Email


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
        runner.report(filename='TestReport%s' % get_time(),
                      description='测试接口报告',
                      log_path=self.report_path)


if __name__ == '__main__':
    alltest = AllTest()
    e = Email(server='smtp.126.com',
              sender='zwh2537@126.com',
              password='ABc19891969',
              receiver='374448636@qq.com',
              title='测试报告',
              message='test',
              path=r'E:\接口测试\data\report')
    alltest.run()
    time.sleep(8)
    e.send()