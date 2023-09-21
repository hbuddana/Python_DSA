def remove_duplicates_in_place(arr):
    if not arr:
        return arr

    # Sort the array to group duplicates together
    arr.sort()

    # Initialize pointers for the unique part of the array
    unique_end = 0

    # Iterate through the sorted array
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_end]:
            # Found a new unique element, move it to the unique part
            unique_end += 1
            arr[unique_end] = arr[i]

    # Slice the array to remove any remaining elements
    arr[unique_end + 1:] = []

# Example usage:
arr = [1, 2, 2, 3, 4, 4, 5]
remove_duplicates_in_place(arr)
print(arr)  # Output: [1, 2, 3, 4, 5]
