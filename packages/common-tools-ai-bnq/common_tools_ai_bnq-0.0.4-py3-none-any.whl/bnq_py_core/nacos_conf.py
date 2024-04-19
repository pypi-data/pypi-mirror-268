# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # @time:2024/3/27 17:34
# # Author:Zhang HongTao
# # @File:nacos_conf.py
#
# import ast
# import json
#
# from nacos import NacosClient
# from utils.read_conf_from_ini import GetConfInfo
#
#
# class NacConnect(object):
#     """Redis读取类，用于记录运行中的信息
#
#     """
#     __instance = None  # 单例
#
#     def __new__(cls, *args, **kwargs):
#         """单例模式"""
#         if not cls.__instance:
#             cls.__instance = super(NacConnect, cls).__new__(cls, *args, **kwargs)
#
#         return cls.__instance
#
#     def __init__(self) -> None:
#         self.CONF = {}
#         self.nac_init()
#
#     def nac_init(self):
#         """
#
#         Returns:
#
#         """
#         get_conf_ins = GetConfInfo()
#         conf_in_nac = get_conf_ins.get_conf_info("NACOS_CONFIG")
#         info_of_nac = ast.literal_eval(conf_in_nac)
#         username = info_of_nac.get("username")
#         password = info_of_nac.get("password")
#         server_addresses = info_of_nac.get("server_addresses")
#         namespace = info_of_nac.get("namespace")
#         client = NacosClient(server_addresses=server_addresses, namespace=namespace, username=username,
#                              password=password)
#
#         COMMON_CONF = {}
#         group_dict = info_of_nac.get("group")
#         for group_name, data_ids in group_dict.items():
#             for data_id in data_ids:
#                 COMMON_CONF = self.get_and_watch(client, data_id, group_name, COMMON_CONF)
#
#         self.CONF = COMMON_CONF
#
#     @staticmethod
#     def get_and_watch(client, data_id, group, pre_conf=None):
#         """
#
#         Args:
#             client:
#             data_id:
#             group:
#             pre_conf:
#
#         Returns:
#
#         """
#         if pre_conf is None:
#             pre_conf = {}
#         conf = client.get_config(data_id, group)
#         if conf is None:
#             return pre_conf
#
#         conf = json.loads(conf)
#         for key, value in conf.items():
#             pre_conf[key] = value
#
#         return pre_conf
#
#
# if __name__ == "__main__":
#     conf_test = NacConnect()
