

def prepend(self, value): #Prepend takes in the value 
    new_node = Node(value)
    if self.length == 0: # Checks if LL is empty 
        self.head = new_node
        self.tail = new_node
    else:                        # If not empty new node should point to the present head 
        new_node.next = self.head
        self.head = new_node     #  And now the head should point to the new node

    self.length += 1
    return True








    