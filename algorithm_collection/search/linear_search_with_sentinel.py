
def linear_search_with_sentinel(arr, key):
    i = 0
    arr.append(key)

    while arr[i] != key:
        i += 1

    if i == len(arr) - 1:
        return -1

    return i
