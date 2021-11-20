import time
from copy import deepcopy
from typing import Sequence

import numpy
import pytest

from src.algorithms.sorting import (
    SortFunction,
    insertion_sort,
    merge_sort,
    heap_sort,
    quick_sort,
)


@pytest.mark.parametrize(
    "data",
    [
        [],
        [1],
        [4, 5, 2, 7, -1],
        list(numpy.random.randint(0, 1_000_000, 100)),
        list(numpy.random.randint(0, 1_000_000, 1000)),
        list(numpy.random.randint(0, 1_000_000, 10_000)),
    ],
)
@pytest.mark.parametrize(
    "algorithm",
    [
        insertion_sort,
        merge_sort,
        heap_sort,
        quick_sort,
    ],
)
def test_sort(
    algorithm: SortFunction,
    data: Sequence[int],
) -> None:
    copy = deepcopy(data)

    start = time.perf_counter()
    result = algorithm(copy)
    print(algorithm.__name__, time.perf_counter() - start)

    assert result == sorted(data)


# Expected :[-1, 2, 4, 5, 7]
# Actual   :[-1, 5, 2, 7, 4]
