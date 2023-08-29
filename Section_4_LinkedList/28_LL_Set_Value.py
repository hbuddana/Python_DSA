


def get(self, index):
    if index < 0 or index >= self.length:
        return None
    temp = self.head
    for _ in range(index):
        temp = temp.next # The loop iterates index times. In each iteration, the variable temp is moved to the next node in the list.
    return temp # Prints the node at the given index



# Set_Value


def set_value(self, index, value):
    temp =self.get(index) # The temp variable is assigned the result of calling the get() method with the specified index.
    if temp:
        temp.value = value
        return True
    return False