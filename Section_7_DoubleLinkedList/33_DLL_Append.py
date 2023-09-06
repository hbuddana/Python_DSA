def append(self, value):
    # Create a new node with the provided value.
    new_node = Node(value)
    
    # Check if the linked list is currently empty (head is None).
    if self.head is None:
        # If empty, set both head and tail to the new node since it's the only node in the list.
        self.head = new_node
        self.tail = new_node
    else:
        # If not empty, add the new node to the end of the linked list.
        # 1. Set the 'next' of the current tail node to the new node.
        self.tail.next = new_node
        # 2. Set the 'prev' of the new node to the current tail node.
        new_node.prev = self.tail
        # 3. Update the tail to be the new node, as it is now the last node in the list.
        self.tail = new_node
    
    # Increase the length of the linked list to account for the added node.
    self.length += 1
    
    # Return True to indicate a successful append operation.
    return True
