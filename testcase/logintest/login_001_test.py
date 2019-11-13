import unittest
from utils.rundecorator import run_test
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson
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

    def test_login_001(self):
        """测试登录成功"""
        # url = self.oper.get_url(2)
        url = urljoin(self.readconfig.get_section_value('HTTP', 'BASE_URL'), self.oper.get_data(2))  # 拼接url路径
        # data = json.loads(self.oper.get_data(2), encoding='utf-8')
        data = self.operjson.get_request_data(2)
        method = self.oper.get_method(2)
        res = self.runmethod.run_main(url=url, data=data, method=method)
        print(url)

    @unittest.skip("跳过该测试案例")
    def test_login_002(self):
        """测试登录，密码为空，登录失败"""
        url = self.oper.get_url(1)
        data = self.oper.get_data(1)
        method = self.oper.get_method(1)
        res = self.runmethod.run_main(url=url, params=data, method=method)
        self.assertEqual(res.json()['code'], '200')
        flag = assert_code(res.json()['code'])
        if flag == True:
            self.oper.write_value(1, 'pass')
        else:
            self.oper.write_value(1, 'fail')
        print(url)
        print(type(data))
        print(method)
        print(res.text)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)