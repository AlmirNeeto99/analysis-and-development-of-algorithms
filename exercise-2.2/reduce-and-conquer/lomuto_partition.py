def lomuto_partition(
    items: list[int],
    left: int,
    right: int,
):
    pivot = items[right]
    i = left - 1

    for j in range(left, right):
        if items[j] <= pivot:
            i += 1
            items[i], items[j] = items[j], items[i]
    right_place = i + 1
    items[right_place], items[right] = items[right], items[right_place]
    return right_place
