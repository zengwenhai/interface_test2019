from ruamel.yaml import YAML
from config.getPath import getpath


class ReadYaml(object):

    def __init__(self):
        self.yaml = YAML(typ='safe')  # 创建YAML对象
        self.path = getpath('config', 'confi.yaml')

    def get_value(self):
        with open(self.path, encoding='utf-8') as f:
            data = self.yaml.load(f)
            return data


if __name__ == "__main__":
    r = ReadYaml()
    print(r.get_value()['EMAIL']['REPORT_PATH'])