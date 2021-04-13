#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/4/12 15:03
# @file: interpolation_search.py
"""
mid=(low+high)/2, 即mid=low+1/2*(high-low);
　　通过类比，我们可以将查找的点改进为如下：
　　mid=low+(key-a[low])/(a[high]-a[low])*(high-low)，
基本思想：基于二分查找算法，将查找点的选择改进为自适应选择，可以提高查找效率。当然，差值查找也属于有序查找。
　　注：对于表长较大，而关键字分布又比较均匀的查找表来说，插值查找算法的平均性能比折半查找要好的多。反之，数组中如果分布非常不均匀，那么插值查找未必是很合适的选择。
　　复杂度分析：查找成功或者失败的时间复杂度均为O(log2(log2n))。
"""


def interpolation_search(array: list, target: int) -> int:
    def inner(i_a: list, i_t: int, left: int, right: int) -> int:
        if left >= right:
            return -1
        mid = int(left + (target - array[left]) / (array[right] - array[left]) * (right - left))
        mid_value = array[mid]
        if mid_value == target:
            return mid
        if mid_value < target:
            if left == mid:
                left += 1
            else:
                left = mid
        else:
            if right == mid:
                right += 1
            else:
                right = mid
        return inner(i_a, i_t, left, right)

    return inner(array, target, 0, len(array) - 1)


if __name__ == '__main__':
    a = sorted([3, 34, 56, 8, 5, 6, 9, 2, 3, 83974927, 1, 2, 3, 54])
    import random
    a = sorted(list(random.randint(1, 20000) for _ in range(200)))
    for t in a:
        assert a[interpolation_search(a, t)] == t
