import math

def get_variance(data, ci):
    column_data = []

    for ri in range(len(data)):
        if data[ri][ci] >= 0:
            column_data.append(data[ri][ci])

    return calculate_variance(column_data)


def get_variances(data):
    var = []

    for ci in range(len(data[0])):
        var.append(get_variance(data, ci))

    return var
def convert_to_int(data):
    int_data = []

    for ri in range(len(data)):
        int_data.append([])

        for ci in range(len(data[0])):
            int_data[ri].append(int(data[ri][ci]))

    return int_data

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

