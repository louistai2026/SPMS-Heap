# min_heap_app.py

from min_heap import MinHeap

class MinHeapApp:
    def __init__(self):
        self.heap = MinHeap()

    def run(self):
        print("=== Min-Heap Program ===")
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
        min_val = self.heap.extract_min()
        print("Minimum value extracted:", min_val)

        print("Heap array after extraction:", self.heap.data)
