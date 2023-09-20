# Create a list containing some numbers
arr = [1, 2, 3, 7, 5, 8]

# Initialize a variable 'max' with the first element of the list 'arr'
max = arr[0]

# Iterate through the indices of the list 'arr' using a for loop
for i in range(len(arr)):
    # Check if the current element at index 'i' is greater than the current 'max'
    if arr[i] > max:
        # If it is, update 'max' to the new maximum value
        max = arr[i]

# After the loop finishes, 'max' will contain the maximum value in the list 'arr'

# Print the maximum value
print(max)


# Optimal solution with O(n) runtime.

# Brute - Force Method: Just sort the array and return the last element.
