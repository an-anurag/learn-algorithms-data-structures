"""
Traverse tree in inorder fashion
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


def inorder(tree):

    if tree:
        root = tree
        inorder(root.left_child)
        print(root, end=' ')
        inorder(root.right_child)


inorder(t)


print()


def inorder_iter(tree):

    node_stack = []
    root = tree

    if root.left_child:
        node_stack.append(root.left_child)

    node_stack.append(tree)

    if root.right_child:
        node_stack.append(root.right_child)

    node = node_stack.pop()
    print(node.node)


inorder_iter(t)