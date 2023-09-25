def move_zeroes_to_end(arr):
    left = 0  # Left pointer starts at the beginning of the array

    # Iterate through the array with the right pointer
    for right in range(len(arr)):
        if arr[right] != 0:
            # Swap non-zero element at 'right' with element at 'left'
            arr[left], arr[right] = arr[right], arr[left]
            left += 1  # Increment the left pointer

    return arr

# Example usage:
arr = [1, 0, 2, 0, 3, 4, 0, 5]
print(move_zeroes_to_end(arr))
