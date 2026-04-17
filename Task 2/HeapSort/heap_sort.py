# heap_sort.py

from max_heap import MaxHeap

class HeapSort:
    def sort(self, arr):
        """Perform heap sort using a Max-Heap."""
        heap = MaxHeap()
        heap.build_heap(arr)

        sorted_arr = []
        while heap.data:
            sorted_arr.append(heap.extract_max())

        # Extracting max gives descending order → reverse for ascending
        return sorted_arr[::-1]
