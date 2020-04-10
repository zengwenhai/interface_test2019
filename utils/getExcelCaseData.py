import xlrd
import os


class ReadExcel(object):

    def __init__(self, filepath, sheetname):
        self.data = xlrd.open_workbook(filepath)
        self.sheet = self.data.sheet_by_name(sheetname)
        self.rowNum = self.sheet.nrows  # 获取数据表行数
        self.colNum = self.sheet.ncols  # 获取数据表列数
        self.keys = self.sheet.row_values(0)  # 获取第一行的标题

    def get_data(self):
        if self.rowNum <= 1:
            print("没有数据！")
        else:
            r, j = [], 1
            for i in range(self.rowNum -1):
                s, values = {}, self.sheet.row_values(j)
                for k in range(self.colNum):
                    s[self.keys[k]] = values[k]
                    r.append(s)
                j += 1
                return r


if __name__ == "__main__":
    filepath = r'E:\接口测试\data\datacase\test.xls'
    sheetname = 'Sheet1'
    data = ReadExcel(filepath, sheetname)
    print(data.get_data())
    r = data.get_data()
    for i in r:
        print(i)