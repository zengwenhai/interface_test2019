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
from config.readConfig import ReadConfig


class AllTest(object):

    def __init__(self):
        # self.report_path = os.path.join(getpath('data', 'report'), '%sreport.html' % get_time())
        self.report_path = os.path.join(getpath('data', 'report'))
        self.test_path = getpath('testcase', '')
        self.readconf = ReadConfig('config', 'conf.ini')
        self.email = Email()

    def add_suite_test(self):
        discover = unittest.defaultTestLoader.discover(
            self.test_path,
            pattern='*test.py',
            top_level_dir=None
        )
        print(self.test_path)
        return discover

    def run(self):
        # with open(self.report_path, 'wb') as f:
        #     runner = HTMLTestRunner(f,
        #                             description='测试',
        #                             title='测试报告',
        #                             verbosity=2)
        #     runner.run(self.add_suite_test())
        try:
            runner = BeautifulReport(self.add_suite_test())
            runner.report(filename='TestReport%s' % get_time(),
                      description='测试接口报告',
                      log_path=self.report_path)
        except Exception as e:
            print(e)
        finally:
            on_off = self.readconf.get_section_value('EMAIL', 'ON_OFF')
            print(on_off)
            if on_off == 'on':
                self.email.send()
            else:
                print('不发送邮件！')


if __name__ == '__main__':
    alltest = AllTest()
    alltest.run()
    print(alltest.add_suite_test())