
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in reversed(range(i+1, len(arr))):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr
