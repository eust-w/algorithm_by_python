#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/4/12 13:49
# @file: binary_search.py
"""
条件：有序数组

原理：查找过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜素过程结束； 如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元
素的那一半中查找，而且跟开始一样从中间元素开始比较。 如果在某一步骤数组为空，则代表找不到。 这种搜索算法每一次比较都使搜索范围缩小一半。

时间复杂度：O(logn)
复杂度分析：最坏情况下，关键词比较次数为log2(n+1)，且期望时间复杂度为O(log2n)；
注：折半查找的前提条件是需要有序表顺序存储，对于静态查找表，一次排序后不再变化，折半查找能得到不错的效率。但对于需要频繁执行插入或删除操作的数
据集来说，维护有序的排序会带来不小的工作量，那就不建议使用
"""


def binary_search_if(array: list, target: int) -> int:
    low = 0
    height = len(array) - 1
    while low < height:
        mid = int((low + height) / 2)
        mid_value = array[mid]
        if mid_value == target:
            return mid
        if mid_value < target:
            low = mid
        else:
            height = mid
    return -1


def binary_search_recursive(a1: list, t1: int) -> int:
    def inner(array: list, target: int, left: int, right: int) -> int:
        if left >= right:
            return -2
        mid = int((left+right)/2)
        mid_value = array[mid]
        if mid_value == target:
            return mid
        if mid_value < target:
            left = mid
        else:
            right = mid
        return inner(array, target, left, right)
    return inner(a1, t1, 0, len(a1)-1)


if __name__ == '__main__':
    a_unsorted = [2, 343, 4, 54, 54, 32445, 345, 4, 543, 9, 543, 5435, 43543543, 2343, 432, 43, 6, 8, 8, 5, 78, 90]
    a = sorted(a_unsorted)
    t = 5
    assert a[binary_search_if(a, t)] == t
    # print(binary_search_if(a, t))
    assert a[binary_search_recursive(a, t)] == t
