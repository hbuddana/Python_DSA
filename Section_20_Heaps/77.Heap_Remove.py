def remove(self):
    # Check if the heap is empty. If so, return None.
    if len(self.heap) == 0:
        return None
    
    # If there's only one element in the heap, remove and return it.
    if len(self.heap) == 1:
        return self.heap.pop()
    
    # Store the maximum value (root of the Max Heap) in a variable.
    max_value = self.heap[0]
    
    # Replace the root with the last element in the heap and remove the last element.
    self.heap[0] = self.heap.pop()
    
    # Perform a "heapify-down" operation to maintain the Max Heap property.
    self._sink_down(0)

    # Return the maximum value that was removed.
    return max_value

# The 'remove' method is used to remove the maximum value (root) from the Max Heap.
# It ensures that the Max Heap property is maintained by replacing the root with the last element
# in the heap and then performing a "heapify-down" operation, which involves comparing the
# root with its children and moving it down the tree as needed until the Max Heap property is satisfied.
