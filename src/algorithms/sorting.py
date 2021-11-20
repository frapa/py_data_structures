from collections.abc import Callable
from typing import Any, Sequence

from src.data_structures.heap import Heap

SortFunction = Callable[[Sequence[Any]], Sequence[Any]]


def insertion_sort(data: Sequence[Any]) -> Sequence[Any]:
    if len(data) <= 1:
        return data

    for i, item in enumerate(data[1:], start=1):
        for j in reversed(range(i)):
            if item < data[j]:
                data[j + 1] = data[j]
                data[j] = item
            else:
                break

    return data


def merge_sort(data: Sequence[Any]) -> Sequence[Any]:
    if len(data) <= 1:
        return data

    len_half = len(data) // 2
    half1 = merge_sort(data[:len_half])
    half2 = merge_sort(data[len_half:])

    result = []
    i1 = 0
    i2 = 0
    while half1 or half2:
        if i1 == len(half1):
            result.extend(half2[i2:])
            break

        if i2 == len(half2):
            result.extend(half1[i1:])
            break

        if half1[i1] <= half2[i2]:
            result.append(half1[i1])
            i1 += 1
        else:
            result.append(half2[i2])
            i2 += 1

    return result


def heap_sort(data: Sequence[Any]) -> Sequence[Any]:
    if len(data) <= 1:
        return data

    heap = Heap.from_sequence(data)
    return heap.heap_sort()


def quick_sort(data: Sequence[Any]) -> Sequence[Any]:
    if len(data) <= 1:
        return data

    data = list(data)
    pivot = data[-1]

    smaller_i = 0
    for i in range(len(data) - 1):
        if data[i] <= pivot:
            temp = data[smaller_i]
            data[smaller_i] = data[i]
            data[i] = temp

            smaller_i += 1

    temp = data[smaller_i]
    data[smaller_i] = pivot
    data[-1] = temp

    data[:smaller_i] = quick_sort(data[:smaller_i])
    data[smaller_i + 1 :] = quick_sort(data[smaller_i + 1 :])

    return data
