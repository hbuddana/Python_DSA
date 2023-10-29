def find_subsequences_with_sum(arr, k):
    def find_subsequences_helper(index, current_sum, current_seq):
        if index == len(arr):
            if current_sum == k:
                print(current_seq)
            return

        # Include the current element in the subsequence and update the sum.
        find_subsequences_helper(index + 1, current_sum + arr[index], current_seq + [arr[index]])

        # Exclude the current element from the subsequence.
        find_subsequences_helper(index + 1, current_sum, current_seq)

    find_subsequences_helper(0, 0, [])

# Test the function with an example.
arr = [2, 4, 6, 8]
k = 8
find_subsequences_with_sum(arr, k)
