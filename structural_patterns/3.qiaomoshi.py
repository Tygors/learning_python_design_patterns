#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


# 桥模式是将一个事物的两个维度分离，使其可以独立地变化
# 在事物有两个维度的表现，两个维度都可能扩展时使用桥模式

# 优点是使得抽象和实现相分离，扩展能力强
# 如果不使用桥模式，在任何维度进行扩展时，都要改好多代码，因为使用了继承

# 举个例子，画一个可以填充颜色的几何形状，即有形状和颜色两个维度
# 紧耦合型代码
class Shape:
	pass


class Rectangle(Shape):
	pass

class Circle(Shape):
	pass


class RedRectangle(Rectangle):
	pass

class GreenRectangle(Rectangle):
	pass


class RedCircle(Circle):
	pass

class GreenCircle(Circle):
	pass


# 应用桥模式的思想，可以实现松耦合（利用组合来实现）
from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    def __init__(self, color_ins):
        self.color_ins = color_ins
    # 一方面子类要把需要填充的颜色实例传进来
    # 一方面还要实现draw方法，这里也就是还需要用上颜色实例的方法
    @abstractmethod
    def draw(self):
	    pass

class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass

class Rectangle(Shape):
	name = "长方形"
	def draw(self):
		self.color_ins.paint(self)#这里括号里的self不能漏
		
# 如果要扩展形状，只需要添加形状类
class Circle(Shape):
	name = "圆形"
	def draw(self):
	    self.color_ins.paint(self)#这里括号里的self不能漏
	    
class Red(Color):
	def paint(self, shape_ins):
		print(f"红色的{shape_ins.name}")
		
# 如果要扩展颜色，则增加颜色类
class Green(Color):
	def paint(self, shape_ins):
		print(f"绿色的{shape_ins.name}")
		
if __name__ == "__main__":
	rect = Rectangle(Red())
	rect.draw()
	cir = Circle(Green())
	cir.draw()