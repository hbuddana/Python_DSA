def get(self, index):
    # Check if the provided index is out of bounds.
    if index < 0 or index >= self.length:
        return None

    # Initialize a temporary pointer 'temp' to the head of the linked list.
    temp = self.head

    # Check if the provided index is closer to the head or tail of the list.
    if index < self.length / 2:
        # If the index is closer to the head, iterate forward from the head to the desired index.
        for _ in range(index):
            temp = temp.next
    else:
        # If the index is closer to the tail, iterate backward from the tail to the desired index.
        temp = self.tail
        for _ in range(self.length - 1, index, -1):
            temp = temp.prev

    # Return the node at the specified index.
    return temp
