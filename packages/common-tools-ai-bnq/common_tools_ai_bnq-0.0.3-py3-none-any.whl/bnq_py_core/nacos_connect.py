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
        eg:  {'group':{'AI-UAT':['spaceDesign']},'username':'nacos','password':'nacos','server_addresses':'127.0.0.1:8080','namespace':'AI-UAT'}

    """
    __instance = None  # 单例

    def __new__(cls, *args, **kwargs):
        """单例模式"""
        if not cls.__instance:
            cls.__instance = super(NacConnect, cls).__new__(cls, *args, **kwargs)

        return cls.__instance

    def __init__(self, server_addresses, namespace, username, password, group_dict) -> None:
        """

        :param server_addresses: 地址
        :param namespace: 命名空间
        :param username: 用户名
        :param password: 密码
        :param group_dict: 组合字典
        """
        self.CONF = {}
        self.server_addresses = server_addresses  # 地址
        self.namespace = namespace  # 命名空间
        self.username = username  # 用户名
        self.password = password  # 密码
        self.group_dict = group_dict  # 组
        self.nac_init()

    def __call__(self, *args, **kwargs):
        return self.CONF

    def nac_init(self):
        """初始化

        Returns:

        """
        client = NacosClient(server_addresses=self.server_addresses,
                             namespace=self.namespace,
                             username=self.username,
                             password=self.password)
        COMMON_CONF = {}
        for group_name, data_ids in self.group_dict.items():
            for data_id in data_ids:
                COMMON_CONF = self.get_and_watch(client, data_id, group_name, COMMON_CONF)

        self.CONF = COMMON_CONF

    @staticmethod
    def get_and_watch(client, data_id, group, pre_conf=None):
        """

        Args:
            client:
            data_id:
            group:
            pre_conf:

        Returns:

        """
        if pre_conf is None:
            pre_conf = {}
        conf = client.get_config(data_id, group)
        if conf is None:
            return pre_conf

        conf = json.loads(conf)
        for key, value in conf.items():
            pre_conf[key] = value

        return pre_conf


if __name__ == "__main__":
    conf_test = NacConnect()
