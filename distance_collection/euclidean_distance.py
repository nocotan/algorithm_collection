

def euclidean_distance(a, b):
    res = 0
    assert len(a) == len(b)

    for i in range(len(a)):
        res += (a[i] - b[i]) ** 2

    return (res)**(1/2)
