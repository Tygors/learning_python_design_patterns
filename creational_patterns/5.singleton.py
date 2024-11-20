#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


# 单例模式保证一个类只有一个实例
# 并提供一个全局访问点
# 优点是对唯一实例的受控访问
# 单例相当于全局变量

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
class MyClass(Singleton):
    def __init__(self, a):
        self.a = a

if __name__ == "__main__":
    ms1 = MyClass(1)
    ms2 = MyClass(2)
    print(ms1.a, ms2.a)
    print(id(ms1),id(ms2),id(ms1)==id(ms2))

# 1-如果实例只出现一次，如日志系统中只需要一个日志对象
# （否则两个日志对象同时操作一个文件就会造成造作冲突）
# 2-数据库连接池只需要创建一个对象来操作数据库
# 3-操作系统只需要创建一个文件系统对象来操作文件系统

