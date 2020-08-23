
"""
Main driver code for the assignment runs on python 3.6+ only
Created on 23/08/2020
@author: Anurag Gundappa
"""

# imports
try:
    from assignments.binary_tree import BinaryTree
except ModuleNotFoundError:
    from binary_tree import BinaryTree


# Approach 1: no nodes given.
# It gives the distance between first and last node by default in each level

def find_distance(tree) -> None:
    """
    finds the horizontal distance between first and last node
    in the every level of binary tree

    :param tree: root of the binary tree
    :return: None
    """

    # edge case check
    if not tree:
        return

    # temporary storage of tree nodes
    nodes = [tree]
    # initialization
    current_count, next_count = 1, 0

    while nodes:
        current_node = nodes.pop(0)
        current_count -= 1

        if current_node:

            # make sure at least one child is present for current node
            if current_node.left_child or current_node.right_child:
                # add left node to count
                nodes.append(current_node.left_child)
                next_count += 1
                # add right node to count
                nodes.append(current_node.right_child)
                next_count += 1

        # check if current level has no nodes left to visit
        if current_count == 0:

            # make sure there are nodes in node list after pop operation
            if nodes:
                # all the middle nodes except first and last is the total distance
                # including absent nodes
                distance = len(nodes[1:len(nodes) - 1])
                print("distance between node %s and node %s is %s" % (nodes[0], nodes[-1], distance))

            # prepare for next iteration
            current_count, next_count = next_count, current_count


# Approach 2: nodes given as input.
# argument nodes can be any two nodes but they has to be from same level
# random nodes would yield weird result

def find_distance2(tree, node1, node2):
    """
    finds the horizontal distance between any two nodes present at same level,
    It wont handle duplicate node value in given level

    :param tree: root node of the binary tree
    :param node1: starting node from where distance should be measured
    :param node2: the last node up to which the distance should be measured
    :return: int
    """

    # edge case check
    if not tree:
        return

    # temporary storage of tree nodes
    nodes = [tree]
    # initialization
    current_count, next_count = 1, 0
    distance = 0

    while nodes:
        current_node = nodes.pop(0)
        current_count -= 1

        if current_node:

            # if current node is the first argument then start counting distance
            if current_node.node == node1:
                distance = 0

            # if we found current node is equal with second argument then stop looking further
            elif current_node.node == node2:
                break

            # add 1 to the distance for each present node
            else:
                distance += 1

            # make sure at least one child is present for current node
            if current_node.left_child or current_node.right_child:
                # add left node to count
                nodes.append(current_node.left_child)
                next_count += 1
                # add right node to count
                nodes.append(current_node.right_child)
                next_count += 1

        # add 1 to the distance for each absent node
        else:
            distance += 1

        # check if current level has no nodes left to visit
        if current_count == 0:
            # prepare for next iteration
            current_count, next_count = next_count, current_count

    return "distance between node %s and node %s is %s" % (node1, node2, distance)


if __name__ == '__main__':

    # create the desired binary tree for eg-

    fig = r"""
                5
              /   \
             2     3
            / \   /  \
           7   N  N   1
          / \         /\
         9   N       4  6

    """

    # level 1
    tree = BinaryTree(5)

    # level 2
    tree.add_left_child(2)
    tree.add_right_child(3)

    # level 3
    left_node1 = tree.get_left_child()
    right_node1 = tree.get_right_child()
    left_node1.add_left_child(7)
    right_node1.add_right_child(1)

    # level 4
    left_node2 = left_node1.get_left_child()
    left_node2.add_left_child(9)
    right_node2 = right_node1.get_right_child()
    right_node2.add_left_child(4)
    right_node2.add_right_child(6)

    # test solution
    print(fig)
    print("Solution: 1 passing root only")
    find_distance(tree)
    print()
    print("Solution: 2 passing desired nodes")
    # test solution 2
    dist = find_distance2(tree, 9, 6)
    print(dist)
