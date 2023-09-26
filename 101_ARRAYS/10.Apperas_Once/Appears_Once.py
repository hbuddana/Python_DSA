arr = [1, 1, 2, 2, 3, 4, 4]

# Initialize count to 0
count = 0

# XOR all the elements in the array
for num in arr:
    count ^= num

print(count) # Prints the number which appears a single time.
