

def sieve_of_sundaram(n):
    res = []
    if n > 2:
        res.append(2)

    n = int((n - 1) / 2)
    table = [0] * (n + 1)

    for i in range(1, n + 1):
        j = i
        while (i + j + 2 * i * j) <= n:
            table[i + j + 2 * i * j] = 1
            j += 1

    for i in range(1, n + 1):
        if table[i] == 0:
            res.append((2 * i + 1))

    return res
