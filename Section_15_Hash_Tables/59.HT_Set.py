# Define a method called 'set_item' to add or update a key-value pair in the hash table
def set_item(self, key, value):
    # Calculate the index where the key-value pair should be stored using the '__hash' method
    index = self.__hash(key)
    
    # Check if the slot at the calculated index is empty (None)
    if self.data_map[index] == None:
        # If it's empty, initialize it as an empty list to hold key-value pairs
        self.data_map[index] = []
    
    # Append a new list containing the key and value to the slot at the calculated index
    # This allows handling collisions by storing multiple key-value pairs in the same slot
    self.data_map[index].append([key, value])
