#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/2/24 17:23
# @file: 5.py


class A:
    count = 0


class B:
    num = 0

    def __init__(self):
        B.num += 1


if __name__ == '__main__':
    B1 = B()
    B2 = B()
    B3 = B()
    B4 = B()
    print(B.num)
    print(B1.num)
