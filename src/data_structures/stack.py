"""This is a ridiculous file, you can use a list instead of this class!"""


class StackEmptyError(Exception):
    ...


class Stack:
    def __init__(self):
        self._stack = []

    def size(self) -> int:
        return len(self._stack)

    def empty(self) -> bool:
        return not self._stack

    def insert(self, value):
        self._stack.append(value)

    def pop(self):
        if self.size() == 0:
            raise StackEmptyError()
        return self._stack.pop()

    def peek(self):
        if self.size() == 0:
            raise StackEmptyError()
        return self._stack[-1]
