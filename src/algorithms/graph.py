from typing import Set, Literal

from collections.abc import Iterable
from src.data_structures.graph import Node
from src.data_structures.stack import Stack
from src.data_structures.queue import LinkedListQueue


def depth_first(
    start: Node,
    algo: Literal["recursive", "iterative"] = "iterative",
) -> Iterable[Node]:
    if algo == "recursive":
        yield from _depth_first_rec(start)
    else:
        yield from _depth_first_iter(start)


def _depth_first_rec(start: Node, visited: Set[Node] = None) -> Iterable[Node]:
    """Basic recursive version of DF."""
    visited = visited or set()
    yield start
    visited.add(start)

    for node in start.adjacent:
        if node in visited:
            continue

        yield from _depth_first_rec(node, visited)


def _depth_first_iter(start: Node) -> Iterable[Node]:
    """Iterative DF version.

    This is more than 10x faster than the other version.
    """
    stack = Stack()
    stack.insert(start)

    visited = set()
    while not stack.empty():
        node = stack.pop()

        if node in visited:
            continue
        visited.add(node)

        yield node

        # Reversed to keep the same ordering as other function
        for adj_node in reversed(node.adjacent.keys()):
            stack.insert(adj_node)
