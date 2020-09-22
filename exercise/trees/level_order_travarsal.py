"""
Main driver code for the assignment
"""

from implementations.data_structures.tree import BinaryTree
import collections


def levelOrderPrint(tree):
    if not tree:
        return
    nodes = collections.deque([tree])
    currentCount, nextCount = 1, 0
    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -= 1
        print(currentNode.node, end=" ")
        if currentNode.left_child:
            nodes.append(currentNode.left_child)
            nextCount += 1
        if currentNode.right_child:
            nodes.append(currentNode.right_child)
            nextCount += 1
        if currentCount == 0:
            #finished printing current level
            print()
            currentCount, nextCount = nextCount, currentCount


if __name__ == '__main__':
    # create the desired binary tree

    """
                5
              /   \
             2     3
            /       \
           7         1
          /          /\
         9          4  6
    """

    # level 1
    tree = BinaryTree(5)

    # level 2
    tree.add_left_child(2)
    tree.add_right_child(3)

    # level 3
    two = tree.get_left_child()
    three = tree.get_right_child()
    two.add_left_child(7)
    three.add_right_child(1)

    # level 4
    seven = two.get_left_child()
    one = three.get_right_child()
    seven.add_left_child(9)
    one.add_left_child(4)
    one.add_right_child(6)

    levelOrderPrint(tree)