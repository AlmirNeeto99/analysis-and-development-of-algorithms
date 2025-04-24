def insertionSort(items: list[int]):
    len_items = len(items)
    for i in range(1, len_items):
        j = i
        while j > 0 and items[j] < items[j - 1]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1
