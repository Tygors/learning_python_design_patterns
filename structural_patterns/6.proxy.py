#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


# 代理模式为其它对象提供一种代理以控制对这个对象的访问
# 重点在于控制
# 应用场景有远程代理：为远程的对象提供代理（通过ORM向数据库写值，不用关注数据库是在远程）

# 虚代理：根据需要创建很大的对象（需要的时候创建对象）
# 保护代理：控制对原始对象的访问，用于对象有不同的访问权限

# 不用虚代理
from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

# 如果不用虚代理，则一次性会读完整个文件存在内存中
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        print('读取文件内容！')
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def get_content(self):
        return self.content

    def set_content(self, content):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(content)

subj = RealSubject('./data/test.txt')

# 以下使用虚代理
class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    # 在这里加了逻辑，判断真正调用的时候才拿文件数据
    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()
    
    # 在这里加了逻辑，真正调用才创建对象去调用真正的set
    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)

        return self.subj.set_content(content)
    
subj = VirtualProxy('data/test.txt')
# 上面创建这句不会拿数据
print(subj.get_content())
# 真正调用方法了，才通过代理创建

# 控制读写权限，用保护代理,这里控制可读不可写
class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()
    
    def set_content(self, content):
        raise PermissionError("无写入权限！")
    
subj = ProtectedProxy('data/test.txt')
print(subj.get_content())
subj.set_content('abc')