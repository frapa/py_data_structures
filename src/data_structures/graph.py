"""Graph implementation using adjacency lists."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, Set, Optional, Union, Tuple
from collections.abc import Iterable


@dataclass
class Node:
    """This class can be used standalone or with a Graph
    (if fast access to the list of all nodes is required)
    """

    value: Any
    # Maps edge to weight
    adjacent: Dict[Node, int] = field(default_factory=dict)

    def edge(self, other: Node, weight: int = 1, rev_weight: Optional[int] = None):
        """Don't forget to call Graph.add_node() if you are using a Graph class."""
        self.adjacent[other] = weight
        other.adjacent[self] = weight if rev_weight is None else rev_weight

    def __hash__(self) -> int:
        """Every node is unique, we cannot have node equality."""
        return id(self)


@dataclass
class Graph:
    nodes: Set[Node] = field(default_factory=set)

    @staticmethod
    def _normalize_node(node: Any) -> Node:
        if isinstance(node, Node):
            return node
        return Node(node)

    def add_node(self, node: Any, adjacent: Iterable[Node] = ()) -> Node:
        node = self._normalize_node(node)
        self.nodes.add(node)
        for adj_node in adjacent:
            node.edge(adj_node)
        return node

    def add_node_weights(
        self,
        node: Any,
        adjacent: Dict[Node, Union[int, Tuple[int, int]]] = (),
    ) -> Node:
        node = self._normalize_node(node)
        self.nodes.add(node)
        for adj_node, weight in adjacent.items():
            if isinstance(weight, tuple):
                node.edge(adj_node, *weight)
            else:
                node.edge(adj_node, weight)
        return node
