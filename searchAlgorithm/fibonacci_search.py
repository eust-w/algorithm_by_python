#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/4/12 15:39
# @file: fibonacci_search.py
"""
也是二分查找的一种提升算法，通过运用黄金比例的概念在数列中选择查找点进行查找，提高查找效率。同样地，斐波那契查找也属于一种有序查找算法。
mid=low+F(k-1)-1
low=mid+1,k-=2
high=mid-1,k-=1
"""


def fibonacci_search(array: list, target: int) -> int:
    def anti_fib(n):
        nonlocal fib2, fib1, fib3
        for _ in range(n):
            fib3 = fib2
            fib2 = fib1
            fib1 = fib3 - fib2
    fib1 = 0
    fib2 = 1
    fib3 = fib2 + fib1
    while fib3 < len(array) - 1:
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib2
    left = -1
    while fib3 > 1:
        mid = min(left + fib1, len(array) - 1)
        mid_value = array[mid]
        if mid_value == target:
            return mid
        if mid_value < target:
            left = mid
            anti_fib(1)
        else:
            anti_fib(2)
    return -1


if __name__ == '__main__':
    import random
    a = sorted(list(random.randint(1, 20000) for _ in range(500000)))
    for t in a:
        assert a[fibonacci_search(a, t)] == t
