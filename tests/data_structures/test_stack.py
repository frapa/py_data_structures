from pytest import fixture

from src.data_structures.stack import Stack

_NUM_ELEMENTS = 1000


def test_stack_insert():
    stack = Stack()
    for i in range(_NUM_ELEMENTS):
        stack.insert(i)


def test_stack_empty():
    stack = Stack()
    assert stack.empty() is True
    stack.insert(1)
    assert stack.empty() is False


@fixture
def stack() -> Stack:
    stack = Stack()
    for i in range(_NUM_ELEMENTS):
        stack.insert(i)
    return stack


def test_stack_size(stack: Stack):
    assert stack.size() == _NUM_ELEMENTS

    stack = Stack()
    assert stack.size() == 0


def test_stack_pop(stack: Stack):
    assert stack.size() == _NUM_ELEMENTS
    for i in range(_NUM_ELEMENTS - 1, -1, -1):
        assert stack.pop() == i
    assert stack.size() == 0


def test_stack_peek(stack: Stack):
    assert stack.size() == _NUM_ELEMENTS
    assert stack.peek() == _NUM_ELEMENTS - 1
    assert stack.size() == _NUM_ELEMENTS
