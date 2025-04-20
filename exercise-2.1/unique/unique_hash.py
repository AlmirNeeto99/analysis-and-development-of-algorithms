def unique_hashing(items: list[int]) -> bool:
    hash = set()
    for item in items:
        if item not in hash:
            hash.add(item)
        else:
            return False
    return True
