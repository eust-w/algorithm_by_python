#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/4/12 17:15
# @file: hash_search.py

"""
条件：先创建哈希表（散列表）

原理：根据键值方式(Key Value)进行查找，通过散列函数，定位数据元素。

时间复杂度：几乎是O(1)，取决于产生冲突的多少。
"""


class Hash:
    def __init__(self, array: list):
        self.__maps = {}
        for index, value in enumerate(array):
            if value in self.__maps:
                self.__maps[value].append(index)
            else:
                self.__maps[value] = [index]

    def get(self, va: int) -> list:
        return self.__maps[va]


if __name__ == '__main__':
    import random
    a = list(random.randint(1, 20000) for _ in range(200))
    h = Hash(a)
    for t in a:
        assert a[h.get(t)[0]] == t
