

def fibonacci_numbers_space_optimized(n):
    a = 0
    b = 1

    assert n >= 0

    if n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
