#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/4/13 13:22
# @file: 1.py

class Search:
    def __init__(self, array: list, target: int):
        self.array = array
        self.target = target

    @property
    def sequence(self):
        array = self.array
        target = self.target
        for index, value in enumerate(array):
            if value == target:
                return index
        else:
            return -1

    @property
    def binary_loop(self):
        array = self.array
        target = self.target
        left = 0
        right = len(array) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            mid_value = array[mid]
            if mid_value < target:
                left = mid
            elif mid_value > target:
                right = mid
            else:
                return mid
        return -1

    @property
    def binary_recursion(self):
        def inner(array, target, left, right):
            if left >= right:
                return -1
            mid = (left + right) // 2 + 1
            mid_value = array[mid]
            if mid_value > target:
                right = mid
            elif mid_value < target:
                left = mid
            else:
                return mid
            return inner(array, target, left, right)

        return inner(self.array, self.target, 0, len(self.array) - 1)

    @property
    def interpolation(self):
        def inner(array, target, left, right):
            if left >= right:
                return -1
            mid = int(left + (target-array[left]) / (array[right] - array[left]) * (right - left))
            mid_value = array[mid]
            if mid_value > target:
                right = mid - 1
            elif mid_value < target:
                left = mid + 1
            else:
                return mid
            return inner(array, target, left, right)

        return inner(self.array, self.target, 0, len(self.array) - 1)

    @property
    def fibonacci(self):
        array = self.array
        target = self.target
        fib1 = 0
        fib2 = 1
        fib3 = 1
        left = 0

        def anti_fib(times):
            nonlocal fib1, fib2, fib3
            for _ in range(times):
                fib3 = fib2
                fib2 = fib1
                fib1 = fib3 - fib2
        while fib3 < len(array) - 1:
            fib1 = fib2
            fib2 = fib3
            fib3 = fib1 + fib2
        while fib3 > 1:
            mid = left + fib1
            print("mid", mid)
            mid_value = array[mid]

            if mid_value > target:
                anti_fib(2)
            elif mid_value < target:
                left = mid
                anti_fib(1)
            else:
                return mid
        return -1

    @property
    def block(self):
        array = self.array
        target = self.target
        right = left = 0
        gap = 20
        while right < len(array)-1:
            right_value = array[right]
            if right_value == target:
                return right
            elif right_value > target:
                break
            left = right
            right += gap
        else:
            right = len(array)-1
        for index, value in enumerate(array[left:right+1]):
            if value == target:
                return index + left
        else:
            return -1


if __name__ == '__main__':
    a = sorted(
        [2, 3, 4, 23212, 32432, 432, 342, 34, 43, 423, 5454, 543, 7, 543, 435, 35, 4353, 4435, 345, 345, 34354, 5,
         43543, 3, 2, 32, 23, 2, 3, 4, 4, 5, 6, 7, 8, 7, 5, 200, 7654321])
    t = 7654321
    # print("len", len(a))

    s = Search(a, t)
    print(s.binary_loop)
    print(s.binary_recursion)
    print(s.interpolation)
    print(s.block)
    assert a[s.sequence] == t
    assert s.sequence == s.binary_loop == s.binary_recursion == s.interpolation == s.fibonacci == s.block
