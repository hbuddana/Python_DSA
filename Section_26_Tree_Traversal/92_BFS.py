def BFS(self): # METHOD IN BST
    # Start the breadth-first search from the root node.
    current_node = self.root
    results = []  # Initialize a list to store the results (values visited).
    queue = []    # Initialize a queue for BFS traversal. IT STORES THE COMPLETE NODE
    queue.append(current_node)  # Enqueue the root node to start the traversal.

    while len(queue) > 0:
        current_node = queue.pop(0)  # Dequeue the first node in the queue.
        results.append(current_node.value)  # Add the current node's value to the results.

        # Enqueue the left child if it exists.
        if current_node.left is not None:
            queue.append(current_node.left)

        # Enqueue the right child if it exists.
        if current_node.right is not None:
            queue.append(current_node.right)

    # Return the results, which represent the values visited in BFS order.
    return results

"""
BFS is a method for performing a Breadth-First Search (BFS) traversal of a Binary Search Tree (BST).
The method initializes current_node to the root node and creates an empty list results to store the values visited during traversal.
It also creates a queue to implement BFS, starting with the root node in the queue.

Inside the while loop:

It dequeues (pops) the first node from the queue (queue.pop(0)).
It appends the value of the current node to the results list.
If the current node has a left child, it enqueues (appends) the left child to the queue.
If the current node has a right child, it enqueues (appends) the right child to the queue.
This process continues until the queue is empty, which means that all nodes have been visited in BFS order."""