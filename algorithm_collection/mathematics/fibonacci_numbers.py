

def fibonacci_numbers(n):
    assert n >= 0

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)
