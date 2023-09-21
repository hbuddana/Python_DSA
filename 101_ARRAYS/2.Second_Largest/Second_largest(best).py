# Optimal Method - 

arr = [1, 2, 3, 7, 5, 8, 8]  # Example with duplicate values

# Initialize largest to the first element and second largest to -1
largest = arr[0]
second_largest = -1

# Iterate through the array to find the largest and second largest
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest and num > second_largest:
        second_largest = num

# Print both largest and second largest
print("Largest:", largest)
print("Second Largest:", second_largest)
