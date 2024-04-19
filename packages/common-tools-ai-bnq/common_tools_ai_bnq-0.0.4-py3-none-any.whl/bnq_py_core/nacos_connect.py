#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @time:2024/3/27 17:34
# Author:Zhang HongTao
# @File:nacos_connect.py

import json

from nacos import NacosClient


class NacConnect(object):
    """Nacos连接类, 用于连接Nacos

    args:
        server_addresses: Nacos地址

        namespace: 命名空间

        username: 用户名

        password: 密码

        group_dict: 组合字典，
        eg:  {
                'group':{'t-dev':['project_name_1']},
                'username':'nacos',
                'password':'nacos',
                'server_addresses':'127.0.0.1:8080',
                'namespace':'t-dev'
        }

    """
    __instance = None  # 单例

    def __new__(cls, *args, **kwargs):
        """单例模式"""
        if not cls.__instance:
            cls.__instance = super(NacConnect, cls).__new__(cls)

        return cls.__instance

    def __init__(self, server_addresses, namespace, username, password, group) -> None:
        """

        :param server_addresses: 地址
        :param namespace: 命名空间
        :param username: 用户名
        :param password: 密码
        :param group: 组合字典
        """
        self.CONF = {}
        self.client = NacosClient(server_addresses=server_addresses,
                                  namespace=namespace,
                                  username=username,
                                  password=password)
        self.group = group
        self.main()

    def __call__(self, *args, **kwargs):
        return self.CONF

    def main(self):
        """初始化

        Returns:

        """

        COMMON_CONF = {}
        for group_name, data_ids in self.group.items():
            for data_id in data_ids:
                COMMON_CONF = self.get_and_watch(data_id, group_name, COMMON_CONF)

        self.CONF = COMMON_CONF

    def get_and_watch(self, data_id, group, pre_conf=None):
        """获取配置

        Args:
            data_id:
            group:
            pre_conf:

        Returns:

        """
        if pre_conf is None:
            pre_conf = {}
        conf = self.client.get_config(data_id, group)  # 获取配置
        if conf is None:
            return pre_conf

        conf = json.loads(conf)  # 转换为json
        for key, value in conf.items():
            pre_conf[key] = value

        return pre_conf


if __name__ == "__main__":
    test_data = {'group': {'t-dev': ['project_name_1', 'project_name_2']},
                 'username': 'nacos',
                 'password': 'nacos',
                 'server_addresses': '127.0.0.1:8080',
                 'namespace': 't-dev'}
    conf_test = NacConnect(**test_data)
    print(conf_test())
