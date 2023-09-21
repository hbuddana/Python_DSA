
# Brute Force Method


arr = [1, 2, 3, 7, 5, 5, 8, 8]

# Sort the array in non-decreasing order
arr.sort()

# The second-to-last unique element is the second largest
second_largest = None
for num in reversed(arr):
    if num != second_largest:
        second_largest = num
        break

print(second_largest)
