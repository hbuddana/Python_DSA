# Insert at given Index

def insert(self, index, value):
    # Check if the given index is out of bounds
    if index < 0 or index >= self.length:
        return False  # Return False if the index is invalid
    
    # Check if the index is at the beginning of the list
    if index == 0:
        return self.prepend(value)  # Call the prepend method to insert at the beginning
    
    # Check if the index is at the end of the list
    if index == self.length:
        return self.append(value)  # Call the append method to insert at the end
    
    # Create a new node with the given value
    new_node = Node(value)
    
    # Get the node at the index just before the desired insertion point
    temp = self.get(index - 1)
    
    # Set the new node's "next" pointer to the node that was originally at the index
    new_node.next = temp.next
    
    # Update the "next" pointer of the previous node to point to the new node
    temp.next = new_node
    
    # Increase the length of the list by 1
    self.length += 1
    
    return True  # Return True to indicate successful insertion
