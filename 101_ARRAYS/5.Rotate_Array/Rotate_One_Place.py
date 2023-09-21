def left_rotate_by_one(arr):
    if not arr or len(arr) < 2:
        return arr  # No rotation needed for empty or single-element arrays

    first_element = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[-1] = first_element


arr = [1, 2, 3, 4, 5]
left_rotate_by_one(arr)
print(arr)  # Output: [2, 3, 4, 5, 1]
