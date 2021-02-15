import numpy as np


def bogo_sort(arr):
    while (not is_sorted(arr)):
        np.random.shuffle(arr)

    return arr


def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            return False
    return True
