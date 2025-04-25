def quick_lomuto(items: list[int], left: int, right: int):

    if left < right:
        split_index = lomuto_partition(items, left, right)

        quick_lomuto(items, left, split_index - 1)
        quick_lomuto(items, split_index + 1, right)

    return items
