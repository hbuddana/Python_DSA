def contains(self, value):
    # Check if the tree is empty. If it is, return False since the value cannot exist in an empty tree.
    if self.root is None:
        return False
    
    # Start from the root and traverse the tree.
    temp = self.root
    while temp is not None:
        # If the value is less than the current node's value, move to the left subtree.
        if value < temp.value:
            temp = temp.left
        # If the value is greater than the current node's value, move to the right subtree.
        elif value > temp.value:
            temp = temp.right
        # If the value matches the current node's value, return True (value found).
        else:
            return True
    
    # If the loop completes without finding the value, return False (value not found).
    return False
