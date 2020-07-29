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

a.next_pointer = b
b.next_pointer = c
c.next_pointer = d


def find_nth_node(n, head):

    node = head
    for i in range(1, n):
        if node.next_pointer is not None:
            node = node.next_pointer
        else:
            print("n is larger than linked list")

    return node


print(find_nth_node(4, a))