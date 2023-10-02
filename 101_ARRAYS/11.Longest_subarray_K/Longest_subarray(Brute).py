def longestSubarraySumK(nums, K):
    # Get the length of the input array `nums`
    n = len(nums)
    
    # Initialize a variable to store the maximum subarray length
    max_len = 0

    # Iterate through each possible starting index of the subarray
    for start in range(n):
        # Initialize the current sum for this subarray
        current_sum = 0
        
        # Iterate through each possible ending index of the subarray
        for end in range(start, n):
            # Add the current element to the current sum
            current_sum += nums[end]
            
            # If the current sum equals the target sum `K`, update the maximum length
            if current_sum == K:
                max_len = max(max_len, end - start + 1)

    # Return the maximum subarray length with the sum equal to `K`
    return max_len

# Driver code to test the function
if __name__ == "__main__":
    # Example input array
    nums = [1,2,3,1,1,1,1,4,2,3]
    
    # Target sum
    K = 3
    
    # Call the function to find the length of the longest subarray with sum `K`
    result = longestSubarraySumK(nums, K)
    
    # Print the result
    print(f"Length of the longest subarray with sum {K}: {result}")
