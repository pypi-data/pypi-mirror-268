#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @time:2024/4/16 16:12
# Author:Zhang HongTao
# @File:test_pymysql.py

import pymysql

# 创建连接
conn = pymysql.connect(host='10.188.20.129',  # 数据库服务器地址
                       user='ro_ai',  # 数据库用户名
                       password='no3gyqgrs5s)bjLR',  # 数据库密码
                       database='iam_nana',  # 数据库名
                       port=30813,
                       charset='utf8'
                       )  # 数据库使用的字符集（在这里设为utf8）

# 创建游标
cursor = conn.cursor()

# 执行SQL语句
cursor.execute("SELECT * FROM quality_voices LIMIT 10")  # 选择table_name表中的所有数据

# 获取所有记录列表
results = cursor.fetchall()
for row in results:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()
