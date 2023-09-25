def left_rotate_array(arr, d):
    n = len(arr)  # Get the length of the array
    
    # Handle cases where d is larger than the array length
    d %= n  # Take the modulus of d with n to ensure it's within bounds
    
    # Reverse the first part (0 to d-1)
    reverse_array(arr, 0, d - 1)
    
    # Reverse the second part (d to n-1)
    reverse_array(arr, d, n - 1)
    
    # Reverse the entire array
    reverse_array(arr, 0, n - 1)

def reverse_array(arr, start, end):
    # Reverse the elements in the array between 'start' and 'end' indices
    while start < end:
        # Swap the elements at 'start' and 'end'
        arr[start], arr[end] = arr[end], arr[start]
        start += 1  # Move 'start' index forward
        end -= 1    # Move 'end' index backward

# Example usage:
arr = [1, 2, 3, 4, 5]
d = 6
left_rotate_array(arr, d)
print("Rotated Array:", arr)
