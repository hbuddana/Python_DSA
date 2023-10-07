def dfs_pre_order(self):
    # Initialize an empty list to store the results (values visited).
    results = []

    def traverse(current_node):
        # Visit the current node and append its value to the results.
        results.append(current_node.value)
        
        # Recursively traverse the left subtree if it exists.
        if current_node.left is not None:
            traverse(current_node.left)
        
        # Recursively traverse the right subtree if it exists.
        if current_node.right is not None:
            traverse(current_node.right)

    # Start the pre-order traversal from the root node.
    traverse(self.root)

    # Return the results, which represent the values visited in pre-order.
    return results


"""
dfs_pre_order is a method for performing a Depth-First Search (DFS) traversal of a Binary Search Tree (BST) in pre-order.
The method initializes an empty list results to store the values visited during traversal.

Inside the traverse function (a recursive inner function):

It appends the value of the current node to the results list.
If the current node has a left child, it recursively calls traverse on the left child.
If the current node has a right child, it recursively calls traverse on the right child.
The traverse function is used to visit each node in the BST recursively, starting from the root node, following a pre-order traversal pattern (root, left, right)."""