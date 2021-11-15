import time
import numpy as np

from src.algorithms.median import RunningMedianComputer


def test_median_simple():
    comp = RunningMedianComputer()

    comp.update(1)
    assert comp.median() == 1

    comp.update(3)
    assert comp.median() == 2

    comp.update([4])

    comp.update([5, -1])
    assert comp.median() == 3


def test_running_median():
    total_computer = 0

    comp = RunningMedianComputer()

    values = []
    for i in range(100):
        new = np.random.randint(0, 1_000_000, (i + 1,))

        start = time.process_time()
        comp.update(float(new[0]) if i == 0 else map(float, new))
        total_computer += time.process_time() - start

        values.extend(new)

        assert comp.median() == np.median(values)

    start = time.process_time()
    comp.median()
    comp_computer = start - time.process_time()

    start = time.process_time()
    np.median(values)
    comp_numpy = start - time.process_time()

    print("Total:", total_computer)
    print("Comp:", comp_computer)
    print("Numpy:", comp_numpy)
