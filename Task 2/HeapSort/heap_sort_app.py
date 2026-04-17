# heap_sort_app.py

from heap_sort import HeapSort

class HeapSortApp:
    def __init__(self):
        self.hs = HeapSort()

    def run(self):
        print("=== Heap Sort Program (Using Max-Heap) ===")
        print("Enter numbers separated by spaces:")
        user_input = input("Values: ")

        try:
            arr = list(map(int, user_input.split()))
        except ValueError:
            print("Invalid input. Please enter integers only.")
            return

        sorted_arr = self.hs.sort(arr)

        print("\nOriginal array:", arr)
        print("Sorted array:", sorted_arr)
