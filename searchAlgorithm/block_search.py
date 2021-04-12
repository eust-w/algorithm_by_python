#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/4/12 16:19
# @file: block_search.py
"""
要求是顺序表，分块查找又称索引顺序查找，它是顺序查找的一种改进方法。
将n个数据元素"按块有序"划分为m块（m ≤ n）。
每一块中的结点不必有序，但块与块之间必须"按块有序"；
即第1块中任一元素的关键字都必须小于第2块中任一元素的关键字；
而第2块中任一元素又都必须小于第3块中的任一元素，
1、先选取各块中的最大关键字构成一个索引表；
2、查找分两个部分：先对索引表进行二分查找或顺序查找，以确定待查记录在哪一块中；
3、在已确定的块中用顺序法进行查找。
时间复杂度：O(log(m)+N/m)
"""


def block_search(array: list, target: int, m: int) -> int:
    if len(array) == 0:
        return -1
    if array[0] == target:
        return 0
    gap = (len(array) - 1) // m
    remainder = (len(array) - 1) % m
    left = 0
    right = left + gap + remainder
    for _ in range(m):
        if target == array[right]:
            return right
        if target < array[right]:
            break
        left = right
        right = left + gap
    else:
        return -1
    for i in range(left, right):
        if array[i] == target:
            return i
    else:
        return -1


if __name__ == '__main__':
    a = sorted(
        [2, 34, 56, 4, 5, 8, 7, 6, 34, 656, 45, 7, 324, 657, 342, 65, 675, 432, 546, 3425, 8765, 342, 765, 342, 654,
         234, 435342, 532434, 54, 67, 34, 8, 4324, 3426, 56, 45, 87, 234, 43, 546, 76, 342, 432, 5674])
    t = 87
    assert a[block_search(a, t, 7)] == t
