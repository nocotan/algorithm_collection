

def counting_sort(arr):
    output = [0 for i in range(len(arr))]
    count = [0 for i in range(256)]
    res = [0 for _ in arr]

    for i in arr:
        count[i] += 1

    for i in range(256):
        count[i] += count[i-1]

    for i in range(len(arr)):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    for i in range(len(arr)):
        res[i] = output[i]

    return res
