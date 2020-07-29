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

# before
print(a.next_pointer)
print(b.next_pointer)
print(c.next_pointer)
print(d.next_pointer)

print('function')


def reverse(head):
    current = head
    prev_node = None
    next_node = None

    while current:
        print(current)
        # copy current nodes next node temporarily
        next_node = current.next_pointer
        # assign current nodes next pointer to prev,
        # prev_node is nothing, dont bother about it
        current.next_pointer = prev_node
        # make prev_node meaningful, by making it current node
        prev_node = current
        # make next node new current
        current = next_node
        # prev_node, current = current, next_node

    return prev_node


reverse(a)

# after
print("after reversal")
print(d.next_pointer)
print(c.next_pointer)
print(b.next_pointer)
print(a.next_pointer)

