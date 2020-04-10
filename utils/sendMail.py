import re
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error
from config.readConfig import ReadConfig
from config.readYaml import ReadYaml
from utils.log import Logger


class Email(object):

    def __init__(self):
        """

        :param server:
        :param sender:
        :param password:
        :param receiver:
        :param title:
        :param message:
        :param path:
        """
        self.readconf = ReadConfig('config', 'conf.ini')
        self.readyaml = ReadYaml()
        self.server = self.readconf.get_section_value('EMAIL', 'SERVER')
        self.sender = self.readconf.get_section_value('EMAIL', 'SENDER')
        self.password = self.readconf.get_section_value('EMAIL', 'PASSWORD')
        self.receiver = self.readconf.get_section_value('EMAIL', 'RECEIVER')
        self.title = self.readconf.get_section_value('EMAIL', 'TITLE')
        # self.files = self.readconf.get_section_value('EMAIL', 'REPORT_PATH')
        self.files = self.readyaml.get_value()['EMAIL']['REPORT_PATH']
        self.message = self.readconf.get_section_value('EMAIL', 'MESSAGE')
        self.msg = MIMEMultipart('related')
        self.logger = Logger().get_logger()

    def file_sort(self, path):
        lists = os.listdir(path)  # 获取该目录下的所有文件，结果以列表形式返回
        lists.sort(key=lambda fn: os.path.getmtime(os.path.join(path, fn)))  # 最后对lists元素，按文件修改时间大小从小到大排序
        file_path = os.path.join(path, lists[-1])
        return file_path

    def get_new_file(self, path):
        """根据文件最近的修改时间获取最新的测试报告"""
        file_path_list = []
        if isinstance(path, list):
            for i in path:
                file_path_list.append(self.file_sort(i))
            return file_path_list
        elif isinstance(path, str):
            return self.file_sort(path)

    def attach_file(self, att_file):
        """将单个文件添加到附件列表中"""
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att['Content-Disposition'] = 'attachment; filename="%s"' % file_name[-1].encode('utf-8')
        self.msg.attach(att)

    def send(self):
        """"""
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        # 添加邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))

        # 添加附近，支持多个附近传入(传入list)或者单个附件(传入str)
        if self.get_new_file(self.files):
            if isinstance(self.get_new_file(self.files), list):
                for f in self.get_new_file(self.files):
                    self.attach_file(f)
            elif isinstance(self.get_new_file(self.files), str):
                self.attach_file(self.get_new_file(self.files))

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)
        except (gaierror and error) as e:
            self.logger.info ('发送邮件失败，无法连接到SMTP服务器，检查网络以及SMTP服务器%s', e)
        else:
            try:
                smtp_server.login(self.sender, self.password)
                print('邮件发送成功，如果收件箱没看到邮件，请查看一下垃圾箱！')
            except smtplib.SMTPAuthenticationError as e:
                self.logger.info ("用户名密码验证失败！%s", e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())
            finally:
                smtp_server.quit()


if __name__ == '__main__':
    e = Email()
    e.send()
    # print(e.get_new_file(r'E:\接口测试\data\report'))