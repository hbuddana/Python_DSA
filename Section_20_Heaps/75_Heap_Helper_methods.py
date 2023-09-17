class MaxHeap:
    def __init__(self):
        # Initialize an empty list to represent the Max Heap.
        self.heap = []

    def _left_child(self, index):
        # Calculate the index of the left child of a node at 'index'.
        return 2 * index + 1
    
    def _right_child(self, index):
        # Calculate the index of the right child of a node at 'index'.
        return 2 * index + 2
    
    def _parent(self, index):
        # Calculate the index of the parent of a node at 'index'.
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        # Swap the elements at index1 and index2 in the heap.
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

# The MaxHeap class provides a basic framework for creating and manipulating a Max Heap.
# Max Heaps are a type of binary heap data structure where the parent node has a greater
# value than its children, ensuring that the maximum element is always at the root.
