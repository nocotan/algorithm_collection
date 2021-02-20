

def iterative_merge_sort(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr) // 2
    left = iterative_merge_sort(arr[:middle])
    right = iterative_merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result
