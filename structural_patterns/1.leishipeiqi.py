#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


# 类适配器使用多继承
# 对象适配器使用组合

# 组合
# 组合就是在一个类中放入另一个类的对象
class A:
	pass
	
class B:
	def __init__(self):
		self.a = A()
		

# 类适配器
from abc import ABCMeta, abstractmethod

# 目标接口
class Payment(metaclass=ABCMeta):
	@abstractmethod
	def pay(self, money):
		pass
	
# 一开始只有ali
class Alipay(Payment):
    def pay(self, money):
        print(f'支付了{money}元')
	

# 现在多了一个BankPay,但用的是cost方法
# 待适配的类
class BankPay():
    def cost(self, money):
        print(f'银联支付了{money}')
	

# 类适配器,用多继承
class BankPayAdapter(Payment, BankPay):
    """
        把不兼容的cost转换成pay
    """
    def pay(self, money):
          self.cost(money)

if __name__ == "__main__":
      p = BankPayAdapter()
      p.pay(100)