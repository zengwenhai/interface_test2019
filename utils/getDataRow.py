from config.readConfig import ReadConfig, getpath


class GetRow(object):

    def __init__(self):
        self.readconfig = ReadConfig('config', 'conf.ini')

    def get_url_col(self):
        """获取测试案例中url列数"""
        return self.readconfig.get_section_value('TESTCASE_COL', 'URL')

    def get_title_col(self):
        """获取测试案例中title列数"""
        return self.readconfig.get_section_value('TESTCASE_COL', 'TITLE')

    def get_data_col(self):
        """获取测试案例中data列数"""
        return self.readconfig.get_section_value('TESTCASE_COL', 'DATA')

    def get_isexute_col(self):
        """获取测试案例中isexute列数"""
        return self.readconfig.get_section_value('TESTCASE_COL', 'ISEXUTE')

    def get_method_col(self):
        """获取测试案例中method列数"""
        return self.readconfig.get_section_value('TESTCASE_COL', 'METHOD')

    def get_except_col(self):
        """获取测试案例中except列数"""
        return self.readconfig.get_section_value('TESTCASE_COL', 'EXCEPT')


if __name__ == '__main__':
    print(GetRow().get_url_col())