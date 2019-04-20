#!/bin/python3

import math


def calculate_mean(arr):
    total = 0

    for num in arr:
        total += num

    mean = total / len(arr)

    return mean


def calculate_variance(arr):
    mean = calculate_mean(arr)
    total = 0

    for num in arr:
        total += (num - mean) ** 2

    variance = math.sqrt(total / len(arr))

    return variance


def quick_partition(arr, low, high, indexes=None):
    curr = low - 1
    pivot = arr[high]

    for i in range(low, high):
        if arr[i] <= pivot:
            curr += 1
            arr[i], arr[curr] = arr[curr], arr[i]

            if indexes is not None:
                indexes[i], indexes[curr] = indexes[curr], indexes[i]

    curr += 1
    arr[curr], arr[high] = arr[high], arr[curr]

    if indexes is not None:
        indexes[curr], indexes[high] = indexes[high], indexes[curr]

    return curr


def quick_sort(arr, low=None, high=None, indexes=None, is_ascending=True):
    if (low is None) or (high is None):
        indexes = [i for i in range(0, len(arr))]
        quick_sort(arr, 0, len(arr) - 1, indexes)

        if not is_ascending:
            arr.reverse()
            indexes.reverse()

        return indexes

    if low < high:
        pivot = quick_partition(arr, low, high, indexes)

        quick_sort(arr, low, pivot - 1, indexes)
        quick_sort(arr, pivot + 1, high, indexes)


if __name__ == '__main__':
    data = [10, 2, 8, -3, 20, 1, 4]

    result = quick_sort(data, is_ascending=False)

    print(result)
    print(data)
