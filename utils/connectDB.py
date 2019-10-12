import pymysql
from config.readConfig import ReadConfig


class ConnectDb(object):

    def __init__(self):
        self.readconfig = ReadConfig('config', 'conf.ini')
        self.IP = self.readconfig.get_section_value('DATABASE', 'IP')
        self.PORT = self.readconfig.get_section_value('DATABASE', 'PORT')
        self.USER = self.readconfig.get_section_value('DATABASE', 'USERNAME')
        self.PASSWORD = self.readconfig.get_section_value('DATABASE', 'PASSWORD')
        self.DATABASE = self.readconfig.get_section_value('DATABASE', 'DATABASE')
        self.RETURN_RESULT_TYPE = self.readconfig.get_section_value('DATABASE', 'RETURN_RESULT_TYPE')
        self.conn = None
        self.cursor = None

    def connect_db(self):
        try:
            self.conn = pymysql.connect(host=self.IP, user=self.USER, password=self.PASSWORD, port=int(self.PORT), db=self.DATABASE)
            print("数据库连接成功！")
        except Exception as e:
            print(e)
        return self.conn

    def get_cursor(self):
        """创建数据库操作句柄"""
        if self.RETURN_RESULT_TYPE == 0:  # 0返回结果为元组形式，1返回结果为字典形式
            self.cursor = self.conn.cursor()
        else:
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        return self.cursor

    def close_db(self):
        """关闭数据库连接和数据库操作句柄"""
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql, params=None):
        """执行sql语句，数据集存在cursor句柄中"""
        self.cursor.execute(sql, params)
        # data = cursor.fetchone()
        # return data

    def get_one_data(self):
        """获取一条数据"""
        try:
            data = self.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.close_db()  # 关闭数据库连接
        return data

    def get_all_data(self):
        """获取全部数据"""
        try:
            data = self.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.close_db()
        return data


if __name__ == '__main__':
    sql = 'select * from user'
    c = ConnectDb()
    con = c.connect_db()
    cur = c.get_cursor()
    c.execute_sql(sql)
    print(c.get_all_data())