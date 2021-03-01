#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/2/22 10:40
# @file: sheng_cheng_qi.py
"""
在 Python 中，使用了 yield 的函数被称为生成器（generator）。

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

调用一个生成器函数，返回的是一个迭代器对象。
"""

import sys


# def fibonacci_generator():  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while 1:
#         a, b, counter = b, a+b, counter+1
#         yield a
#
#
# def fibonacci_print(n):
#     f_g_1 = fibonacci_generator()
#     for _ in range(n):
#         print(_+1, next(f_g_1))
#
#
# def static(initial_value, func):
#     n = initial_value
#     while 1:
#         n = func(n)
#         k = yield n
#         print(k)
#
#
# def self_add(initial_int):
#     return initial_int + 1
#
#
# if __name__ == '__main__':
#     fibonacci_print(10)
#     print('*'*10)
#     static_1 = static(2, self_add)
#     static_1.send(None)
#     for _ in range(12):
#         print(static_1.send('12'))
#     static_1.close()

class A:
    instance_count = 0

    def __init__(self, count):
        self.count = count
        A.instance_count += 1

    # @staticmethod
    # def fibonacci(p):
    #     _a, _b, _count = 0, 1, p
    #     _out_list = []
    #     while _count:
    #         _a, _b, _count = _b, _a+_b, _count-1
    #         _out_list.append(_a)
    #     return _out_list

    def fibonacci(self):
        _a, _b, _count = 0, 1, self.count
        _out_list = []
        while _count:
            _a, _b, _count = _b, _a+_b, _count-1
            _out_list.append(_a)
        return _out_list

    # @classmethod
    # def fibonacci(cls):
    #     _a, _b, _count = 0, 1, cls.instance_count
    #     _out_list = []
    #     while _count:
    #         _a, _b, _count = _b, _a+_b, _count-1
    #         _out_list.append(_a)
    #     return _out_list

    # @staticmethod
    # def fibonacci(p):
    #     _a, _b, _count = 0, 1, p
    #     _out_list = []
    #     while _count:
    #         _a, _b, _count = _b, _a+_b, _count-1
    #         _out_list.append(_a)
    #     return _out_list


if __name__ == '__main__':
    C = A(5)
    D = A(12)
    C.instance_count = 500
    C.__delattr__("instance_count")
    A.instance_count = 12
    print(C.instance_count)
    print(D.instance_count)
    print(C.fibonacci())
    print(C.fibonacci(19))
