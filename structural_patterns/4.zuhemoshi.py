#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


### 组合模式
'''
将对象组合成树形结构以表示 “部分-整体”的层次结构（尤其当结构是递归的情况）

组合模式使得用户对单个对象和组合对象的使用具有一致性

优点是定义了包含基本对象和组合对象的层次结构

简化客户端代码，客户端可以一致地使用组合对象或单个对象，更容易增加新类型的组件
'''

from abc import ABCMeta, abstractmethod

# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'点{self.x},{self.y}'
    
    def draw(self):
        print(self)
    
# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def __str__(self):
        return f"线段{self.p1},{self.p2}"
    
    def draw(self):
        print(self)

# 复合组件
class Picture(Graphic):
    def __init__(self, iterable_ins):
        self.children = []
        for g in iterable_ins:
            self.add(g)

    def add(self, graphic_ins):
        self.children.append(graphic_ins)

    def draw(self):
        for g in self.children:
            g.draw()

if __name__ == "__main__":
    print("单个对象图形")
    p = Point(1,2)
    print(p)
    p.draw()
    print("复杂组合图形")
    l1 = Line(Point(3,4), Point(5,6))
    l1.draw()
    l2 = Line(Point(6,7), Point(8,9))
    l2.draw()
    print(l1)
    print(l2)
    print("更复杂组合图形")
    pic = Picture([p,l1,l2])
    pic.draw()
    print(pic)