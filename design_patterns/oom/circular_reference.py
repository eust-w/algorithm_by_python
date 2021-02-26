#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/2/20 17:36
# @file: circular_reference.py
import sys
import time
import threading


class Person(object):
    free_lock = threading.Condition()

    def __init__(self, name: str = ""):
        """
        Parameters
        ----------
        name: str
        姓名
        best_friend: str
        最要好的朋友名
        """

        self._name = name
        self._best_friend = None

    @property
    def best_friend(self, person: "Person"):
        return self._best_friend

    @best_friend.setter
    def best_friend(self, friend: "Person"):
        self._best_friend = friend

    def __str__(self):
        """
        """
        return self._name

    def __del__(self):
        """
        """
        self.free_lock.acquire()
        print(f"{self._name} 要 GG 了，现在释放它的内存空间。")
        sys.stderr.flush()
        self.free_lock.release()


def mem_leak():
    """
    循环引用导致内存泄漏
    """


zhang_san = Person(name='张三')
li_si = Person("李四")

# 构造出循环引用
# 李四的好友是张三
li_si.best_friend = zhang_san
# 张三的好友是李四
zhang_san.best_friend = li_si

if __name__ == "__main__":
    for i in range(3):
        time.sleep(0.01)
print(f"{i}")
mem_leak()

print("mem_leak 执行完成了.")
time.sleep(5)
