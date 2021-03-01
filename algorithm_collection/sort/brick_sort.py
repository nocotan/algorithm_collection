

def brick_sort(arr):
    n = len(arr)
    is_sorted = 0
    while is_sorted == 0:
        is_sorted = 1
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = 0

        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = 0

    return arr
