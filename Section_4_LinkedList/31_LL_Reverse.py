

def reverse(self):
    # Swap the head and tail pointers to reverse the order of the list
    temp = self.head
    self.head = self.tail
    self.tail = temp

    after = temp.next  # Store the next node after the current node
    before = None  # Initialize a pointer to the previous node (starts as None)

    # Loop through each node in the list to reverse the links
    for _ in range(self.length):
        after = temp.next  # Store the next node after the current node
        temp.next = before  # Update the "next" pointer of the current node to point backward
        before = temp  # Move the "before" pointer to the current node
        temp = after  # Move the "temp" pointer to the next node

