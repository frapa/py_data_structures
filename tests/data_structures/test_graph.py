from pytest import mark

from src.data_structures.graph import Node, Graph


@mark.parametrize(
    "params, exp_weight, exp_rev_weight",
    [
        ((), 1, 1),
        ((2,), 2, 2),
        ((2, 3), 2, 3),
    ],
)
def test_edge(params, exp_weight, exp_rev_weight):
    node1 = Node(1)
    assert node1.value == 1

    node2 = Node(2)
    node2.edge(node1, *params)

    assert node2 in node1.adjacent
    assert node1 in node2.adjacent
    assert node2.adjacent[node1] == exp_weight
    assert node1.adjacent[node2] == exp_rev_weight


def test_graph_add_node():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)

    node3 = Node(3)
    graph.add_node(node3, [node1, node2])

    assert node2 in node3.adjacent
    assert node1 in node3.adjacent
    assert node3 in node1.adjacent
    assert node3 in node2.adjacent

    assert set(node1.adjacent.values()) == {1}
    assert set(node2.adjacent.values()) == {1}
    assert set(node3.adjacent.values()) == {1}


def test_graph_add_node_weight():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)

    node3 = Node(3)
    graph.add_node_weights(node3, {node1: 5, node2: (2, 3)})

    assert node2 in node3.adjacent
    assert node1 in node3.adjacent
    assert node3 in node1.adjacent
    assert node3 in node2.adjacent

    assert set(node1.adjacent.values()) == {5}
    assert set(node2.adjacent.values()) == {3}
    assert set(node3.adjacent.values()) == {5, 2}
