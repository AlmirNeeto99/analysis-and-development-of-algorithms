def lomuto_partition(items: list[int]):
    s = 0
    pivot = items[0]
    for i in range(1, len(items)):
        if items[i] <= pivot:
            s += 1
            items[i], items[s] = items[s], items[i]
    items[s], items[0] = items[0], items[s]
    return s
