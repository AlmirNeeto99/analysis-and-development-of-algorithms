import heapq


def heapsort(arr):
    heapq.heapify(arr)
    sorted_array = []
    while arr:
        sorted_array.append(heapq.heappop(arr))
    return sorted_array
