from algorithm_collection.search import binary_search


def exponential_search(arr, key):
    n = len(arr)
    if arr[0] == key:
        return 0

    i = 1
    while i < n and arr[i] <= key:
        i = i * 2

    return binary_search(arr, key, i // 2, min(i, n-1))
