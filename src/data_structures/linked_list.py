from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class SinglyLinkedListItem:
    value: Any
    next: Optional[SinglyLinkedListItem] = None

    def append(self, other: SinglyLinkedListItem):
        self.next = other


@dataclass
class DoublyLinkedListItem:
    value: Any
    prev: Optional[DoublyLinkedListItem] = None
    next: Optional[DoublyLinkedListItem] = None

    def prepend(self, other: DoublyLinkedListItem):
        self.prev = other
        other.next = self

    def append(self, other: DoublyLinkedListItem):
        self.next = other
        other.prev = self
