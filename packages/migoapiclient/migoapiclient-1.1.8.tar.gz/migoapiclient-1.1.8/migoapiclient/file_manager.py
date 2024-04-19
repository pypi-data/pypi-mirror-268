"""
文件管理器
"""
import os
import sys

ITEM_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ITEM_PATH)


# 日志文件管理
class LogFileManager:
    def __init__(self, log_path: str):
        self.log_path = log_path
        if not os.path.exists(self.log_path):
            os.mkdir(self.log_path)

    def write_system_error_log(self, msg: str):
        """
        记录系统错误日志
        :param msg 错误信息
        """
        log_path = self.log_path + '/system_error.log'
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(msg + '\n')

    def write_request_error_log(self, msg: str):
        """
        记录请求错误日志
        :param msg 错误信息
        """
        log_path = self.log_path + '/request_error.log'
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(msg + '\n')


if __name__ == '__main__':
    pass
