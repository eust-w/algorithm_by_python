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
    a = sorted(
        [2, 34, 435, 324, 34, 6, 54, 7, 43, 2, 9768, 34, 34, 43, 324, 452, 65, 4, 6, 32, 6, 4543, 3443, 32, 6557, 3434,
         453, 34, 8, 43, 21, 6, 4, 763, 342, 4, 5, 7, 34, 57, 43, 76, 5, 4, 33, 2, 4])
    t = 7
    h = Hash(a)
    print(a)
    print(h.get(t))
