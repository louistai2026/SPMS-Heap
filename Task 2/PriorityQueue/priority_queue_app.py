# priority_queue_app.py

from priority_queue import PriorityQueue

class PriorityQueueApp:
    def __init__(self):
        self.pq = PriorityQueue()

    def run(self):
        print("=== Priority Queue (Max-Heap) ===")
        print("Enter numbers separated by spaces:")
        user_input = input("Values: ")

        try:
            values = list(map(int, user_input.split()))
        except ValueError:
            print("Invalid input. Please enter integers only.")
            return

        for v in values:
            self.pq.insert(v)

        print("\nInternal heap array:", self.pq.heap.data)
        print("Maximum element:", self.pq.maximum())
        max_val = self.pq.extract_max()
        print("Extracted:", max_val)

        print("Heap after extraction:", self.pq.heap.data)
