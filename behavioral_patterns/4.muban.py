#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


# 模板方法模式定义一个操作中的算法骨架，将一些步骤延迟到子类中
# 模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤

# 抽象类的作用是是定义抽象类（钩子操作），实现一个模板方法作为算法的骨架。
# 具体类的作用实现原子操作。

from abc import ABCMeta, abstractmethod
from time import sleep

# 一个windows一直刷新画面的例子
# 抽象类
class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):  # 原子操作/钩子操作
        pass

    @abstractmethod
    def repaint(self):  # 原子操作/钩子操作
        pass

    @abstractmethod
    def stop(self):  # 原子操作/钩子操作
        pass
    
    # 一共四个方法，只需要改变前三个要改变的，即因此推迟到子类写结构
    # 第四个run方法，则是每个子类都一样的
    def run(self):
        """
        模板方法(具体方法)，这个大逻辑就不需要自己写了
        """
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()

# 具体类，只需要实现三个抽象方法，而run方法是统一的
class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print('窗口开始运行！')

    def stop(self):
        print('窗口停止运行！')

    def repaint(self):
        print(self.msg)

if __name__ == "__main__":
    a = MyWindow("hi,你好")
    a.run()

'''
模板方法适用的场景：一次性实现一个算法的不变部分，各个子类中的公共行为应该被提取出来并集中到一个公共父类中以避免代码重复；控制子类扩展。
'''