#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/2/26 13:45
# @file: 6.py


def decorator(func):
    print("into decorator")
    f = 12

    def adsd(k):
        k += 1

    return lambda *args, **kwargs: [print("start"),
                                    adsd(f),
                                    func(*args, **kwargs),
                                    print(func.__name__),
                                    print("end"),
                                    ][-3]


def decorator2(func):
    print("into decorator")
    return lambda *args, **kwargs: {"a": print("start"),
                                    "b": func(*args, **kwargs),
                                    "c": print(func.__name__),
                                    "d": print("end"),
                                    }["b"]


def k(func):
    print("into k")
    return lambda *args, **kwargs: func(*args, **kwargs)


# @decorator(k)  # z = decorator(k)(z)
@decorator2
def z(n):
    print(n)
    return 99


if __name__ == '__main__':
    # p = z(5)
    # print(p)
    # pass
    a = {"a": print("1"),
         "d": print("2"),
         }
