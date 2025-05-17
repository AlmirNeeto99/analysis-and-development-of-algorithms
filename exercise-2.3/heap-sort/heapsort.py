def get_max(arr, left, right, n):
    if left >= n:
        return n
    if right >= n:
        return left
    return left if arr[left] > arr[right] else right


def max_heapify(arr, i, n):
    c = get_max(arr, 2 * i + 1, 2 * i + 2, n)
    while c < n and arr[i] < arr[c]:
        arr[i], arr[c] = arr[c], arr[i]
        i = c
        c = get_max(arr, 2 * i + 1, 2 * i + 2, n)


def build_max_heap(arr, n):
    for i in range((n - 1) // 2, -1, -1):
        max_heapify(arr, i, n)


def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)
    return arr
