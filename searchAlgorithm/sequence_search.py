#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/4/12 13:39
# @file: sequence_search.py
"""
条件：无序或有序队列。
原理：按顺序比较每个元素，直到找到关键字为止。
时间复杂度：O(n)
查找成功时的平均查找长度为：（假设每个数据元素的概率相等） ASL = 1/n(1+2+3+…+n) = (n+1)/2 ;
当查找不成功时，需要n+1次比较，时间复杂度为O(n);
所以，顺序查找的时间复杂度为O(n)。
"""


def int_sequence_search(array: list, target: int) -> int:
    for index in range(len(array) - 1):
        if array[index] == target:
            return index
    else:
        return -1


if __name__ == '__main__':
    a = [324, 76, 34, 3, 42, 3, 4, 24, 23, 23, 43, 53, 5423, 87, 432, 4, 2, 4, 23, 4]
    t = 2
    print(int_sequence_search(array=a, target=t))
