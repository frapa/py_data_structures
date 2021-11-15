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


def test_heap_size():
    heap = Heap()

    assert heap.size() == 0

    for _ in range(57):
        heap.insert(1)

    assert heap.size() == 57


@mark.parametrize("size", [1000, 10_000, 100_000])
def test_heap_from_sequence(size: int):
    numbers = np.random.randint(0, 1_000_000, (size,))
    heap = Heap.from_sequence(numbers)

    assert heap.peek() == np.max(numbers)


def test_heap_pop():
    heap = Heap()

    heap.insert(1)
    heap.insert(4)
    heap.insert(5)
    heap.insert(-2)
    heap.insert(3)
    heap.insert(10)

    assert heap.pop() == 10
    assert heap.pop() == 5
    assert heap.pop() == 4
    assert heap.pop() == 3

    assert heap.peek() == 1
    assert heap.size() == 2
