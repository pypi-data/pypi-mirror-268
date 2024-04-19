#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @time:2024/3/27 17:44
# Author:Zhang HongTao
# @File:read_conf_from_ini.py


import configparser
import os
import ast


class GetConfInfo:
    """获取配置文件中的信息
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        """单例模式

        :param args:
        :param kwargs:
        """
        if not cls.__instance:
            cls.__instance = super(GetConfInfo, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.conf = configparser.RawConfigParser()
        path_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.conf_path = os.path.join(path_file, "config", "conf.ini")
        self.conf.read(self.conf_path)
        log_env_path = os.path.join(path_file, 'logenv')
        self.field = self.get_field(log_env_path)

    @staticmethod
    def get_field(log_env_path):
        """根据log env记录的值，获取不同环境的配置参数

        :param log_env_path:
        :return:
        """
        field = "ENV-DEV"
        if not os.path.exists(log_env_path):
            # log env路径不存在，返回dev配置
            return field
        with open(log_env_path) as f:
            content_log = f.read()
            content_split = content_log.split('/')
        content_split = str(content_split).lower()
        if 'test' in content_split:
            field = "ENV-TEST"
        elif 'uat' in content_split:
            field = "ENV-UAT"
        elif 'prod' in content_split:
            field = "ENV-PROD"
        return field

    def get_conf_info(self, key):
        """获取key对应的配置信息

        :param key:
        :return:
        """
        conf_info = self.conf.get(self.field, key)
        return conf_info


if __name__ == '__main__':
    test_ins = GetConfInfo()
    res_t_1 = test_ins.get_conf_info("NACOS_CONFIG")
    res_t_2 = ast.literal_eval(res_t_1)
    print(res_t_1)
