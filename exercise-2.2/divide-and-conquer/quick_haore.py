from haore_partition import haore_partition


def quick_haore(items: list[int], start: int, pivot_index: int):

    if start < pivot_index:
        split_index = haore_partition(items, start, pivot_index)

        quick_haore(items, start, split_index - 1)
        quick_haore(items, split_index + 1, pivot_index)
