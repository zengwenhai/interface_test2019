from ruamel.yaml import YAML
from config.getPath import getpath


class ReadYaml(object):

    def __init__(self):
        self.yaml = YAML()  # 创建YAML对象
        self.path = getpath('config', 'confi.yaml')

    def get_value(self):
        """获取yaml配置文件的中数据"""
        with open(self.path, encoding='utf-8') as f:
            data = self.yaml.load(f)
            return data

    def write_value(self, value):
        """将字典类型数据转化为yaml格式的数据并写入文件中"""
        with open(self.path, 'a+', encoding='utf-8') as file:
            self.yaml.dump(value, file)


if __name__ == "__main__":
    r = ReadYaml()
    print(r.get_value()['EMAIL']['REPORT_PATH'])
    src_data = {'user': {'name': '可优', 'age': 17, 'money': None, 'gender': True},
                'lovers': ['柠檬小姐姐', '橘子小姐姐', '小可可']
                }
    #r.write_value(src_data)