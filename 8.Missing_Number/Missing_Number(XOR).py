def find_missing_number(nums):
    # Initialize the result to 0
    result = 0

    # XOR all the numbers in the input array
    for num in nums:
        result ^= num

    # XOR all numbers from 1 to n, where n is the length of the input array + 1
    for i in range(1, len(nums) + 2):
        result ^= i

    # The result now contains the missing number
    return result

# Example usage:
arr = [1, 2, 4, 6, 3, 7, 8]
missing_num = find_missing_number(arr)
print("The missing number in the array is:", missing_num)
