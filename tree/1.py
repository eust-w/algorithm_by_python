#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/4/12 19:10
# @file: 1.py

class Node:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

class SearchBinaryTree:
    """二叉树类"""
    def __init__(self):
        self.__root = None
        self.prefix_branch = "├"
        self.prefix_trunk = "|"
        self.prefix_leaf = '└'
        self.prefix_empty = ''
        self.prefix_left = '─L─'
        self.prefix_right = '─R─'

    def is_empty(self):
        return not self.__root

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, value):
        self.__root = value if isinstance(value, Node) else Node(value)

    def show_tree(self):
        if self.is_empty():
            print("empty binary tree")
            return
        print("-"*20)
        print(self.__root.data)
        self.__print_tree(self.__root)
        print("-"*20)

    def insert(self, root, value):
        node
