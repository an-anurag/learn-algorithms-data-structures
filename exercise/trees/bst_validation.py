"""
Check given binary tree is bst or not
"""

# get the root node
# check its left child, it must be less than root
# check its right child, it must be greater that root
# if any node violating these condition
# then it is not bst


def solution(tree):

    node_stack = [tree]
    root = tree

    if root:

        current_node = node_stack.pop()

        if root.right_child:
            node_stack.append(root.right_child)



