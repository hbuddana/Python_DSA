def longestSubarraySumK(nums, K):
    # Get the length of the input array `nums`
    n = len(nums)
    
    # Initialize a dictionary to store prefix sums and their corresponding indices
    prefix_sum = {0: -1}
    
    # Initialize the current sum and the maximum subarray length
    current_sum = 0
    max_len = 0

    # Iterate through the input array
    for i in range(n):
        # Calculate the current sum by adding the current element
        current_sum += nums[i]
        
        # Check if (current_sum - K) exists in the prefix_sum dictionary
        if current_sum - K in prefix_sum:
            # If it exists, update the maximum length
            max_len = max(max_len, i - prefix_sum[current_sum - K])
        
        # Check if the current_sum exists in the prefix_sum dictionary
        if current_sum not in prefix_sum:
            # If it doesn't exist, add it with the current index
            prefix_sum[current_sum] = i

    # Return the maximum subarray length with the sum equal to `K`
    return max_len

# Driver code to test the function
if __name__ == "__main__":
    # Example input array
    nums = [1, -1, 5, -2, 3]
    
    # Target sum
    K = 3
    
    # Call the function to find the length of the longest subarray with sum `K`
    result = longestSubarraySumK(nums, K)
    
    # Print the result
    print(f"Length of the longest subarray with sum {K}: {result}")
