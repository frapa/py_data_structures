from pytest import raises, mark
import numpy as np

from src.data_structures.heap import Heap, HeapEmptyError


def test_heap_peek_error():
    heap = Heap()
    with raises(HeapEmptyError):
        heap.peek()


def test_heap_insert():
    heap = Heap()

    heap.insert(1)
    heap.insert(4)
    heap.insert(5)
    heap.insert(-2)
    heap.insert(3)
    heap.insert(10)

    assert heap.peek() == 10


@mark.parametrize("size", [1000, 10_000, 100_000])
def test_heap_from_sequence(size: int):
    numbers = np.random.randint(0, 1_000_000, (size,))
    heap = Heap.from_sequence(numbers)

    assert heap.peek() == np.max(numbers)
