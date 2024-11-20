#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


from leishipeiqi1 import Payment, Alipay, BankPay

# 多了一个待适配的类
class ApplePay():
    def cost(self, money):
        print(f"苹果支付{money}")

class PaymentAdapterCost2Pay(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)

if __name__ == "__main__":
    bp = PaymentAdapterCost2Pay(BankPay())
    alip = Alipay()
    ap = PaymentAdapterCost2Pay(ApplePay())
    bp.pay(10)
    alip.pay(20)
    ap.pay(30)