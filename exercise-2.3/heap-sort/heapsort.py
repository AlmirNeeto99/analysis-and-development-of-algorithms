def get_max(arr, left, right):
    arr_len = len(arr)
    if left >= arr_len or right >= arr_len:
        return -1

    if arr[left] >= arr[right]:
        return left
    return right


def max_heapify(arr, n, i):
    c = get_max(arr, 2 * i + 1, 2 * i + 2)
    while c != -1 and c < len(arr) and arr[c] > arr[i]:
        arr[i], arr[c] = arr[c], arr[i]
        i = c
        c = get_max(arr, 2 * i + 1, 2 * i + 2)


def build_max_heap(arr):
    pass


def heapsort(arr):
    pass
