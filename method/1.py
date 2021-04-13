#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/4/12 19:40
# @file: 1.py

class As:
    def __init__(self, p):
        self.p = p

    def show(self):
        return self.p

    @property
    def shos(self):
        return self.p

    @shos.setter
    def shos(self, value):
        self.p = value


if __name__ == '__main__':
    A = As(11)
    print(A.shos)
    A.shos = 12
    print(A.shos)
