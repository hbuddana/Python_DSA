def find_missing_number(arr, n):
    # Calculate the expected sum of the first n natural numbers
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the elements in the array
    actual_sum = sum(arr)
    
    # Find the missing number
    missing_number = expected_sum - actual_sum
    
    return missing_number

arr = [1, 2, 4, 6, 3, 7, 8]
n = 8  # The range of natural numbers is from 1 to 8

missing_number = find_missing_number(arr, n)
print("The missing number is:", missing_number)


"""
O(n)
O(1)
"""