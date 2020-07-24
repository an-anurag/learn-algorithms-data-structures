"""
Singly linked list implementation
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.pointer = None


a = Node(1)
b = Node(2)
c = Node(3)

a.pointer = b
b.pointer = c

print(a.value, a.pointer.value, b.pointer.value, c.pointer)
