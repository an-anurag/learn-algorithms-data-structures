"""
Check whether given linked_list has a loop
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.pointer = None

    def method(self, a, b):
        pass

class A(Node):
    def method(self, a=None, b=None, c=None):
        print(1)


z = A(5)
z.method()


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.pointer = b
b.pointer = c
c.pointer = d
f.pointer = e
e.pointer = f
f.pointer = c