from queue import Queue


def heap_sort_not_in_place(arr):
    max_heap = Queue()

    for element in arr:
        max_heap.add(element)
    sorted_array = [0] * len(arr)
    for i in range(len(arr), 0, -1):
        sorted_array[i - 1] = max_heap.remove()
    return sorted_array
