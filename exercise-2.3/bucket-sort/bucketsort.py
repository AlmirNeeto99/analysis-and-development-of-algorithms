def bucketsort(arr: list[int]):
    if len(arr) == 0:
        return arr
    min_value = min(arr)
    max_value = max(arr)
    diff = abs(max_value - min_value)
    if diff == 0:
        return arr
    bucket = [0] * (diff + 1)
    for element in arr:
        index = element - min_value
        bucket[index] += 1
    arr = []
    for i in range(len(bucket)):
        item = bucket[i]
        for _ in range(item):
            arr.append(i + min_value)
    return arr
