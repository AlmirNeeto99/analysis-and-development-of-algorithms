def haore_partition(items: list[int], start: int, pivot_index: int):

    pivot = items[pivot_index]
    right = pivot_index - 1
    left = start

    while left <= right:
        while left <= right and items[left] < pivot:
            left += 1
        while left <= right and items[right] > pivot:
            right -= 1
        if left <= right:
            items[left], items[right] = items[right], items[left]
            left += 1
            right -= 1
    items[left], items[pivot_index] = items[pivot_index], items[left]
    return left  # return the new pivot index
