def generate_subsequences(arr, current=[], index=0):
    if index == len(arr):
        # If the current sequence is complete, print it.
        print(current)
        return

    # Include the current element in the subsequence.
    generate_subsequences(arr, current + [arr[index]], index + 1)

    # Exclude the current element from the subsequence.
    generate_subsequences(arr, current, index + 1)

# Test the function with the input array [3, 1, 2].
arr = [3, 1, 2]
generate_subsequences(arr)
