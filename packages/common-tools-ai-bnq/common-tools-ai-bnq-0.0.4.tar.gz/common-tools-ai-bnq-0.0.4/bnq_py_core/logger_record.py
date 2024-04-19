#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @time:2024/3/27 17:36
# Author:Zhang HongTao
# @File:logger_record.py

import logging
import logging.config
import logging.handlers
import os
import pathlib
import time

from structlog import configure, processors, stdlib


class LoggingRecord(object):
    """日志记录类，用于记录运行中的信息

    """
    __instance = None  # 单例
    __filename = None  # 日志文件名

    def __new__(cls, log_dir=None, *args, **kwargs):
        """保证日志模块是单例模式"""
        if not cls.__instance:
            cls.__instance = super(LoggingRecord, cls).__new__(cls)
        __now_time = int(round(time.time()))
        __time_record = time.strftime("%Y%m%d", time.localtime(__now_time))
        if log_dir:
            cls.__filename = __time_record + "_" + log_dir + ".log"
        else:
            cls.__filename = __time_record + "_BNQ_AI.log"
        return cls.__instance

    def __init__(self, max_bytes=20 * 1024 * 1024, backup_count=10, log_level=logging.INFO, log_dir=None):
        self.record_info = None
        self.logger = None
        self.log_record_path = log_dir  # 日志记录路径
        self.max_bytes = max_bytes  # 日志文件大小
        self.backup_count = backup_count  # 日志文件备份数量
        self.level = log_level  # 日志级别
        self.init_log()

    def init_log(self):
        """初始化log模块

        Returns:

        """
        if self.log_record_path is None:
            # 获取根目录路径，并创建日志文件夹
            self.log_record_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "log")
        pathlib.Path(self.log_record_path).mkdir(parents=True, exist_ok=True)
        log_filename = os.path.join(self.log_record_path, self.__filename)
        logging.config.dictConfig({
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
                }
            },
            "handlers": {
                "file_handler": {
                    "level": self.level,
                    "formatter": "default",
                    "class": "concurrent_log_handler.ConcurrentRotatingFileHandler",
                    "filename": log_filename,
                    "maxBytes": self.max_bytes,
                    "backupCount": self.backup_count,
                    "encoding": "UTF-8"
                },
            },
            "loggers": {
                "": {
                    "handlers": ["file_handler"],
                    "level": self.level
                }
            }
        })
        configure(
            context_class=dict,
            logger_factory=stdlib.LoggerFactory(),
            wrapper_class=stdlib.BoundLogger,
            processors=[
                stdlib.filter_by_level,
                stdlib.PositionalArgumentsFormatter(),
                processors.StackInfoRenderer(),
                processors.format_exc_info,
                processors.UnicodeDecoder(),
                stdlib.render_to_log_kwargs]
        )
        self.logger = logging.getLogger("BNQ-AI")
        self.logger.level = self.level

    def debug(self, record_info):
        """debug级别的日志记录

        :param record_info:
        :return:
        """
        self.logger.debug(record_info)

    def info(self, record_info):
        """

        Args:
            record_info:

        Returns:

        """
        self.logger.info(record_info)

    def error(self, error_info, exc_info_=True):
        """

        Args:
            error_info:
            exc_info_:

        Returns:

        """
        self.logger.error(error_info, exc_info=exc_info_)

    def warning(self, warning_info):
        """

        Args:
            warning_info:

        Returns:

        """
        self.logger.warning(warning_info)

    def exception(self, exception_info):
        self.logger.exception(exception_info)


if __name__ == "__main__":
    testLog = LoggingRecord(log_level=logging.DEBUG)
    for i in range(10):
        print(i, 'i')
        print(testLog, "testLog")
        testLog.debug(i)
        testLog.info("中文测试")
        testLog.error(i)
        testLog.warning(i)
        testLog.exception(i)
        # time.sleep(3)
