from __future__ import annotations

from collections.abc import Sequence, Callable


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

    @classmethod
    def from_sequence(cls, sequence: Sequence) -> Heap:
        heap = cls()
        heap._heap = list(sequence)
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

    def _valid(self, i: int) -> bool:
        if i >= len(self._heap):
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
        for i in reversed(range(len(self._heap) // 2)):
            self._fix_children(i)

    def _fix_parent(self, i: int):
        pi = self._parent(i)
        while self._cmp(self._heap[i], self._heap[pi]):
            self._swap(i, pi)
            i = pi
            pi = self._parent(i)

    def insert(self, value):
        self._heap.append(value)
        self._fix_parent(len(self._heap) - 1)

    def peek(self):
        if not self._heap:
            raise HeapEmptyError("The heap is empty, cannot peek.")
        return self._heap[0]
