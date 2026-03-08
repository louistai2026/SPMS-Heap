def heapSort(arr):
    n = len(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

arr = [25, 4, 13, 37, 15, 9]
heapSort(arr)
