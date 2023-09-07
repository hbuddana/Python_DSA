def push(self, value):
    # Create a new node with the provided 'value'.
    new_node = Node(value)

    # Check if the stack is empty (height is 0).
    if self.height == 0:
        # If empty, set the 'top' attribute to the new node since it's the first element.
        self.top = new_node
    else:
        # If not empty, add the new node to the top of the stack.
        # 1. Set the 'next' of the new node to the current 'top' node.
        new_node.next = self.top
        # 2. Update the 'top' to be the new node, as it becomes the new top element.
        self.top = new_node

    # Increase the 'height' of the stack to account for the added element.
    self.height += 1
