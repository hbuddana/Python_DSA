def pop_first(self):
    # Check if the linked list is empty (length is 0).
    if self.length == 0:
        return None

    # Store a reference to the current head node in 'temp'.
    temp = self.head

    # Check if the linked list has only one node.
    if self.length == 1:
        # If there's only one node, set both head and tail to None since the list will become empty.
        self.head = None
        self.tail = None
    else:
        # If there's more than one node, update the head to be the next node.
        self.head = self.head.next
        # Set the 'prev' pointer of the new head to None, indicating the start of the list.
        self.head.prev = None
        # Set the 'next' pointer of the removed node ('temp') to None to detach it from the list.
        temp.next = None

    # Decrease the length of the linked list to account for the removed node.
    self.length -= 1

    return True


