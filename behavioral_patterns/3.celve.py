#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


# 策略模式定义一个个算法，把它们封装起来，并且使它们可以相互替换
# 策略模式使得算法可独立于使用它的客户而变化


# 一个根据不同时间执行不同策略的例子

from abc import abstractmethod, ABCMeta
from datetime import datetime

# 抽象策略
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass

# 具体策略
class FastStrategy(Strategy):
    def execute(self, data):
        print("使用较快的策略处理%s" % data)

# 具体策略
class SlowStrategy(Strategy):
    def execute(self, data):
        print("使用较慢的策略处理%s" % data)

# 只定义了两种可以用来切换的类，并把这些具体的类的使用方法封装起来，客户端只需要知道什么时候用什么策略就行

# 上下文类，其实就是封装了策略和数据，客户端部分只需要知道要用什么策略和处理什么数据
# 然后将需要用的策略和数据传进上下文类即可，也就是说客户端需要判断用什么策略，而上下文类本身不做判断
class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy
        # 可以定义用户不知道的东西，客户端不需要知道上下文类拿到策略和数据后要做什么
        # 例如我需要当前时间做些什么事情，但客户端完全不知道这件事
        self.date = datetime.now()

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)

if __name__ == "__main__":
    data = "Hello!"
    # 使用较快的策略处理
    fast_strategy = FastStrategy()
    context = Context(fast_strategy, data)
    context.do_strategy()
    # 使用较慢的策略处理
    slow_strategy = SlowStrategy()
    context = Context(slow_strategy, data)
    context.do_strategy()

    '''
    优点：定义了一系列可重用的算法和行为；消除了一些条件语句；可以提供相同行为的不同实现；
    缺点：客户必须了解不同的策略
    '''