class QueueEmptyError(Exception):
    ...


class QueueFullError(Exception):
    ...


class _ArrayQueueBase:
    """Base class for queues, based on arrays."""

    def __init__(self, max_size: int):
        self.max_size = max_size
        self._queue = [None] * (max_size + 1)
        self._left = 0  # Start
        self._right = 0  # Index of next added element

    def _enlargeLeft(self):
        self._left -= 1
        if self._left == -1:
            self._left = self.max_size

    def _enlargeRight(self):
        self._right += 1
        if self._right == self.max_size + 1:
            self._right = 0

    def _shrinkLeft(self):
        self._left += 1
        if self._left == self.max_size + 1:
            self._left = 0

    def _shrinkRight(self):
        self._right -= 1
        if self._right == -1:
            self._right = self.max_size

    def size(self) -> int:
        diff = self._right - self._left

        if self._right < self._left:
            return self.max_size + 1 + diff

        return diff

    def empty(self) -> bool:
        return self.size() == 0

    def full(self) -> bool:
        return self.size() == self.max_size


class Queue(_ArrayQueueBase):
    """Classical circular queue implementation based on arrays."""

    def enqueue(self, value):
        if self.full():
            raise QueueFullError()
        self._queue[self._right] = value
        self._enlargeRight()

    def dequeue(self):
        if self.empty():
            raise QueueEmptyError()
        value = self._queue[self._left]
        self._shrinkLeft()
        return value

    def peek(self):
        if self.empty():
            raise QueueEmptyError()
        return self._queue[self._left]


class Deque(_ArrayQueueBase):
    def enqueueLeft(self, value):
        if self.full():
            raise QueueFullError()
        self._enlargeLeft()
        self._queue[self._left] = value

    def enqueueRight(self, value):
        if self.full():
            raise QueueFullError()
        self._queue[self._right] = value
        self._enlargeRight()

    def dequeueLeft(self):
        if self.empty():
            raise QueueEmptyError()
        value = self._queue[self._left]
        self._shrinkLeft()
        return value

    def dequeueRight(self):
        if self.empty():
            raise QueueEmptyError()
        self._shrinkRight()
        value = self._queue[self._right]
        return value

    def peekLeft(self):
        if self.empty():
            raise QueueEmptyError()
        return self._queue[self._left]

    def peekRight(self):
        if self.empty():
            raise QueueEmptyError()
        return self._queue[self._right]
