# max_heap.py

class MaxHeap:
    def __init__(self):
        """Initialize an empty max-heap."""
        self.data = []

    def insert(self, x):
        """Insert a new value into the max-heap."""
        self.data.append(x)
        self._sift_up(len(self.data) - 1)

    def extract_max(self):
        """Remove and return the maximum element (root)."""
        if not self.data:
            return None
        self._swap(0, len(self.data) - 1)
        max_val = self.data.pop()
        self._sift_down(0)
        return max_val

    def build_heap(self, arr):
        """Build a max-heap from an array."""
        self.data = arr[:]
        n = len(self.data)
        for i in range((n // 2) - 1, -1, -1):
            self._sift_down(i)

    def _sift_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.data[i] > self.data[parent]:
            self._swap(i, parent)
            i, parent = parent, (parent - 1) // 2

    def _sift_down(self, i):
        n = len(self.data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < n and self.data[left] > self.data[largest]:
                largest = left
            if right < n and self.data[right] > self.data[largest]:
                largest = right
            if largest == i:
                break

            self._swap(i, largest)
            i = largest

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
