def set_value(self, index, value):
    # Get the node at the specified index using the 'get' method.
    temp = self.get(index)
    
    # Check if the 'get' method returned a valid node.
    if temp:
        # If a valid node was found, update its value with the provided 'value'.
        temp.value = value
        return True  # Return True to indicate a successful update.
    
    # If the 'get' method returned None (invalid index), return False to indicate failure.
    return False
