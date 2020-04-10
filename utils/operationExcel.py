import xlrd
from xlutils.copy import copy
from config.getPath import getpath
from utils.getDataRow import GetRow


class OperationExcel(object):

    def __init__(self, sheetname):
        self.path = getpath('data', 'test.xls')
        self.operexcel = xlrd.open_workbook(self.path)
        self.sheet = self.operexcel.sheet_by_name(sheetname)
        self.getdatacol = GetRow()

    def get_rows(self):
        """获取测试案例总数"""
        return self.sheet.nrows - 1

    def get_row_col_value(self, row, col):
        """获取单元格数据"""
        return self.sheet.cell_value(row, col)

    def get_url(self, row):
        """获取用例列表中请求url"""
        return self.get_row_col_value(row, int(self.getdatacol.get_url_col()))

    def get_data(self, row):
        """获取用例列表中的请求参数"""
        return self.get_row_col_value(row, int(self.getdatacol.get_data_col()))

    def get_method(self, row):
        """获取用例列表中的请求方法参数"""
        return self.get_row_col_value(row, int(self.getdatacol.get_method_col()))

    def get_excute(self, row):
        """获取用例列表中的是否执行参数"""
        return self.get_row_col_value(row, int(self.getdatacol.get_isexute_col()))

    def write_value(self, row, value):
        """写入数据"""
        data = copy(self.operexcel)
        sheet = data.get_sheet(0)
        sheet.write(row, int(self.getdatacol.get_except_col()), value)
        data.save(self.path)

    def get_cell_value(self):
        """获取测试用例数据并添加到一个列表中"""
        cls = []
        nrow = self.sheet.nrows  # 获取测试用例的行数
        for i in range(nrow):  # 循环读取测试用例
            if self.sheet.row_values(i)[0] != 'CaseId':  # 如果第i行不等于CaseId，则将测试用例这一行数据添加到cls中
                cls.append(self.sheet.row_values(i))
        return cls


if __name__ == '__main__':
    oper = OperationExcel('Sheet1')
    print(oper.get_rows())
    # print(oper.get_row_col_value(1, 1))
    print(oper.get_url(1))
    print(oper.get_data(1))
    print(oper.get_cell_value())