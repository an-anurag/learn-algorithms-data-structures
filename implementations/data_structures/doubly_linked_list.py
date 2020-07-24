"""
Doubly linked list implementation
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None


a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.prev_node = a
b.next_node = c
c.prev_node = b

print(a.value, '-->', a.next_node.value, '-->', b.next_node.value, '-->', c.next_node)
print(a.prev_node, '<--', b.prev_node.value, '<--', c.prev_node.value)