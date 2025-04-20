def swap(items: list, i: int, j: int) -> None:
    aux = items[i]
    items[i] = items[j]
    items[j] = aux
