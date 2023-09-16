# Define a method called 'keys' to retrieve all keys stored in the hash table
def keys(self):
    # Initialize an empty list to store all the keys
    all_keys = []
    
    # Iterate through the elements (slots) of the 'data_map' list
    for i in range(len(self.data_map)):
        # Check if the slot at the current index is not empty (i.e., it's not None)
        if self.data_map[i] is not None:
            # Iterate through the list of key-value pairs stored at the current index
            for j in range(len(self.data_map[i])):
                # Append the key (first element of the key-value pair) to the 'all_keys' list
                all_keys.append(self.data_map[i][j][0])
    
    # Return the list of all keys found in the hash table
    return all_keys
