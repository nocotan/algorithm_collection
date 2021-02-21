

def stooge_sort(arr, l=0, r=-1):
    if r < 0:
        r = len(arr) - 1

    if l >= r:
        return arr

    if arr[l] >= arr[r]:
        t = arr[l]
        arr[l] = arr[r]
        arr[r] = t

    if r - l + 1 > 2:
        t = (r - l + 1) // 3
        arr = stooge_sort(arr, l, r-t)
        arr = stooge_sort(arr, l+t, r)
        arr = stooge_sort(arr, l, r-t)

    return arr
