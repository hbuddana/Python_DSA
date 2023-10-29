def count_subsequences_with_sum(arr, k):
    def count_subsequence_helper(index, current_sum):
        if index == len(arr):
            # If we reach the end of the array, check if the current_sum is equal to k.
            return 1 if current_sum == k else 0

        # Include the current element in the subsequence and update the sum.
        count_with_current = count_subsequence_helper(index + 1, current_sum + arr[index])

        # Exclude the current element from the subsequence.
        count_without_current = count_subsequence_helper(index + 1, current_sum)

        # Return the sum of counts with and without the current element.
        return count_with_current + count_without_current

    # Start the count from index 0 with a current sum of 0.
    return count_subsequence_helper(0, 0)

# Test the function with an example.
arr = [2, 4, 6, 8]
k = 8
count = count_subsequences_with_sum(arr, k)
print("Number of subsequences with sum", k, "is:", count)
