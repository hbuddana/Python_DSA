# Definition of a Node class for creating individual nodes in a singly linked list.
class Node:
    def __init__(self, value):
        self.value = value  # Data stored in the node.
        self.next = None    # Reference to the next node in the list.

# Definition of a Stack class representing a stack data structure.
class Stack:
    def __init__(self, value):
        
        new_node = Node(value) # Create a new node with the provided 'value'.
        self.top = new_node  # Initialize the 'top' attribute to point to the new node.
        self.height = 1 # Initialize the 'height' attribute to 1, indicating one element in the stack.

    # Method to print the elements of the stack.
    def print_list(self):
        temp = self.top  # Start from the 'top' of the stack.
        while temp is not None:
            print(temp.value)  # Print the value of the current node.
            temp = temp.next  # Move to the next node in the list.

# Create a new stack called 'my_stack' with an initial value of 4.
my_stack = Stack(4)

# Call the 'print_list' method to print the elements in the stack.
my_stack.print_list()
