import math


def prime_factors(n):
    res = []
    while n % 2 == 0:
        res.append(n)
        n /= 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            res.append(i)
            n /= i

    if n > 2:
        res.append(n)

    return res
