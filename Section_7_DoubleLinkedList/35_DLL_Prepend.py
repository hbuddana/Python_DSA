
def prepend(self, value):
    # Create a new node with the provided value.
    new_node = Node(value)

    # Check if the linked list is currently empty (head is None).
    if self.head is None:
        # If empty, set both head and tail to the new node since it's the only node in the list.
        self.head = new_node
        self.tail = new_node
    else:
        # If not empty, add the new node to the beginning of the linked list.
        # 1. Set the 'next' of the new node to the current head node.
        new_node.next = self.head
        # 2. Set the 'prev' of the current head node to the new node.
        self.head.prev = new_node
        # 3. Update the head to be the new node, as it is now the first node in the list.
        self.head = new_node

    # Increase the length of the linked list to account for the added node.
    self.length += 1

    # Return True to indicate a successful prepend operation.
    return True
