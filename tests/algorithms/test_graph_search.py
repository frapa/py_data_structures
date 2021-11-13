from typing import List, Tuple
from contextlib import nullcontext

from pytest import fixture, mark, raises

from src.data_structures.graph import Node
from src.algorithms.graph_search import depth_first, breadth_first


@fixture
def nodes() -> List[Node]:
    return [None, Node(1), Node(2), Node(3), Node(4), Node(5)]


@fixture
def graph(nodes: List[Node]) -> Node:
    nodes[1].edge(nodes[2])
    nodes[1].edge(nodes[3])
    nodes[2].edge(nodes[5])
    nodes[3].edge(nodes[4])
    nodes[5].edge(nodes[3])
    return nodes[1]


@fixture(params=[1000, 2000, 5000, 10000])
def large_graph(request) -> Tuple[Node, int]:
    nodes = [Node(i) for i in range(request.param)]
    for i, node in enumerate(nodes):
        if i + i < len(nodes):
            node.edge(nodes[i + 1])

    return nodes[0], request.param


@mark.parametrize("algo", ["recursive", "iterative"])
def test_depth_first(algo: str, nodes: List[Node], graph: Node):
    df_values = [node.value for node in depth_first(graph, algo)]
    assert df_values == [1, 2, 5, 3, 4]


@mark.parametrize("algo", ["recursive", "iterative"])
def test_depth_performances(algo: str, large_graph: Node):
    graph, num_nodes = large_graph

    # 1000 is the maximum stack depth in python by default
    if algo == "recursive" and num_nodes > 1000:
        context = raises(RecursionError)
        print("Exception expected!")
    else:
        context = nullcontext()

    with context:
        for _ in depth_first(graph, algo):
            pass


def test_breadth_first(nodes: List[Node], graph: Node):
    df_values = [node.value for node in breadth_first(graph)]
    assert df_values == [1, 2, 3, 5, 4]
