from lomuto_partition import lomuto_partition


def quick_select(items: list[int], left: int, right: int, k: int):
    index = lomuto_partition(items, left, right)
    search = k - 1

    if index == search:
        return items[index]
    else:
        if index > search:
            return quick_select(items, left, index - 1, k)
        else:
            return quick_select(items, index + 1, right, k)
