def _sink_down(self, index):
    max_index = index  # Initialize the 'max_index' to the given 'index'.
    
    while True:
        left_index = self._left_child(index)
        right_index = self._right_child(index)

        # Compare the value at 'left_index' with the value at 'max_index'.
        if (left_index < len(self.heap) and
                self.heap[left_index] > self.heap[max_index]):
            max_index = left_index

        # Compare the value at 'right_index' with the value at 'max_index'.
        if (right_index < len(self.heap) and
                self.heap[right_index] > self.heap[max_index]):
            max_index = right_index

        # If 'max_index' is not equal to the original 'index', swap the elements
        # to maintain the Max Heap property and update the 'index' to 'max_index'.
        if max_index != index:
            self._swap(index, max_index)
            index = max_index
        else:
            return

# The '_sink_down' method is used to maintain the Max Heap property by moving a
# misplaced element down the heap as needed. It compares the element at the given
# 'index' with its children and swaps it with the maximum of its children if necessary.
