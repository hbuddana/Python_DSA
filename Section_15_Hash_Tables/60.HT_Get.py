# Define a method called 'get_index' to retrieve the value associated with a given key
def get_index(self, key):
    # Calculate the index where the key-value pair is expected to be stored using the '__hash' method
    index = self.__hash(key)
    
    # Check if the slot at the calculated index is not empty (i.e., it's not None)
    if self.data_map[index] is not None:
        # Iterate through the list of key-value pairs stored at the calculated index
        for i in range(len(self.data_map[index])):
            # Check if the KEY at the current position matches the target KEY
            if self.data_map[index][i][0] == key:
                # If a match is found, return the associated VALUE
                return self.data_map[index][i][1]
    
    # If the key is not found or the slot at the index is empty, return None (indicating the key is not in the hash table)
    return None
