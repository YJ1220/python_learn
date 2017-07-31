#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#最基本的类使用

# __call__ 类的特殊函数，将类变成可调用的，初始化后，可以直接调用

class Person():
    def __init__(self,name):
        self.name = name

    def __call__(self, res):
        print(self.name)
        print(res)

    def printname(self):
        print(self.name)

    def color(self,color):
        self.color=color
        print(self.color)


if __name__ == '__main__':
    a = Person('hello')
    # __call__ 调用
    a('world')