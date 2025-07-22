def greedy(value: int, notes: list[int]):
    notes.sort(reverse=True)
    sum = 0
    result = []
    for note in notes:
        while sum + note <= value:
            sum += note
            result.append(note)
    return result


value = 223
notes = [5, 2, 10, 50, 100, 20]


print(greedy(value, notes))
