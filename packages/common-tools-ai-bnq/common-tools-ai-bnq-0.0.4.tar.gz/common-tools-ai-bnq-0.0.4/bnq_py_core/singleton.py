#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @time:2023/4/14 18:12
# Author:Zhang HongTao
# @File:singleton.py

class SingletonMeta(type):
    """
    定义了一个名为SingletonMeta的元类，
    通过定义__call__方法来控制类的实例化过程，确保只创建一个实例。
    然后在定义类SingletonClass时，指定其元类为SingletonMeta，
    从而将SingletonClass变为单例模式
    """
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


# 示例
class SingletonClass(metaclass=SingletonMeta):
    pass
