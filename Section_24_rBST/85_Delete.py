def min_value(self, current_node):
    # Find the minimum value in the BST by traversing the left subtree.
    while current_node.left is not None:
        current_node = current_node.left
    return current_node.value

def __delete_node(self, current_node, value):
    if current_node is None:
        return None
    
    # If the value is less than the current node's value, recursively delete it in the left subtree.
    if value < current_node.value:
        current_node.left = self.__delete_node(current_node.left, value)
    
    # If the value is greater than the current node's value, recursively delete it in the right subtree.
    elif value > current_node.value:
        current_node.right = self.__delete_node(current_node.right, value)
    
    else:
        # Case 1: Node to delete has no children (leaf node).
        if current_node.left is None and current_node.right is None:
            return None
        # Case 2: Node to delete has one child (either left or right).
        elif current_node.left is None:
            current_node = current_node.right
        elif current_node.right is None:
            current_node = current_node.left
        # Case 3: Node to delete has two children.
        else:
            # Find the minimum value in the right subtree (successor).
            sub_tree_min = self.min_value(current_node.right)
            current_node.value = sub_tree_min
            # Delete the successor node from the right subtree.
            current_node.right = self.__delete_node(current_node.right, sub_tree_min)
    
    # Return the modified current_node (with potential new subtrees).
    return current_node

def delete_node(self, value):
    # Start the deletion process from the root node.
    self.root = self.__delete_node(self.root, value)


"""min_value is a method that finds the minimum value in a Binary Search Tree (BST) by traversing the left subtree from the given current_node.
__delete_node is a private recursive helper method for deleting a node with a specific value from the BST.
It takes three arguments: current_node, which represents the current node being checked during deletion, value, which is the value to be deleted, and it handles three cases:
The node to delete has no children (a leaf node).
The node to delete has one child.
The node to delete has two children.
The delete_node method serves as a public interface(for ease) for deleting values from the BST, and it starts the deletion process from the root."""
