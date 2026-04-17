# priority_queue.py

from max_heap import MaxHeap

class PriorityQueue:
    def __init__(self):
        """Priority Queue implemented using a Max-Heap."""
        self.heap = MaxHeap()

    def insert(self, x):
        """Insert a new element with priority x."""
        self.heap.insert(x)

    def maximum(self):
        """Return the maximum priority element."""
        return self.heap.peek()

    def extract_max(self):
        """Remove and return the element with highest priority."""
        return self.heap.extract_max()

    def increase_key(self, i, new_key):
        """Increase the priority of element at index i."""
        self.heap.increase_key(i, new_key)

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.heap.data) == 0
