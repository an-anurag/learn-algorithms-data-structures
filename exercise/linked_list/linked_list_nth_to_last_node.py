"""
Return a node from nth to the last of linked list
eg - nth_to_last(2, head) -> returns 2nd to the last of list

"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next_pointer = None

    def __str__(self):
        return str(self.value)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)


a.next_pointer = b
b.next_pointer = c
c.next_pointer = d
d.next_pointer = e
e.next_pointer = f


def nth_to_the_last(n, head):

    marker1 = head
    marker2 = head

    for i in range(n):
        if not marker2.next_pointer:
            raise LookupError("N is larger than linked list")
        marker2 = marker2.next_pointer

    while marker2.next_pointer:
        marker1 = marker1.next_pointer
        marker2 = marker2.next_pointer

    return marker1


print(nth_to_the_last(2, a))
