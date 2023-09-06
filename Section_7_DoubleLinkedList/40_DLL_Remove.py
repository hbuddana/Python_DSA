def remove(self, index):
    # Check if the provided index is out of bounds.
    if index < 0 or index >= self.length:
        return None

    # If the index is 0, use the 'pop_first' method to remove and return the first node.
    if index == 0:
        return self.pop_first()

    # If the index is at the end of the list, use the 'pop' method to remove and return the last node.
    if index == self.length - 1:
        return self.pop()

    # Get the node at the specified index using the 'get' method.
    temp = self.get(index)

    # Update the 'prev' and 'next' pointers of adjacent nodes to remove 'temp' from the list.
    temp.next.prev = temp.prev
    temp.prev.next = temp.next

    # Set 'next' and 'prev' pointers of 'temp' to None to detach it from the list.
    temp.next = None
    temp.prev = None

    # Decrease the length of the linked list to account for the removed node.
    self.length -= 1

    # Return the removed node ('temp').
    return temp
