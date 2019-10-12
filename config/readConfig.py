from configparser import ConfigParser
from config.getPath import getpath


class ReadConfig(object):

    def __init__(self, filepath, filename):
        self.path = getpath(filepath, filename)
        self.readconfig = ConfigParser()
        self.readconfig.read(self.path, encoding='utf-8')

    def get_section(self, sectionname):
        """获取配置文件中的键值对数据,以列表形式返回"""
        return self.readconfig.items(sectionname)

    def get_section_value(self, sectionname, optionname):
        """获取指定节点下的键值对"""
        return self.readconfig.get(sectionname, optionname)


if __name__ == "__main__":
    conf = ReadConfig('config', 'conf.ini')
    print(conf.get_section('DATABASE'))
    print(conf.get_section_value('DATABASE', 'IP'))