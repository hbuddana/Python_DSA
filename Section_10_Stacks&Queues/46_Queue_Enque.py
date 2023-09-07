
def enqueue(self, value):
    # Create a new node with the provided 'value'.
    new_node = Node(value)

    # Check if the queue is empty (first is None).
    if self.first is None:
        # If the queue is empty, set both 'first' and 'last' to the new node.
        self.first = new_node
        self.last = new_node
    else:
        # If the queue is not empty, add the new node to the end of the queue:
        # 1. Set the 'next' pointer of the current last node to the new node.
        self.last.next = new_node
        # 2. Update the 'last' attribute to be the new node, as it becomes the new last element.
        self.last = new_node 
    # Increase the 'length' of the queue to account for the added element.
    self.length += 1
