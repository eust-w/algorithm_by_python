#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/2/20 16:19
# @file: method_by_new.py
import sys


# class SingleTon(object):
#     _instance = None
#
#     def __new__(cls, *args, **kwagrs):
#         # print(cls)
#         if not cls._instance:
#             cls._instance = super(SingleTon, cls).__new__(cls, *args, **kwagrs)
#         # print(cls)
#         # print(cls._instance)
#         return cls._instance


class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        cls._instance = super(SingleTon, cls).__new__(cls, *args, **kwagrs)


# A = SingleTon()

print(sys.getrefcount(SingleTon))
# B = SingleTon()
# C = SingleTon
# D = SingleTon
# print(SingleTon())
# print(SingleTon())
# print(C)
# print(D)
# print(C())
# print(D())
# print(A.__str__())
# print(id(A))
# print(B)
# print(id(B))


# class MyClass(SingleTon):
#     class_val = 22
#
#     def __init__(self, val):
#         self.val = val
#
#     def obj_fun(self):
#         print(self.val, 'obj_fun')
#
#     @staticmethod
#     def static_fun():
#         print('static_fun')
#
#     @classmethod
#     def class_fun(cls):
#         print(cls.class_val)
#
#
# if __name__ == '__main__':
#     a = MyClass(1)
#     b = MyClass(2)
#     print(a is b)
#     print(id(a), id(b))
#     # 类型验证
#     print(type(a))
#     print(type(b))
