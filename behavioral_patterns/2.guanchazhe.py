#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


# 观察者模式应用比较广泛，又被称为“发布-订阅”模式
# 它用来定义对象间一种一对多的依赖关系，当一个对象的状态发生变化时，所有依赖它的对象都得到通知并被自动更新

from abc import ABCMeta, abstractmethod

# 抽象的订阅者
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice_ins):
        pass

# 抽象的发布者：可以是接口，但子类不需要实现，因此不需要定义抽象方法
class Notice:
    def __init__(self):
        self.observers = []

    def attach(self, obs_ins):
        self.observers.append(obs_ins)
    
    def detach(self, obs_ins):
        self.observers.remove(obs_ins)

    def notify(self):
        for obs in self.observers:
            obs.update(self)

# 具体的发布者
class StaffNotice(Notice):
    def __init__(self, company_msg):
        super().__init__()# 这里要调用父类的初始化方法获得observers属性
        # 定义一个私有化属性
        self.__company_msg = company_msg

    # 将私有属性通过装饰器的属性返回出去
    @property
    def company_msg(self):
        return self.__company_msg
    
    # 有了装饰器的这种属性company_msg，就可以用它的setter装饰器
    @company_msg.setter
    def company_msg(self, info):
        self.__company_msg = info
        # 其实这种setter形式来赋值，只是为了顺便把下面这一句推送执行了
        self.notify()

from abc import ABCMeta, abstractmethod

# 具体的订阅者
class Staff(Observer):
    def __init__(self):
        self.company_msg = None

    def update(self, notice_ins):
        self.company_msg = notice_ins.company_msg

if __name__ == "__main__":
    staff_notice = StaffNotice('初始化公司信息')
    # 初始的职员对象，还没有消息
    staff1 = Staff()
    staff2 = Staff()
    # 订阅，增员
    staff_notice.attach(staff1)
    staff_notice.attach(staff2)
    # 为了要推送，就要setter，sertter的时候，一方面更新消息，一方面推送消息
    staff_notice.company_msg = '放假！'
    print(staff1.company_msg,"staff1")
    print(staff2.company_msg,"staff2")
    # 解绑2
    staff_notice.detach(staff2)
    # 再次更新setter
    staff_notice.company_msg = '开会！'
    print(staff1.company_msg,"staff1")
    print(staff2.company_msg,"staff2")

    '''结果
    放假！ staff1
    放假！ staff2
    开会！ staff1
    放假！ staff2
    '''