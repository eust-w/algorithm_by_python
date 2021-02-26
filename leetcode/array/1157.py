#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/2/23 10:15
# @file: 1157.py
"""
实现一个 MajorityChecker 的类，它应该具有下述几个 API：

MajorityChecker(int[] arr) 会用给定的数组 arr 来构造一个 MajorityChecker 的实例。
int query(int left, int right, int threshold) 有这么几个参数：
0 <= left <= right < arr.length 表示数组 arr 的子数组的长度。
2 * threshold > right - left + 1，也就是说阈值 threshold 始终比子序列长度的一半还要大。
每次查询 query(...) 会返回在 arr[left], arr[left+1], ..., arr[right] 中至少出现阈值次数 threshold 的元素，如果不存在这样的元素，就返回 -1。



示例：

MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // 返回 1
majorityChecker.query(0,3,3); // 返回 -1
majorityChecker.query(2,3,2); // 返回 2
"""

from typing import List


class MajorityChecker:
    def __init__(self, array: List[int]):
        self.array = array

    def query(self, left: int, right: int, threshold: int) -> int:
        print(self.array)
