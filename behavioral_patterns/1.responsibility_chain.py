#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


# 责任链模式，可以使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系
# 意思就是请求者只管无脑发请求
# 就像请假，会一直递到有权限的人手里批

from abc import ABCMeta, abstractmethod

# 抽象的处理者
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass

# 需要像链表一样的数据结构，可以在属性里加个next
# 因此从最高层级的类开始构建
# 先构建总经理
# 具体的处理者
class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 30:
            print('总经理准假%d' % day)
        else:
            print('可以辞职了！')

# 具体的处理者，经理的权限不足时，就传递给next，为总经理的实例
class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 7:
            print('项目主管准假%d' % day)
        else:
            print('部门经理职权不足')
            self.next.handle_leave(day)

# 具体的处理者,主管权限不足时，会传递给next为部门经理的实例
class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print('项目主管准假%d' % day)
        else:
            print('项目主管职权不足')
            self.next.handle_leave(day)

if __name__ == "__main__":
    day = 20
    p = ProjectDirector()
    p.handle_leave(day)
    print("-"*20)
    day = 3
    p.handle_leave(day)
    print("-"*20)
    day = 32
    p.handle_leave(day)