#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


# 简单工厂模式只创建一个工厂类
# 当有了新产品，都需要将新产品类加到工厂中
# 因此用工厂方法模式

from abc import ABCMeta, abstractmethod

from simple_factory1 import (
    Payment,
    Alipay,
    WeChatPay
    )

# 增加一个支付手段
class UnionPay(Payment):
    def pay(self,money):
        print(f"银联支付{money}元")

# 定义一个工厂接口，具体由具体的产品工厂去实现
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()
    
class WechatFactory(PaymentFactory):
    def create_payment(self):
        return WeChatPay()
    
class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)

# 要增加新的支付手段，就加一种工厂（缺点）
class UnionPayFactory(PaymentFactory):
    def create_payment(self):
        return UnionPay()
    
if __name__ == "__main__":
    # 先由具体的产品工厂拿到具体产品工厂实例
    real_pf = WechatFactory()
    # 具体工厂实例生产出具体产品的实例
    real_p = real_pf.create_payment()
    # 具体产品实例付款
    real_p.pay(18.8)

    # 先由具体的产品工厂拿到具体产品工厂实例
    real_pf = UnionPayFactory()
    # 具体工厂实例生产出具体产品的实例
    real_p = real_pf.create_payment()
    # 具体产品实例付款
    real_p.pay(18.8)

