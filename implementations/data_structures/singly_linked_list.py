"""
Singly linked list implementation
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.pointer = None


a = Node('A')
b = Node('B')
c = Node('C')

a.pointer = b
b.pointer = c
c.pointer = a

print(a.value, a.pointer.value, b.pointer.value, c.pointer)


