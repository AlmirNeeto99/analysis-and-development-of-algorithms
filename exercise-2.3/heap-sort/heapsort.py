def get_max(arr, left, right):
    arr_len = len(arr)
    if left >= arr_len:
        return arr_len
    if right >= arr_len:
        return left
    if arr[left] >= arr[right]:
        return left
    return right


def max_heapify(arr, size, i):
    c = get_max(arr, 2 * i + 1, 2 * i + 2)
    while c < size and arr[c] > arr[i]:
        arr[i], arr[c] = arr[c], arr[i]
        i = c
        c = get_max(arr, 2 * i + 1, 2 * i + 2)


def build_max_heap(arr):
    arr_len = len(arr)
    for i in range(arr_len // 2 - 1, -1, -1):
        max_heapify(arr, arr_len, i)


def heapsort(arr):
    pass
