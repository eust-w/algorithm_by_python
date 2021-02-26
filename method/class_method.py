#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/2/22 14:32
# @file: class_method.py
import sys


class Sample:
    # num = 0
    #
    # def __init__(self):
    #     Sample.num += 1
    #
    # @staticmethod
    # def print_yes(self):
    #     return 'yes'
    #
    # @classmethod
    # def class_num(cls):
    #     return cls.num
    #
    # # def __del__(self):
    # #     Sample.num -= 1
    pass


# class A:
#     def __new__(cls, *args, **kwargs):
#         pass
B = type('B', (), {})
C = type('C', (), {})
#
A = type('A', (B, C,), {})
# A = type('A', (B,), {})
# A = type('A', (), {})

for _ in dir(A):
    q = eval('A.{}'.format(_))
    print(_+':', end='')
    print(q)
# print(dir(A))
# print(A.__class__)
print(A.__dict__)
print(sys.getrefcount(A)) # 5
print(sys.getrefcount(B))
print(sys.getrefcount(C))

# s_1 = Sample()
# s_2 = Sample()
#
# print(s_1.class_num())
#
# s_3 = Sample()
# print(s_1.class_num())
# s_3 = Sample()
# print(s_1.class_num())
#
# print(sys.getrefcount(Sample))
