# -*- coding: utf-8 -*-

"""
Binary tree implementation, runs on python 3.6+ only
Created on 23/08/2020
@author: Anurag Gundappa
"""


class BinaryTree:

    def __init__(self, node):
        """
        Initialization
        :param node:
        """
        self.node = node
        self.left_child = None
        self.right_child = None

    def __str__(self):
        """
        Instance string representation for user
        :return:
        """
        return str(self.node)

    def __repr__(self):
        """
        Official instance representation
        :return:
        """
        return str(self.node)

    def add_left_child(self, node):
        """
        Add node to the left of tree
        If left node already exists, it adds the node and pushes existing nodes one level down in the tree
        :param node:
        :return:
        """

        if self.left_child is None:
            self.left_child = BinaryTree(node)

        else:
            t = BinaryTree(node)
            t.left_child = self.left_child
            self.left_child = t

    def add_right_child(self, node):
        """
        Add node to the right of tree
        If right node already exists, it adds the node and pushes existing nodes one level down in the tree
        :param node:
        :return:
        """

        if self.right_child is None:
            self.right_child = BinaryTree(node)

        else:
            t = BinaryTree(node)
            t.right_child = self.right_child
            self.right_child = t

    def set_rootnode(self, node):
        """
        Set the new root node
        :param node:
        :return:
        """
        self.node = node

    def get_root_val(self):
        """
        Get the value at root node
        :return:
        """
        return self.node

    def get_left_child(self):
        """
        Get the value at the left child node
        :return:
        """
        return self.left_child

    def get_right_child(self):
        """
        Get the value at the right child node
        :return:
        """
        return self.right_child
