def merge(
    a: list[int],
    b: list[int],
):

    max_len = len(a) + len(b)
    merged = []
    i, j = 0, 0

    while len(merged) < max_len:

        if i >= len(a):
            merged.append(b[j])
            j += 1
        elif j >= len(b):
            merged.append(a[i])
            i += 1
        else:
            if a[i] <= b[j]:
                merged.append(a[i])
                i += 1
            elif b[j] <= a[i]:
                merged.append(b[j])
                j += 1
    return merged


def merge_sort(arr):
    arr_len = len(arr)
    if arr_len != 1:
        size = arr_len // 2
        start = arr[:size]
        end = arr[size:]
        return merge(merge_sort(start), merge_sort(end))
    return arr
