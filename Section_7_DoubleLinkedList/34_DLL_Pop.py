def pop(self):
    # Check if the linked list is empty (length is 0).
    if self.length == 0:
        return None

    # Store a reference to the current tail node in 'temp'.
    temp = self.tail

    # Check if the linked list has only one node.
    if self.length == 1:
        # If there's only one node, set both head and tail to None since the list will become empty.
        self.head = None
        self.tail = None
    else:
        # If there's more than one node, update the tail to be the previous node.
        self.tail = self.tail.prev
        # Set the 'next' pointer of the new tail to None, indicating the end of the list.
        self.tail.next = None
        # Set the 'prev' pointer of the removed node to None to detach it from the list.
        temp.prev = None

    # Decrease the length of the linked list to account for the removed node.
    self.length -= 1

    # Return the removed node ('temp').
    return temp
