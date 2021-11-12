class QueueEmptyError(Exception):
    ...


class QueueFullError(Exception):
    ...


class Queue:
    """Classical circular queue implementation."""

    def __init__(self, max_size: int):
        self.max_size = max_size
        self._queue = [None] * (max_size + 1)
        self._left = 0
        self._right = 0

    def _enlarge(self):
        self._right += 1
        if self._right == self.max_size + 1:
            self._right = 0

    def _shrink(self):
        self._left += 1
        if self._left == self.max_size + 1:
            self._left = 0

    def size(self) -> int:
        diff = self._right - self._left

        if self._right < self._left:
            return self.max_size + 1 + diff

        return diff

    def empty(self) -> bool:
        return self.size() == 0

    def full(self) -> bool:
        return self.size() == self.max_size

    def enqueue(self, value):
        if self.full():
            raise QueueFullError()
        self._queue[self._right] = value
        self._enlarge()

    def dequeue(self):
        if self.empty():
            raise QueueEmptyError()
        value = self._queue[self._left]
        self._shrink()
        return value

    def peek(self):
        if self.empty():
            raise QueueEmptyError()
        return self._queue[self._left]
