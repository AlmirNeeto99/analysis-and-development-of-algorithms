def is_unique_brute_force(items: list[int]) -> bool:
    list_len = len(items)
    for i in range(list_len - 1):
        for j in range(i + 1, list_len):
            if items[i] == items[j]:
                return False
    return True
