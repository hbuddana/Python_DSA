# Two - Pass technique : Better Approach

arr = [1, 2, 3, 7, 8, 8]

# First pass: Find the largest element
largest = float('-inf')
for num in arr:
    if num > largest:
        largest = num

# Initialize the second largest to a value smaller than any element in the array
second_largest = float('-inf')

# Second pass: Find the second largest element by comparing with the largest
for num in arr:
    if num != largest and num > second_largest:
        second_largest = num

# Check if a second largest element was found
if second_largest != float('-inf'):
    print(second_largest)
else:
    print("There is no second largest element.")
