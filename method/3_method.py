#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/2/24 16:24
# @file: 3_method.py

class Classes:
    num = None

    def __init__(self, b):
        self.b = b

    @classmethod
    def ins_num(cls):
        print(cls.num)

    @staticmethod
    def fun(name):
        print("hello", name)

    def a(self):
        print(self.b)

    def p(self):
        print(12)

if __name__ == '__main__':
    A = Classes(12)
    A.ins_num()
