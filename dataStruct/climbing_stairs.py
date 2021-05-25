#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/4/16 15:17
# @file: climbing_stairs.py

class Solution:
    def waysToStep(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 4
        # 本题用动态规划的思路解题，但是不需要n个数组空间，只需3个记录
        e1 = 1
        e2 = 2
        e3 = 4
        for i in range(4, n+1):
            e4 = (e1 + e2 + e3)%1000000007 # 注意！取模一定要在这里就算好，而不是放到最后一步
            e1 = e2
            e2 = e3
            e3 = e4
        return e3

def allMethods(stairs):
    '''
    :param stairs:the  numbers of stair
    :return:
    '''
    if isinstance(stairs,int) and stairs > 0:
        basic_num = {1:1,2:2,3:4}
        if stairs in basic_num.keys():
            return basic_num[stairs]
        else:
            return allMethods(stairs-1) + allMethods(stairs-2) + allMethods(stairs-3)
    else:
        print('the num of stair is wrong')
        return False

