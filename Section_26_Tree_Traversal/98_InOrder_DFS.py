def dfs_in_order(self):
    # Initialize an empty list to store the results (values visited).
    results = []

    def traverse(current_node):
        # Recursively traverse the left subtree if it exists.
        if current_node.left is not None:
            traverse(current_node.left)
        
        # Visit the current node and append its value to the results.
        results.append(current_node.value)
        
        # Recursively traverse the right subtree if it exists.
        if current_node.right is not None:
            traverse(current_node.right)

    # Start the in-order traversal from the root node.
    traverse(self.root)

    # Return the results, which represent the values visited in in-order.
    return results

# Now for InOrder, we traverse left, Append the values and then traverse the right subtree.