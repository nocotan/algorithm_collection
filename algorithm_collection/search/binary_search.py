

def binary_search(arr, key, l=0, r=-1):
    if r == -1:
        r = len(arr) - 1

    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, key, l, mid-1)
        else:
            return binary_search(arr, key, mid+1, r)
    else:
        return -1
