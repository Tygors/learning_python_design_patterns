#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


# 与普通工厂和工厂方法不同
# 抽象工厂类的接口让工厂子类创建一系列相关或相互依赖的对象
# 抽象工厂模式中的每一个具体工厂都生产一套产品

from abc import ABCMeta, abstractmethod

# 假设一个最终的产品需要三个组件
# 每个组件都有不同的型号或品牌
# 先按每个组件都是产品进行定义抽象的接口

# ------抽象的产品------
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass

class PhoneCPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class PhoneOS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass

# 按组件产品的接口生产具体的产品
# ------具体的产品------
class SmallShell(PhoneShell):
    def show_shell(self):
        print('普通手机小手机壳')

class BigShell(PhoneShell):
    def show_shell(self):
        print('普通手机大手机壳')

class AppleShell(PhoneShell):
    def show_shell(self):
        print('苹果手机壳')

class SnapDragonCPU(PhoneCPU):
    def show_cpu(self):
        print('骁龙CPU')

class HuaweiCPU(PhoneCPU):
    def show_cpu(self):
        print('华为CPU')

class AppleCPU(PhoneCPU):
    def show_cpu(self):
        print('苹果CPU')

class AndroidOS(PhoneOS):
    def show_os(self):
        print('IOS系统')

class AppleOS(PhoneOS):
    def show_os(self):
        print('安卓系统')


# 由于抽象工厂模式中的每一个具体工厂都生产一套产品
# 先定义出工厂的接口，工厂定义出所需要生产的组件
# ------抽象的工厂------
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass

# 开始建厂，具体的厂会按具体生产的组件返回组件的对象
# ------具体的工厂------
class HuaweiFactory(PhoneFactory):
    def make_shell(self):
        return SmallShell()

    def make_cpu(self):
        return HuaweiCPU()

    def make_os(self):
        return AndroidOS()

class AppleFactory(PhoneFactory):
    def make_shell(self):
        return AppleShell()

    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return AppleOS()
    
# 开始真正生产
# 客户端
class Phone:
    def __init__(self, shell, cpu, os):
        self.shell = shell
        self.cpu = cpu
        self.os = os

    def show_info(self):
        print("手机信息如下：")
        self.shell.show_shell()
        self.cpu.show_cpu()
        self.os.show_os()

def make_phone(factory):
    shell = factory.make_shell()
    cpu = factory.make_cpu()
    os = factory.make_os()
    return Phone(shell, cpu, os)

if __name__ == "__main__":
    # 想要华为手机
    # 先建华为的厂
    pf = HuaweiFactory()
    # 开始生产手机
    # makephone方法拿到了华为的厂
    # 首先会用该厂，生产出具体的手机壳、cpu和操作系统
    # 把具体的三个组件给到Phone类进行组装
    p = make_phone(pf)
    # 组装完后，就可以看看手机啥配置了
    p.show_info()
    # 缺点是难以支持新种类的抽象产品，例如如果制作手机的组件增加了，那么几乎所有类都要改