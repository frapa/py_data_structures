from pytest import fixture, raises

from src.data_structures.queue import (
    QueueFullError,
    QueueEmptyError,
    Queue,
    LinkedListQueue,
    Deque,
    LinkedListDeque,
    AnyQueue,
    AnyDeque,
)

_MAX_SIZE = 100
_NUM_ELEMENTS = 50


@fixture(
    params=[Queue, LinkedListQueue],
    ids=["queue", "ll_queue"],
)
def queue(request) -> AnyQueue:
    if request.param == Queue:
        return request.param(_MAX_SIZE)
    else:
        return request.param()


@fixture(
    params=[Queue, LinkedListQueue],
    ids=["queue", "ll_queue"],
)
def queue_elements(request) -> AnyQueue:
    if request.param == Queue:
        queue = request.param(_MAX_SIZE)
    else:
        queue = request.param()

    for i in range(_NUM_ELEMENTS):
        queue.enqueue(i)

    return queue


@fixture
def queue_full() -> Queue:
    queue = Queue(_MAX_SIZE)
    for i in range(_MAX_SIZE):
        queue.enqueue(i)
    return queue


@fixture(
    params=[Deque, LinkedListDeque],
    ids=["deque", "ll_queue"],
)
def deque(request) -> AnyDeque:
    if request.param == Deque:
        return request.param(_MAX_SIZE)
    else:
        return request.param()


def test_queue_enqueue():
    queue = Queue(_MAX_SIZE)
    assert queue.max_size == _MAX_SIZE
    assert queue._queue == [None] * (_MAX_SIZE + 1)
    for i in range(_NUM_ELEMENTS):
        queue.enqueue(i)
    assert queue._queue == list(range(_NUM_ELEMENTS)) + [None] * (
        _MAX_SIZE - _NUM_ELEMENTS + 1
    )


def test_ll_queue_enqueue():
    queue = LinkedListQueue()
    assert queue._head is None
    assert queue._tail is None
    for i in range(_NUM_ELEMENTS):
        queue.enqueue(i)
    assert queue._head != queue._tail


def test_queue_enqueue_full(queue_full: Queue):
    with raises(QueueFullError):
        queue_full.enqueue(1_000_000)


def test_queue_size_initial(queue: AnyQueue):
    assert queue.size() == 0


def test_queue_size(queue_elements: AnyQueue):
    assert queue_elements.size() == _NUM_ELEMENTS


def test_queue_empty(queue: AnyQueue):
    assert queue.empty() is True
    queue.enqueue(1)
    assert queue.empty() is False
    queue.dequeue()
    assert queue.empty() is True


def test_queue_dequeue(queue_elements: AnyQueue):
    for i in range(_NUM_ELEMENTS):
        assert queue_elements.dequeue() == i


def test_queue_dequeue_empty(queue: AnyQueue):
    with raises(QueueEmptyError):
        queue.dequeue()


def test_queue_peek(queue_elements: AnyQueue):
    print(queue_elements)
    assert queue_elements.size() == _NUM_ELEMENTS
    assert queue_elements.peek() == 0
    assert queue_elements.size() == _NUM_ELEMENTS


def test_queue_peek_empty(queue: AnyQueue):
    with raises(QueueEmptyError):
        queue.peek()


def test_queue_circular():
    """Test that the queue properly handles circularity."""
    queue = Queue(_MAX_SIZE)
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

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()


def test_deque_enqueueRight_dequeueLeft(deque: AnyDeque):
    for i in range(_NUM_ELEMENTS):
        deque.enqueueRight(i)
    for i in range(_NUM_ELEMENTS):
        assert deque.dequeueLeft() == i


def test_deque_enqueueRight_dequeueRight(deque: AnyDeque):
    for i in range(_NUM_ELEMENTS):
        deque.enqueueRight(i)
    for i in reversed(range(_NUM_ELEMENTS)):
        assert deque.dequeueRight() == i


def test_deque_enqueueLeft_dequeueLeft(deque: AnyDeque):
    for i in range(_NUM_ELEMENTS):
        deque.enqueueRight(i)
    for i in range(_NUM_ELEMENTS):
        assert deque.dequeueLeft() == i


def test_deque_enqueueLeft_dequeueRight(deque: AnyDeque):
    for i in range(_NUM_ELEMENTS):
        deque.enqueueRight(i)
    for i in reversed(range(_NUM_ELEMENTS)):
        assert deque.dequeueRight() == i


def test_deque_circular():
    """Test that the deque properly handles circularity."""
    deque = Deque(_MAX_SIZE)
    size = 0
    for i in range(2 * _MAX_SIZE - 1):  # -1 to avoid queue being full
        deque.enqueueRight(i)
        size += 1
        if i % 2:
            deque.dequeueLeft()
            size -= 1
        assert deque.size() == size

    with raises(QueueFullError):
        deque.enqueueRight(1_000_000)

    deque.dequeueLeft()
    deque.dequeueLeft()
    deque.dequeueLeft()
    size -= 3

    for i in range(2 * size - 1):  # -1 to avoid queue being empty
        deque.dequeueRight()
        size -= 1
        if i % 2:
            deque.enqueueLeft(i)
            size += 1
        assert deque.size() == size

    with raises(QueueEmptyError):
        deque.dequeueRight()
