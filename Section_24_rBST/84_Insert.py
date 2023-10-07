def __r_insert(self, current_node, value):
    # Base case: If the current_node is None, create a new Node with the given value.
    if current_node is None:
        return Node(value)
    
    # If the value is less than the current node's value, recursively insert it in the left subtree.
    if value < current_node.value:
        current_node.left = self.__r_insert(current_node.left, value)
    
    # If the value is greater than the current node's value, recursively insert it in the right subtree.
    if value > current_node.value:
        current_node.right = self.__r_insert(current_node.right, value)
    
    # Return the modified current_node (with potential new subtrees).
    return current_node

def r_insert(self, value):
    # If the tree is empty (root is None), create a new root node with the given value.
    if self.root is None:
        self.root = Node(value)
    else:
        # Call the recursive insert method starting from the root.
        self.__r_insert(self.root, value)


"""
__r_insert is a private recursive helper method for inserting a value into a Binary Search Tree (BST).

It takes two arguments: current_node, which represents the current node being checked during insertion, and value, which is the value to be inserted.

The base case checks if the current_node is None, indicating that we've reached a leaf node, and in this case, it creates a new Node with the given value."""