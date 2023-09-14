def dequeue(self):
    # Check if the queue is empty (if the length is 0).
    if self.length == 0:
        return None

    # Store a reference to the current 'first' node in 'temp'.
    temp = self.first

    # Check if there is only one element in the queue.
    if self.length == 1:
        # If there's only one element, set both 'first' and 'last' to None
        # to indicate an empty queue.
        self.first = None
        self.last = None
    else:
        # If there are multiple elements in the queue, update 'first' to point
        # to the next node, effectively removing the current first node.
        self.first = self.first.next
        # Set the 'next' pointer of the removed node ('temp') to None to detach it.
        temp.next = None

    # Decrease the 'length' of the queue to account for the removed element.
    self.length -= 1

    # Return the removed node ('temp').
    return temp
