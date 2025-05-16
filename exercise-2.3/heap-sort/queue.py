class Queue:

    items = []

    def __init__(self):
        self.items = []

    def add(self, item: int) -> None:
        self.items.append(item)
        current_index = len(self.items) - 1
        parent = (current_index - 1) // 2
        if parent < 0:
            return
        while self.items[parent] < self.items[current_index]:
            self.items[parent], self.items[current_index] = (
                self.items[current_index],
                self.items[parent],
            )
            current_index = parent
            parent = (current_index - 1) // 2
            if current_index == 0 or parent < 0:
                break

    def remove(self) -> int:
        if self.size() == 0:
            raise Exception("Queue is empty")
        if self.size() == 1:
            return self.items.pop()
        current_root = self.items[0]
        last = self.items.pop()
        self.items[0] = last
        index = 0
        array_len = len(self.items)
        while index < array_len:
            left = 2 * index + 1
            right = 2 * index + 2

            if left < array_len and right < array_len:
                if (
                    self.items[left] >= self.items[right]
                    and self.items[left] >= self.items[index]
                ):
                    self.items[left], self.items[index] = (
                        self.items[index],
                        self.items[left],
                    )
                    index = left
                elif (
                    self.items[right] > self.items[left]
                    and self.items[right] > self.items[index]
                ):
                    self.items[right], self.items[index] = (
                        self.items[index],
                        self.items[right],
                    )
                    index = right
                else:
                    break
            elif left < array_len and self.items[left] >= self.items[index]:
                self.items[left], self.items[index] = (
                    self.items[index],
                    self.items[left],
                )
                index = left
            elif right < array_len and self.items[right] > self.items[index]:
                self.items[right], self.items[index] = (
                    self.items[index],
                    self.items[right],
                )
                index = right
            else:
                break
        return current_root

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> None | int:
        if self.is_empty():
            return None
        return self.items[0]
