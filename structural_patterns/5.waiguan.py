#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


# 外观模式下的角色有外观和子系统类
# 优点是：减少系统相互依赖，提高灵活性，提高了安全性。

# 子系统类
class CPU:
    def run(self):
        print('CPU start to run...')

    def stop(self):
        print('CPU stops...')

# 子系统类
class Disk:
    def run(self):
        print('Disk start to run...')

    def stop(self):
        print('Disk stops...')

# 子系统类
class Memory:
    def run(self):
        print('Memory start to run...')

    def stop(self):
        print('Memory stops...')

# 为子系统的一组接口定义一个高层的接口
# 外观
class Computer():
    def __init__(self):
        self.CPU = CPU()
        self.Disc = Disk()
        self.Member = Memory()

    def run(self):
        self.CPU.run()
        self.Disc.run()
        self.Member.run()

    def stop(self):
        self.Member.stop()
        self.Disc.stop()
        self.CPU.stop()

if __name__ == "__main__":
    # 客户端，高层代码
    c = Computer()
    c.run()
    c.stop()