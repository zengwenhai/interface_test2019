import unittest
from utils.rundecorator import run_test
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson
from utils.getExcelCaseData import ReadExcel
from base.runmethod import RunMethod
from config.readConfig import ReadConfig
from utils.assertTest import assert_code
from utils.rundecorator import run_test
from urllib.parse import urljoin
import json


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.oper = OperationExcel('Sheet1')
        self.operjson = OperationJson('Sheet1')
        self.runmethod = RunMethod()
        self.readconfig = ReadConfig('config', 'conf.ini')
        self.data = ReadExcel(r'E:\接口测试\data\datacase\test.xls', 'Sheet1')

    def get_data(self):
        return self.data.get_data()

    def apicase(self, case_list):
        for i in case_list:
            url = urljoin(self.readconfig.get_section_value('HTTP', 'BASE_URL'), i['url'])  # 拼接url路径
        # data = json.loads(self.oper.get_data(2), encoding='utf-8')
            data = i['data']
            method = i['method']
            res = self.runmethod.run_main(url=url, data=data, method=method)

    def test_login_001(self):
        """测试登录成功"""
        self.apicase(self.get_data())

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)