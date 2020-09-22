def traverse(self):
    """Return the length of this linked list by traversing its nodes."""
    current = self.head  # start at the head

    # Loop through all nodes
    while current is not None:
        current = current.next
