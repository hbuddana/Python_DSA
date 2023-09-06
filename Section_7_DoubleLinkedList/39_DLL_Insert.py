def insert(self, index, value):
    # Check if the provided index is out of bounds.
    if index < 0 or index > self.length:
        return False

    # If the index is at the beginning of the list, use the 'prepend' method to add a new node.
    if index == 0:
        return self.prepend(value)

    # If the index is at the end of the list, use the 'append' method to add a new node.
    if index == self.length:
        return self.append(value)

    # Create a new node with the provided 'value'.
    new_node = Node(value)

    # Find the node immediately before the desired index.
    before = self.get(index - 1)

    # Find the node immediately after the desired index.
    after = before.next

    # Update the 'prev' and 'next' pointers of the new node and the nodes around it.
    new_node.prev = before
    new_node.next = after
    before.next = new_node
    after.prev = new_node

    # Increase the length of the linked list to account for the added node.
    self.length += 1

    # Return True to indicate a successful insert operation.
    return True
