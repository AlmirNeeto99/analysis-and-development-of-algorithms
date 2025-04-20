def is_unique_sort(items: list[int]) -> bool:
    items.sort()
    for i in range(len(items) - 1):
        if items[i] == items[i + 1]:
            return False
    return True
