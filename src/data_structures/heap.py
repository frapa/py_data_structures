from __future__ import annotations

from collections.abc import Sequence, Callable
from typing import List


def heap_max(a, b) -> bool:
    return a > b


def heap_min(a, b) -> bool:
    return a < b


class HeapEmptyError(Exception):
    ...


class Heap:
    def __init__(self, cmp: Callable = heap_max):
        self._heap = []
        self._cmp = cmp
        self._size = 0

    @classmethod
    def from_sequence(cls, sequence: Sequence, cmp: Callable = heap_max) -> Heap:
        heap = cls(cmp)
        heap._heap = list(sequence)
        heap._size = len(sequence)
        heap._build_heap()
        return heap

    @staticmethod
    def _left(i: int) -> int:
        return i * 2 + 1

    @staticmethod
    def _right(i: int) -> int:
        return i * 2 + 2

    @staticmethod
    def _parent(i: int) -> int:
        if i == 0:
            return 0
        return (i - 1) // 2

    def size(self) -> int:
        return self._size

    def _valid(self, i: int) -> bool:
        if i >= self.size():
            return False
        return True

    def _swap(self, i: int, j: int):
        temp = self._heap[j]
        self._heap[j] = self._heap[i]
        self._heap[i] = temp

    def _fix_children(self, i: int):
        li = self._left(i)
        ri = self._right(i)

        largest = i
        if self._valid(li) and self._cmp(self._heap[li], self._heap[largest]):
            largest = li

        if self._valid(ri) and self._cmp(self._heap[ri], self._heap[largest]):
            largest = ri

        if largest != i:
            self._swap(i, largest)
            self._fix_children(largest)

    def _build_heap(self):
        for i in reversed(range(self.size() // 2)):
            self._fix_children(i)

    def _fix_parent(self, i: int):
        pi = self._parent(i)
        while self._cmp(self._heap[i], self._heap[pi]):
            self._swap(i, pi)
            i = pi
            pi = self._parent(i)

    def insert(self, value):
        self._heap.append(value)
        self._size += 1
        self._fix_parent(self.size() - 1)

    def peek(self):
        if not self._heap:
            raise HeapEmptyError("The heap is empty, cannot peek.")
        return self._heap[0]

    def pop(self):
        last = self.size() - 1
        self._swap(0, last)
        value = self._heap.pop()
        self._size -= 1
        self._fix_children(0)
        return value

    def heap_sort(self) -> List:
        """This operation makes the heap unusable afterwards."""
        for i in range(self.size()):
            self._swap(0, len(self._heap) - i - 1)
            self._size -= 1
            self._fix_children(0)

        return self._heap
