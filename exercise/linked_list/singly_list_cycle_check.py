class Node:

    def __init__(self, value):
        self.value = value
        self.pointer = None


a = Node(1)
b = Node(2)
c = Node(3)

a.pointer = b
b.pointer = c
c.pointer = a


def is_cycle(node):
    marker1 = node
    marker2 = node

    while (marker2 is not None) and (marker2.pointer is not Node):
        marker1 = marker1.pointer
        marker2 = marker2.pointer.pointer

        if marker2 == marker1:
            return True
    return False


print(is_cycle(a))