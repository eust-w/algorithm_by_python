#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/2/26 15:39
# @file: 9.py

# from e import a


# a = 21


# def b():
#     # a = 11
#
#     def c():
#         def d():
#             global a
#             # a = 85
#             print(a)
#             print(id(a))
#             # del a
#             # nonlocal a
#             a += 1
#             return a
#
#         return d()
#
#     return c()


from e import a
import time


# a =12

def z():
    a = 29

    def g_a():
        global a
        b = a
        return b

    def p():
        # nonlocal a
        print(g_a(), a)

    # def p():
    #     # global a
    #     # nonlocal a
    #     print(a)
    #     time.sleep(6)
    #     nonlocal b
    #     # global a
    #     print(b)

    # def p():
    #     # global a
    #     nonlocal a
    #     b = a
    #     a = 89
    #     print(a, b)

    return p


z()()
