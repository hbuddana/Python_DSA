def pop(self):
    # Check if the stack is empty (height is 0).
    if self.height == 0:
        return None

    # Store a reference to the current top node in 'temp'.
    temp = self.top

    # Update the 'top' to point to the next node, effectively removing the current top node.
    self.top = self.top.next

    # Set the 'next' pointer of the removed node ('temp') to None to detach it from the stack.
    temp.next = None

    # Decrease the 'height' of the stack to account for the removed element.
    self.height -= 1

    # Return the removed node ('temp').
    return temp
