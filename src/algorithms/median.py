from typing import Union, Iterable

from src.data_structures.heap import Heap, heap_max, heap_min


class RunningMedianComputer:
    def __init__(self):
        self._smaller = Heap(heap_max)
        self._larger = Heap(heap_min)

    def _update(self, value: float):
        self._smaller.insert(value)
        # We only move a value to the _larger heap if
        # the move would balance the heaps, otherwise
        # we keep he _smaller heap larger. This mean
        # that if we have a odd number of elements,
        # _smaller.peek() will give the median.
        if self._smaller.size() > self._larger.size() + 1:
            self._larger.insert(self._smaller.pop())
        # If we do not rebalance, but the inserted element
        # exceeds the minimum in _larger, swap elements.
        elif self._larger.size() and self._smaller.peek() > self._larger.peek():
            self._larger.insert(self._smaller.pop())
            self._smaller.insert(self._larger.pop())

    def update(self, value: Union[float, Iterable[float]]):
        if isinstance(value, (float, int)):
            return self._update(value)

        for v in value:
            self._update(v)

    def median(self) -> float:
        if self._smaller.size() > self._larger.size():
            return self._smaller.peek()

        return (self._smaller.peek() + self._larger.peek()) / 2
