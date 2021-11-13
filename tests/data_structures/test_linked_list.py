from src.data_structures.linked_list import SinglyLinkedListItem, DoublyLinkedListItem


def test_single_append():
    ll = SinglyLinkedListItem(1)
    assert ll.value == 1
    assert ll.next is None

    item = SinglyLinkedListItem(2)
    ll.append(item)
    assert ll.next == item


def test_double_append():
    ll = DoublyLinkedListItem(1)
    assert ll.value == 1
    assert ll.prev is None
    assert ll.next is None

    item = DoublyLinkedListItem(2)
    ll.append(item)
    assert ll.prev is None
    assert ll.next == item
    assert item.prev == ll
    assert item.next is None


def test_double_prepend():
    ll = DoublyLinkedListItem(1)
    assert ll.value == 1
    assert ll.prev is None
    assert ll.next is None

    item = DoublyLinkedListItem(2)
    ll.prepend(item)
    assert ll.prev == item
    assert ll.next is None
    assert item.prev is None
    assert item.next == ll
