def dfs_post_order(self):
    # Initialize an empty list to store the results (values visited).
    results = []

    def traverse(current_node):
        # Recursively traverse the left subtree if it exists.
        if current_node.left is not None:
            traverse(current_node.left)
        
        # Recursively traverse the right subtree if it exists.
        if current_node.right is not None:
            traverse(current_node.right)
        
        # Visit the current node and append its value to the results.
        results.append(current_node.value)

    # Start the post-order traversal from the root node.
    traverse(self.root)

    # Return the results, which represent the values visited in post-order.
    return results


# The only difference between PreoOrder and PostOrder is, in PostOrder we first traverse and then append. But where as in Preorder we append and then traverse.