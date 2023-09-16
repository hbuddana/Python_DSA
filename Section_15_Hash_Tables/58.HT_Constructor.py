# Define a class called HashTable
class HashTable:
    # Constructor method to initialize the hash table with a specified size (default is 7)
    def __init__(self, size=7):
        # Create an empty list of 'size' number of elements to represent the hash table
        self.data_map = [None] * size

    # Private method '__hash' to calculate the hash value for a given 'key'
    def __hash(self, key):
        # Initialize a variable 'my_hash' to store the calculated hash value
        my_hash = 0
        
        # Iterate through each character in the 'key'
        for letter in key:
            # Calculate the ASCII value of the character (ord(letter)) and multiply it by 23
            # Add this result to 'my_hash'
            my_hash = (my_hash + ord(letter) * 23 )
        
        # Take the remainder of 'my_hash' when divided by the length of the data_map
        # This ensures that the hash value falls within the range of valid indices
        my_hash = my_hash % len(self.data_map)
        
        # Return the calculated hash value
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

my_hash_table = HashTable()

my_hash_table.print_table()




"""
This code defines a HashTable class with an underlying data structure represented as a list.

The constructor initializes the hash table with a given size, which defaults to 7 if not specified.

The __hash method calculates a hash value for a given key by iterating through its characters, multiplying their ASCII values by 23, and summing them up. This process results in a numerical hash value.

To ensure that the hash value is within the valid index range of the data_map list, it takes the remainder when divided by the length of the data_map.

The calculated hash value is then returned

"""