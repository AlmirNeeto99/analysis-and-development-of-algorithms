def quick_sort(items: list[int]):
    if len(items) > 1:
        pivot = items[0]
        left = []
        middle = [pivot]
        right = []

        for i in range(1, len(items)):
            item = items[i]
            if item < pivot:
                left.append(item)
            elif item > pivot:
                right.append(item)
            else:
                middle.append(item)

        left = quick_sort(left)
        right = quick_sort(right)
        return left + middle + right
    return items