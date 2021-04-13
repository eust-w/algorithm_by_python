#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/3/1 20:33
# @file: 003.py


# def lengthOfLongestSubstring(self, s):
#     # https://leetcode.com/articles/longest-substring-without-repeating-characters/
#     charMap = {}
#     for i in range(256):
#         charMap[i] = -1
#     ls = len(s)
#     i = max_len = 0
#     for j in range(ls):
#         # Note that when charMap[ord(s[j])] >= i, it means that there are
#         # duplicate character in current i,j. So we need to update i.
#         if charMap[ord(s[j])] >= i:
#             i = charMap[ord(s[j])] + 1
#         charMap[ord(s[j])] = j
#         max_len = max(max_len, j - i + 1)
#     return max_len


def long(s):
    tem = []
    max_num = 0
    for count, _ in enumerate(s):
        tem.append(_)
        num = len(tem)
        for index in range(num):
            if _ == tem[index]:
                tem = tem[index+1:]
                max_num = max(max_num, num)
                break
    return max_num


print(long("aabsdsa"))

