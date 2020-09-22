def length(self):
    """Return the length of this linked list by traversing its nodes."""
    node_count = 0  # initial count is zero
    current = self.head  # start at the head

    # Loop through all nodes
    while current is not None:
        current = current.next
        # add one to the counter each time
        node_count += 1
    # return the total length
    return node_count