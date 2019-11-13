import json
from utils.operationExcel import OperationExcel
from config.getPath import getpath


class OperationJson(object):

    def __init__(self, sheetname):
        self.oper = OperationExcel(sheetname)
        self.path = getpath('data', 'requestData.json')

    def read_json(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    def get_request_data(self, row):
        """通过用例id获取对应的请求参数"""
        return self.read_json()[self.oper.get_data(row=row)]


if __name__ == '__main__':
    oper = OperationJson('Sheet1')
    print(oper.get_request_data(2))