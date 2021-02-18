import math


def jump_search(arr, key):
    n = len(arr)
    step = math.sqrt(n)

    prev = 0
    while arr[int(min(step, n) - 1)] < key:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < key:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[int(prev)] == key:
        return int(prev)

    return -1
