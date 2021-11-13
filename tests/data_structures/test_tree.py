from src.data_structures.tree import Node, BinaryNode


def test_node_add_child():
    parent = Node(1)
    child = Node(2)

    parent.add_child(child)

    assert child.parent == parent
    assert parent.children == [child]


def test_node_replace_child():
    parent = Node(1)
    child1 = Node(21)
    child3 = Node(23)

    parent.add_child(child1)
    child2 = parent.add_child(22)
    parent.replace_child(0, child3)

    assert child1.parent is None
    assert child2.parent == parent
    assert child3.parent == parent
    assert parent.children == [child3, child2]


def test_binary_node_set_left():
    parent = BinaryNode(1)
    left1 = BinaryNode(2)

    parent.set_left(left1)

    assert parent.left == left1
    assert parent.right is None
    assert left1.parent == parent

    left2 = parent.set_left(3)

    assert parent.left == left2
    assert parent.right is None
    assert left2.parent == parent

    # left1 was properly reset
    assert left1.parent is None


def test_binary_node_set_right():
    parent = BinaryNode(1)
    right1 = BinaryNode(2)

    parent.set_right(right1)

    assert parent.right == right1
    assert parent.left is None
    assert right1.parent == parent

    right2 = parent.set_right(3)

    assert parent.right == right2
    assert parent.left is None
    assert right2.parent == parent

    # right1 was properly reset
    assert right1.parent is None
