

def canberra_distance(a, b):
    res = 0
    assert len(a) == len(b)
    for i in range(len(a)):
        res += abs(a[i] - b[i]) / (abs(a[i]) + abs(b[i]))

    return res
