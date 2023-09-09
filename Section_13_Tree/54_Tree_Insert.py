def insert(self, value):
    # Create a new node with the given value.
    new_node = Node(value)
    
    # If the tree is empty, set the new node as the root.
    if self.root is None:
        self.root = new_node
        return True
    
    # Start from the root and traverse the tree to find the appropriate position for the new node.
    temp = self.root
    while True:
        # If the value already exists in the tree, return False (no duplicate values allowed in a BST).
        if new_node.value == temp.value:
            return False
        
        # If the new value is less than the current node's value, move to the left subtree.
        if new_node.value < temp.value:
            # If the left child is None, insert the new node as the left child.
            if temp.left is None:
                temp.left = new_node
                return True
            # Otherwise, continue traversing to the left.
            temp = temp.left
        # If the new value is greater than the current node's value, move to the right subtree.
        else:
            # If the right child is None, insert the new node as the right child.
            if temp.right is None:
                temp.right = new_node
                return True
            # Otherwise, continue traversing to the right.
            temp = temp.right
