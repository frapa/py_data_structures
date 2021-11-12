from pytest import fixture, raises

from src.data_structures.queue import Queue, QueueFullError, QueueEmptyError

_MAX_SIZE = 100
_NUM_ELEMENTS = 50


@fixture
def queue() -> Queue:
    return Queue(_MAX_SIZE)


@fixture
def queue_elements() -> Queue:
    queue = Queue(_MAX_SIZE)
    for i in range(_NUM_ELEMENTS):
        queue.enqueue(i)
    return queue


@fixture
def queue_full() -> Queue:
    queue = Queue(_MAX_SIZE)
    for i in range(_MAX_SIZE):
        queue.enqueue(i)
    return queue


def test_queue_enqueue(queue: Queue):
    assert queue.max_size == _MAX_SIZE
    assert queue._queue == [None] * (_MAX_SIZE + 1)
    for i in range(_NUM_ELEMENTS):
        queue.enqueue(i)
    assert queue._queue == list(range(_NUM_ELEMENTS)) + [None] * (
        _MAX_SIZE - _NUM_ELEMENTS + 1
    )


def test_queue_enqueue_full(queue_full: Queue):
    with raises(QueueFullError):
        queue_full.enqueue(1_000_000)


def test_queue_size(queue: Queue, queue_elements: Queue):
    assert queue.size() == 0
    assert queue_elements.size() == _NUM_ELEMENTS


def test_queue_empty(queue: Queue):
    assert queue.empty() is True
    queue.enqueue(1)
    assert queue.empty() is False
    queue.dequeue()
    assert queue.empty() is True


def test_queue_dequeue(queue_elements: Queue):
    for i in range(_NUM_ELEMENTS):
        assert queue_elements.dequeue() == i


def test_queue_dequeue_empty(queue: Queue):
    with raises(QueueEmptyError):
        queue.dequeue()


def test_queue_peek(queue_elements: Queue):
    assert queue_elements.size() == _NUM_ELEMENTS
    assert queue_elements.peek() == 0
    assert queue_elements.size() == _NUM_ELEMENTS


def test_queue_peek_empty(queue: Queue):
    with raises(QueueEmptyError):
        queue.peek()


def test_queue_circular(queue: Queue):
    """Test that the queue properly handles circularity."""
    size = 0
    for i in range(2 * _MAX_SIZE - 1):  # -1 to avoid queue being full
        queue.enqueue(i)
        size += 1
        if i % 2:
            queue.dequeue()
            size -= 1
        assert queue.size() == size

    with raises(QueueFullError):
        queue.enqueue(1_000_000)
