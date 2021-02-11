
def linear_search(arr, key) -> int:
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    return -1
