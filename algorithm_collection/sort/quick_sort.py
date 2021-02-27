def partition(A, start, end):
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[end] = A[end], A[i+1]
    return i+1, A


def quick_sort(A, start=0, end=-1):
    if end < 0:
        end = len(A) - 1
    if start < end:
        pivot_position, A = partition(A, start, end)
        quick_sort(A, start, pivot_position-1)
        quick_sort(A, pivot_position + 1, end)

    return A
