def find_subsequence_with_sum(arr, k):
    def find_subsequence_helper(index, current_sum, current_seq, found_flag):
        if current_sum == k:
            if not found_flag[0]:
                print(current_seq)
                found_flag[0] = True
            return

        if index == len(arr):
            return

        # Include the current element in the subsequence and update the sum.
        find_subsequence_helper(index + 1, current_sum + arr[index], current_seq + [arr[index]], found_flag)

        # Exclude the current element from the subsequence.
        find_subsequence_helper(index + 1, current_sum, current_seq, found_flag)

    found_flag = [False]  # A flag to track if a valid subsequence has been found.
    find_subsequence_helper(0, 0, [], found_flag)

# Test the function with an example.
arr = [2, 4, 6, 8]
k = 8
find_subsequence_with_sum(arr, k)
