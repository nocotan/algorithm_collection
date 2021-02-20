

def interpolation_search(arr, key, l=0, r=-1):
    if r < 0:
        r = len(arr) - 1

    if (l <= r and key >= arr[l] and key <= arr[r]):
        pos = l + ((r - l) // (arr[r] - arr[l]) * (key - arr[l]))

        if arr[pos] == key:
            return pos

        if arr[pos] < key:
            return interpolation_search(arr, key, pos+1, r)

        if arr[pos] > key:
            return interpolation_search(arr, key, l, pos-1)

    return -1
