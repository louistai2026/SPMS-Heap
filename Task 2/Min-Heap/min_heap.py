# nin_heap.py

class MinHeap:
    def __init__(self):
        """Initialize an empty min-heap."""
        self.data = []

    def insert(self, x):
        """Insert a new value into the min-heap."""
        self.data.append(x)
        self._sift_up(len(self.data) - 1)

    def extract_min(self):
        """Remove and return the minimum element (root)."""
        if not self.data:
            return None
        self._swap(0, len(self.data) - 1)
        min_val = self.data.pop()
        self._sift_down(0)
        return min_val

    def peek(self):
        """Return the minimum element without removing it."""
        return self.data[0] if self.data else None

    def _sift_up(self, i):
        """Move the element at index i up to restore heap property."""
        parent = (i - 1) // 2
        while i > 0 and self.data[i] < self.data[parent]:
            self._swap(i, parent)
            i, parent = parent, (parent - 1) // 2

    def _sift_down(self, i):
        """Move the element at index i down to restore heap property."""
        n = len(self.data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i:
                break

            self._swap(i, smallest)
            i = smallest

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
