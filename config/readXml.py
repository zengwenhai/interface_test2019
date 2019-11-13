from xml.etree.ElementTree import ElementTree
from config.getPath import getpath


class ReadXml(object):

    def __init__(self):
        self.path = getpath('config', 'SQL.xml')
        self.tree = ElementTree.parse(self, source=self.path)
        self.database = {}

    def set_xml(self):
        """将配置文件中的sql语句相关的表名、数据库名和sql语句添加到database字典中"""
        if len(self.database) == 0:
            for db in self.tree.findall("database"):
                db_name = db.get('name')
                table = {}
                for tb in db.getchildren():
                    table_name = tb.get('name')
                    sql = {}
                    for data in tb.getchildren():
                        sql_id = data.get('id')
                        sql[sql_id] = data.text
                    table[table_name] = sql
                self.database[db_name] = table
        return self.database

    def get_xml_dict(self, dataname, tablename):
        """获取存放在database字典中的sql语句字典"""
        self.set_xml()
        return self.database.get(dataname).get(tablename)

    def get_xml_sql(self, dataname, tablename, sql_id):
        """根据sql_id获取配置文件中的SQL语句"""
        data = self.get_xml_dict(dataname, tablename)
        return data.get(sql_id)


if __name__ == '__main__':
    r = ReadXml()
    # print(r.get_xml_dict('test01', 'testtable'))
    print(r.get_xml_sql('test01', 'testtable', 'delete_user'))