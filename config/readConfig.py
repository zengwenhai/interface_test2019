from configparser import ConfigParser
from config.getPath import getpath


class MyConfigParser(ConfigParser):
    """这个类继承ConfigParser注意是为了改写optionform方法，去掉原方法中的写入ini文件自动转为小写的问题"""

    def __init__(self):
        ConfigParser.__init__(self)

    def optionxform(self, optionstr):
        return optionstr


class ReadConfig(object):

    def __init__(self, filepath, filename):
        self.path = getpath(filepath, filename)
        # self.readconfig = ConfigParser()
        self.readconfig = MyConfigParser()
        self.readconfig.read(self.path, encoding='utf-8')

    def get_section(self, sectionname):
        """获取配置文件中的键值对数据,以列表形式返回"""
        return self.readconfig.items(sectionname)

    def get_section_value(self, sectionname, optionname):
        """获取指定节点下的键值对"""
        return self.readconfig.get(sectionname, optionname)

    def write_section_value(self, sectionname, optionname, value):
        """将通用配置信息写入配置文件中"""
        if self.readconfig.has_section(sectionname):
            self.readconfig.set(sectionname, optionname, value)
            with open(self.path, 'w+', encoding='utf-8') as f:
                self.readconfig.write(f)
        else:
            self.readconfig.add_section(sectionname)
            self.readconfig.set(sectionname, optionname, value)
            with open(self.path, 'w+', encoding='utf-8') as f:
                self.readconfig.write(f)


if __name__ == "__main__":
    conf = ReadConfig('config', 'conf.ini')
    print(conf.get_section('DATABASE'))
    print(conf.get_section_value('DATABASE', 'IP'))
    # conf.write_section_value('HTTP', 'TOKEN', '12345')
    # print(urljoin(conf.get_section_value('HTTP', 'BASE_URL'), 'login/123'))