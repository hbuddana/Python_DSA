# Define a Node class to represent individual nodes in the binary search tree.
class Node:
    def __init__(self, value):
        self.value = value  # The value stored in this node.
        self.left = None    # Reference to the left child node.
        self.right = None   # Reference to the right child node.

# Define a BinarySearchTree class to manage the binary search tree.
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize the root of the tree as None.

# Create an instance of the BinarySearchTree class.
my_tree = BinarySearchTree()

# Print the root of the tree (initially None).
print(my_tree.root)

 
"""
    EXPECTED OUTPUT:
    
    None

"""
