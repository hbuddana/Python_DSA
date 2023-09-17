def insert(self, value):
    # Append the new value to the end of the heap.
    self.heap.append(value)
    current = len(self.heap) - 1  # Set 'current' to the index of the newly added element.

    # While the 'current' element is not the root (index 0) and its value is greater than its parent's value,
    # swap the 'current' element with its parent to maintain the Max Heap property.
    while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
        self._swap(current, self._parent(current))  # Swap the 'current' element with its parent.
        current = self._parent(current)  # Update 'current' to be its parent's index.

# The 'insert' method adds a new value to the Max Heap and then performs a 'heapify-up' operation,
# ensuring that the Max Heap property is maintained. This involves comparing the newly inserted
# element with its parent and moving it up the tree as needed until the Max Heap property is satisfied.
