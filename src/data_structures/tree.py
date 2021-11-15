from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, List, Optional, Dict


@dataclass
class Node:
    value: Any
    # Leave empty if tree has no parent link
    parent: Optional[Node] = None
    children: List[Node] = field(default_factory=list)
    # Can be used to implement stuff like red-black trees
    attrs: Dict[str, Any] = field(default_factory=dict)

    @staticmethod
    def _normalize_node(node: Any) -> Node:
        if isinstance(node, Node):
            return node
        return Node(node)

    def add_child(self, child: Any) -> Node:
        child = self._normalize_node(child)
        child.parent = self
        self.children.append(child)
        return child

    def replace_child(self, i: int, child: Any) -> Node:
        self.children[i].parent = None

        child = self._normalize_node(child)
        child.parent = self
        self.children[i] = child
        return child


@dataclass
class BinaryNode:
    value: Any
    # Leave empty if tree has no parent link
    parent: Optional[BinaryNode] = None
    left: Optional[BinaryNode] = None
    right: Optional[BinaryNode] = None
    # Can be used to implement stuff like red-black trees
    attrs: Dict[str, Any] = field(default_factory=dict)

    @staticmethod
    def _normalize_node(node: Any) -> BinaryNode:
        if isinstance(node, BinaryNode):
            return node
        return BinaryNode(node)

    def set_left(self, left: Any) -> BinaryNode:
        if self.left:
            self.left.parent = None
        self.left = self._normalize_node(left)
        self.left.parent = self
        return self.left

    def set_right(self, right: Any) -> BinaryNode:
        if self.right:
            self.right.parent = None
        self.right = self._normalize_node(right)
        self.right.parent = self
        return self.right
