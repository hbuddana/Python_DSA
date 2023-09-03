

# Define a Node class to represent individual elements of the linked list
class Node:
    def __init__(self, value):
        # Initialize a new node with a given value
        self.value = value
        # Initialize the 'next' attribute to None, indicating it's the last node in the beginning
        self.next = None

# Define a LinkedList class to represent a singly linked list
class LinkedList:
    def __init__(self, value):
        # Create a new node with the provided value
        new_node = Node(value)
        # Set the 'head' of the linked list to the new node
        self.head = new_node
        # Set the 'tail' of the linked list to the new node
        self.tail = new_node
        # Initialize the 'length' attribute to 1 since there's one node in the list
        self.length = 1
