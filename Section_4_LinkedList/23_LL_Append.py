
# Apppend

# First check if the LL is empty, if it is empty we need to direct both head and tail to the new node created

# In normal case, just make sure the new node is pointed next to the present tail and then make the newly added node as the tail

def append(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
    self.length += 1
