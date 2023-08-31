



def pop(self):
    if self.length == 0: # If the LL is empty return None straightaway
        return None 
    
    temp = self.head # We create two buffers, first temp goes on to check whether the next node is None and pre is dependent on it
    pre = self.head
    while(temp.next): # This loop runs till the next node is not None
        pre = temp
        temp = temp.next
    self.tail = pre # When the loop fails we set the tail to the Node before the Last node
    self.tail.next = None # As the following node is None we declare that 
    self.length -= 1

#Lets assume the LL contains only one node

    if self.length == 0: 
        self.head = None
        self.tail = None
    return temp
