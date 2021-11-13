from typing import Optional, Union

from src.data_structures.linked_list import DoublyLinkedListItem


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

    def size(self) -> int:
        diff = self._right - self._left

        if self._right < self._left:
            return self.max_size + 1 + diff

        return diff

    def empty(self) -> bool:
        return self.size() == 0

    def full(self) -> bool:
        return self.size() == self.max_size

    def _increase(self, attr: str):
        value = getattr(self, attr)
        if value == self.max_size:
            setattr(self, attr, 0)
        else:
            setattr(self, attr, value + 1)

    def _enqueue(self, enlarge, value):
        if self.full():
            raise QueueFullError()
        self._queue[self._right] = value
        enlarge()

    def _dequeue(self, shrink):
        if self.empty():
            raise QueueEmptyError()
        value = self._queue[self._left]
        shrink()
        return value

    def _peek(self):
        if self.empty():
            raise QueueEmptyError()
        return self._queue[self._left]


class _LinkedListQueueBase:
    def __init__(self):
        # Cache size because for linked list otherwise
        # it's a O(n) operation to compute it
        self._size = 0
        self._head: Optional[DoublyLinkedListItem] = None
        self._tail: Optional[DoublyLinkedListItem] = None

    def size(self) -> int:
        return self._size

    def empty(self) -> bool:
        return self.size() == 0

    def _enqueue(self, value):
        if self._tail is None:
            self._head = DoublyLinkedListItem(value)
            self._tail = self._head
        else:
            node = DoublyLinkedListItem(value)
            self._tail.append(node)
            self._tail = node
        self._size += 1

    def _dequeue(self):
        if self.empty():
            raise QueueEmptyError()

        value = self._head.value
        self._head = self._head.next

        if self._head is None:
            self._tail = None

        self._size -= 1

        return value

    def _peek(self):
        if self.empty():
            raise QueueEmptyError()
        return self._head.value


class Queue(_ArrayQueueBase):
    """Classical circular queue implementation based on arrays."""

    def _enlarge(self):
        self._increase("_right")

    def _shrink(self):
        self._increase("_left")

    def enqueue(self, value):
        self._enqueue(self._enlarge, value)

    def dequeue(self):
        return self._dequeue(self._shrink)

    def peek(self):
        return self._peek()


class LinkedListQueue(_LinkedListQueueBase):
    """Classical circular queue implementation based on linked lists."""

    def enqueue(self, value):
        self._enqueue(value)

    def dequeue(self):
        return self._dequeue()

    def peek(self):
        return self._peek()


class Deque(_ArrayQueueBase):
    """Deque implementation. It's like a queue but can be
    read and written from both sides.
    """

    def _decrease(self, attr):
        value = getattr(self, attr)
        if value == 0:
            setattr(self, attr, self.max_size)
        else:
            setattr(self, attr, value - 1)

    def _enlargeLeft(self):
        self._decrease("_left")

    def _enlargeRight(self):
        self._increase("_right")

    def _shrinkLeft(self):
        self._increase("_left")

    def _shrinkRight(self):
        self._decrease("_right")

    def enqueueLeft(self, value):
        if self.full():
            raise QueueFullError()
        self._enlargeLeft()
        self._queue[self._left] = value

    def enqueueRight(self, value):
        self._enqueue(self._enlargeRight, value)

    def dequeueLeft(self):
        return self._dequeue(self._shrinkLeft)

    def dequeueRight(self):
        if self.empty():
            raise QueueEmptyError()
        self._shrinkRight()
        value = self._queue[self._right]
        return value

    def peekLeft(self):
        return self._peek()

    def peekRight(self):
        if self.empty():
            raise QueueEmptyError()
        return self._queue[self._right]


class LinkedListDeque(_LinkedListQueueBase):
    """Deque implementation based on linked lists."""

    def enqueueLeft(self, value):
        if self._tail is None:
            self._head = DoublyLinkedListItem(value)
            self._tail = self._head
        else:
            node = DoublyLinkedListItem(value)
            self._head.prepend(node)
            self._head = node
        self._size += 1

    def enqueueRight(self, value):
        self._enqueue(value)

    def dequeueLeft(self):
        return self._dequeue()

    def dequeueRight(self):
        if self.empty():
            raise QueueEmptyError()

        value = self._tail.value
        self._tail = self._tail.prev

        if self._tail is None:
            self._head = None

        self._size -= 1

        return value

    def peekLeft(self):
        return self._peek()

    def peekRight(self):
        if self.empty():
            raise QueueEmptyError()
        return self._tail.value


AnyQueue = Union[Queue, LinkedListQueue]
AnyDeque = Union[Deque, LinkedListDeque]
