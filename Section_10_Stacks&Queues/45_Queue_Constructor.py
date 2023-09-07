# Definition of a Node class for creating individual nodes in a singly linked list.
class Node:
    def __init__(self, value):
        self.value = value  # Data stored in the node.
        self.next = None    # Reference to the next node in the list.

# Definition of a Queue class representing a queue data structure.
class Queue:
    def __init__(self, value):
        # Create a new node with the provided 'value'.
        new_node = Node(value)
        
        # Initialize the 'first' attribute to point to the new node.
        self.first = new_node
        
        # Initialize the 'last' attribute to also point to the new node.
        self.last = new_node 
        
        # Initialize the 'length' attribute to 1, indicating one element in the queue.
        self.length = 1

    # Method to print the elements of the queue.
    def print_queue(self):
        temp = self.first  # Start from the 'first' of the queue.
        while temp is not None:
            print(temp.value)  # Print the value of the current node.
            temp = temp.next  # Move to the next node in the list.

# Create a new queue called 'my_q' with an initial value of 4888.
my_q = Queue(4888)

# Call the 'print_queue' method to print the elements in the queue.
my_q.print_queue()
