
# To pop the first node

def pop_first(self): # Check if LL is empty
        if self.length == 0:
            return None
        
        temp = self.head  # If Not Empty, Create a temp direct it to the head, move the head to the next node and equate the removed node to None and reduce the length
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None
        return temp
