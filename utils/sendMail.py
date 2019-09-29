import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error


class Email(object):

    def __init__(self, server, sender, password, receiver, title, message=None, path=None):
        """

        :param server:
        :param sender:
        :param password:
        :param receiver:
        :param title:
        :param message:
        :param path:
        """
        self.server = server
        self.sender = sender
        self.password = password
        self.receiver = receiver
        self.title = title
        self.files = path
        self.message = message
        self.msg = MIMEMultipart('related')

    def attach_file(self, att_file):
        """将单个文件添加到附件列表中"""
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        print(file_name)
        att['Content-Disposition'] = 'attachment; filename="%s"' % file_name[-1]
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
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self.attach_file(f)
            elif isinstance(self.files, str):
                self.attach_file(self.files)
        print(type(self.files))

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)
        except (gaierror and error) as e:
            raise ('发送邮件失败，无法连接到SMTP服务器，检查网络以及SMTP服务器%s', e)
        else:
            try:
                smtp_server.login(self.sender, self.password)
            except smtplib.SMTPAuthenticationError as e:
                raise ("用户名密码验证失败！%s", e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())
            finally:
                smtp_server.quit()


if __name__ == '__main__':
    e = Email(server='smtp.126.com',
              sender='zwh2537@126.com',
              password='ABc19891969',
              receiver='374448636@qq.com',
              title='测试报告',
              message='test',
              path=r'E:\接口测试\data\report\2019-09-26-16-53-25report.html')
    e.send()