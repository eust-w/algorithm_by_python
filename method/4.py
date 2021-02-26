#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/2/24 16:33
# @file: 4.py

class C: count = 100


class A: count = 900


class D: count = 400


class E: count = 20


class C1(C, D, E): pass


# class A1(A, E):
#     A1 = 3
#     def __new__(cls, *args, **kwargs):
#         cls.count = A.count + E.count

class A1(type, A, E):
    count = 3

    def __new__(cls, name, bases, attrs):
        cls.count = A.count + E.count
        attrs['cal_price'] = lambda self: self.price * self._discount
        return type.__new__(cls, name, bases, attrs)


# class B(A1, C1):
class B(metaclass=A1):
    def __init__(self):
        # A.count += 1
        B.count += 1


if __name__ == '__main__':
    B1 = B()
    B2 = B()
    print(A.count)
    print(B.count)
    print(B.mro())
    print(type(B.__bases__))
    print(type(A1.__bases__))
