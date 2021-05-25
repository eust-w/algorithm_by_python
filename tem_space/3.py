#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/4/13 15:17
# @file: 3.py

import time
import math


def func(k, n):
    kk = 1
    for _ in range(n):
        kk *= k
    return kk


def fib1(n):
    return int((((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n) / (5 ** 0.5))


def fib2(n):
    z = math.sqrt(5)
    return int((((1 + z) / 2) ** n - ((1 - z) / 2) ** n) / z)


if __name__ == '__main__':
    print(time.time())
    print(15 ** 5696)
    print(time.time())
    print(fib1(1099))
    for _ in range(500):
        fib1(1099)
    print(time.time())
    print(fib2(1099))
    for _ in range(500):
        fib2(1099)
    print(time.time())
    print(func(15, 5696))
    print(time.time())
