def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False  # Return False as soon as an out-of-order pair is found
    return True  # Return True only if the loop completes without finding any out-of-order pairs

# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 3, 2, 4, 5]

print(is_sorted(arr1))  # Output: True (sorted)
print(is_sorted(arr2))  # Output: False (not sorted)
