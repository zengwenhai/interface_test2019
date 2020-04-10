import os
import logging
from logging.handlers import TimedRotatingFileHandler
from config.getPath import getpath
from config.readConfig import ReadConfig


class Logger(object):

    def __init__(self, logger_name='logname'):
        logging.root.setLevel(logging.NOTSET)  # 默认生成的root logger日志级别是WARNING，低于该级别的就不会输出，所以将root logger日志级别设置为最低
        self.readconfig = ReadConfig('config', 'conf.ini')
        self.log_file_path = getpath('data', 'log')
        self.logger = logging.getLogger(logger_name)
        self.file_output_level = self.readconfig.get_section_value('LOG', 'LEVEL')
        self.log_filename = self.readconfig.get_section_value('LOG', 'LOG_FILENAME')
        self.log_count = self.readconfig.get_section_value('LOG', 'COUNT')
        self.format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        """输出日志到文件中"""
        if not self.logger.handlers:
            """如果日志句柄不存在，则创建日志句柄"""
            file_handlers = TimedRotatingFileHandler(
                filename=os.path.join(self.log_file_path, self.log_filename),
                when='D',
                backupCount=self.log_count,
                interval=2,
                delay=True,
                encoding='utf-8'
            )
            file_handlers.setFormatter(self.format)
            file_handlers.setLevel(self.file_output_level)
            self.logger.addHandler(file_handlers)
        return self.logger


if __name__ == "__main__":
    log = Logger().get_logger()
    log.info("333333")