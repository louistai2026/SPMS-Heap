# max_heap_app.py

from max_heap import MaxHeap

class MaxHeapApp:
    def __init__(self):
        self.heap = MaxHeap()

    def run(self):
        print("=== Max-Heap Program ===")
        print("Enter numbers separated by spaces:")
        user_input = input("Values: ")

        try:
            values = list(map(int, user_input.split()))
        except ValueError:
            print("Invalid input. Please enter integers only.")
            return

        for v in values:
            self.heap.insert(v)

        print("\nHeap array after insertions:", self.heap.data)
        max_val = self.heap.extract_max()
        print("Maximum value extracted:", max_val)

        print("Heap array after extraction:", self.heap.data)
