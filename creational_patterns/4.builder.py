#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create in: 2021-04
"""


# 建造者模式是将一个复杂对象的构建与它的表示分离
# 使得同样的构建过程可以创建不同的表示

# 建造者模式着重一步步构造一个复杂对象（控制顺序）
# 而抽象工厂模式着重于多个系列的产品抽象

from abc import ABCMeta, abstractmethod

# 产品
class Player:
    def __init__(self, face=None, body=None, arms=None, legs=None):
        self.face = face
        self.body = body
        self.arms = arms
        self.legs = legs

    # 打印对象时，显示的内容，在__str__方法写
    def __str__(self):
        return f"{self.face}{self.body}{self.arms}{self.legs}"
    

# 抽象建造者
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arms(self):
        pass

    @abstractmethod
    def build_legs(self):
        pass

# 具体建造者，隐藏了产品了内部结构，只管创建出有哪些结构
# 剩下的要交给指挥者去装配，即控制结构顺序
class GirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()
    # 无需指定各个部分的顺序，只是表示出来
    def build_arms(self):
        self.player.arms = "女孩手臂"

    def build_body(self):
        self.player.body = "女孩身体"

    def build_face(self):
        self.player.face = "女孩脸蛋儿"

    def build_legs(self):
        self.player.legs = "女孩的腿"

# 建造者，只是表示出来
class MonsterBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '绿脸'

    def build_body(self):
        self.player.body = '魁梧的身体'

    def build_arms(self):
        self.player.arms = '粗壮的胳膊'

    def build_legs(self):
        self.player.legs = '粗壮的大腿'

# 指挥者
# 真正在这里构造，构造与表示愤慨，可以对构造过程精细控制
class PlayerDirectory():
    def builder_player(self, builder):
        # 这里确定脸、身体、手臂、腿的顺序
        builder.build_face()
        builder.build_body()
        builder.build_arms()
        builder.build_legs()
        return builder.player
    
# 客户端
if __name__ == "__main__":
    builder = MonsterBuilder()
    director = PlayerDirectory()
    real_player = director.builder_player(builder)
    print(real_player)

    builder1 = GirlBuilder()
    girl_player = director.builder_player(builder1)
    print(girl_player)
