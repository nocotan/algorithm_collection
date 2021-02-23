

def exponential_taylor_approximation(x, n):
    res = 1.0
    for i in range(n, 0, -1):
        res = 1 + x * res / i

    return res
