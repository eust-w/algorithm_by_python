#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/4/14 17:13
# @file: grid.py


"""
you can set value as a function and anti-dimensional as input para class and dimensional as out put para class,
then we get a whole tied project
"""


class Node:
    dimensional_num = 0

    def __init__(self, value=None):
        self.__setattr__("value", value)
        for _index in range(Node.dimensional_num):
            self.__setattr__("D{}".format(_index + 1), None)
            self.__setattr__("RD{}".format(_index + 1), None)

    def stack(self, *args):
        _dimensional_list = args
        if len(_dimensional_list) > Node.dimensional_num:
            return "dimensional disruption"
        _node_pointer = self
        for _index, _dim in enumerate(_dimensional_list):
            if _dim % 1 != 0:
                return "space crack in {}".format(_dim)
            if _dim > 0:
                _dim_name = "D{}".format(_index + 1)
                for _ in range(_dim):
                    _node_pointer = _node_pointer.__getattribute__(_dim_name)
            if _dim < 0:
                _dim_name = "RD{}".format(_index + 1)
                for _ in range(-_dim):
                    _node_pointer = _node_pointer.__getattribute__(_dim_name)
        return _node_pointer

    @property
    def dim_num(self):
        return Node.dimensional_num

    @dim_num.setter
    def dim_num(self, value):
        pass

    def __setattr__(self, key, value, flag=True):
        self.__dict__[key] = value
        if key == "dim_num":
            Node.dimensional_num = value
        key_list = key.split("D")
        if len(key_list) != 2 or not self.is_number(key_list[1]):
            return
        if type(value) != Node or not flag:
            return
        if not hasattr(value, key):
            value.__setattr__(key, None, flag=False)
        if key_list[0] == "R":
            value.__setattr__(key[1:], self, flag=False)
        if key_list[0] == "":
            value.__setattr__("R"+key, self, flag=False)

    @staticmethod
    def is_number(s):
        try:
            if s[0] in ["0", "-", " "]:
                return False
                # raise ValueError
            return int(s)
        except ValueError:
            return False

    def __check(self):
        for index in range(1, Node.dimensional_num+1):
            key = "RD"+str(index)
            if not hasattr(self, key[1:]):
                self.__setattr__(key[1:], None)
            if not hasattr(self, key):
                self.__setattr__(key, None)

    def __getattr__(self, key):
        key_list = key.split("D")
        if len(key_list) != 2:
            return "can not find this parameter"
        key_num = self.is_number(key_list[1])
        if not key_num:
            return "can not find this parameter"
        if key_num > Node.dimensional_num:
            return "{} has out of scope, the Largest dimension is {}.".format(key_num, Node.dimensional_num)
        if key_list[0] == "R" or "":
            self.__setattr__(key, None)
            return None


if __name__ == '__main__':
    def node_value_add(self_node):
        return self_node.stack(1).value + self_node.stack(-2).value + self_node.stack(0, 1).value
    Node.dimensional_num = 3
    a, b, c, d, aa, bb, cc, dd = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8)
    d.RD1 = c
    c.RD1 = b
    a.D1 = b
    c.D2 = cc
    c.value = node_value_add(c)
    d.D2 = dd
    # print(c.value)
    # print(c.dimensional_num)
    Node.dimensional_num = 5
    c.dim_num = 6
    # print(c.dim_num)
    # print(a.dim_num)
    # print(c.__check())
    # print(a.__check())
    print(b.RD2)
    print(a.stack(3, 1).RD8)
    print(a.stack(3, 1).D5)
    print(a.stack(3, 1).value)
