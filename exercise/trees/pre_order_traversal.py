"""
Traverse tree in pre order fashion
"""

from implementations.data_structures.tree import BinaryTree
from exercise.trees.level_order_travarsal import levelOrderPrint

t = BinaryTree('A')
t.left_child = BinaryTree('B')
t.right_child = BinaryTree('C')

t.left_child.left_child = BinaryTree('D')
t.left_child.right_child = BinaryTree('E')

t.right_child.left_child = BinaryTree('F')
t.right_child.right_child = BinaryTree('G')

levelOrderPrint(t)

print()


def preorder(tree):

    if tree:
        root = tree
        print(root, end=' ')
        preorder(root.left_child)
        preorder(root.right_child)


preorder(t)

print()


def preorder_iter(tree):
    root = tree
    nodes = [root]

    while nodes:
        current_node = nodes.pop()
        print(current_node.node, end=' ')
        if current_node.right_child:
            nodes.append(current_node.right_child)
        if current_node.left_child:
            nodes.append(current_node.left_child)


preorder_iter(t)
