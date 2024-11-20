#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei == True:
            print(f"huabei支付{money}元")
        else:
            print(f"zhifubao支付{money}元")


class WeChatPay(Payment):
    def pay(self, money):
        print(f"微信支付{money}元")


# 真正的工厂类

class PaymentFactory:
    def create_payment(self, method):
        if method == "alipay":
            return Alipay()
        elif method == "wechatpay":
            return WeChatPay()
        elif method == "huabeipay":
            return Alipay(
                use_huabei=True 
            )
        else:
            raise TypeError(f"no {method} class")

if __name__ == "__main__":        
    # 一、先拿到工厂类对象
    pf = PaymentFactory()

    # 二、调用工厂类对象的创建具体产品方法
    real_p = pf.create_payment("huabeipay")

    # 三、利用具体产品实例进行付款
    real_p.pay(18.8)