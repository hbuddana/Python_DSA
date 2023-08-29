def remove(self, index):
    # Check if the given index is out of bounds
    if index < 0 or index >= self.length:
        return None  # Return None if the index is invalid
    
    # Check if the index is at the beginning of the list
    if index == 0:
        return self.pop_first()  # Call the pop_first method to remove the first node
    
    # Check if the index is at the end of the list
    if index == self.length - 1:
        return self.pop()  # Call the pop method to remove the last node
    
    # Get the node at the index just before the node to be removed
    pre = self.get(index - 1)
    
    # Get the node to be removed
    temp = pre.next
    
    # Update the "next" pointer of the previous node to skip the node to be removed
    pre.next = temp.next
    
    # Disconnect the removed node from the list
    temp.next = None
    
    # Decrease the length of the list by 1
    self.length -= 1
    
    return temp  # Return the removed node
