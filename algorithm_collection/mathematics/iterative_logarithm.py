import math


def _log(x, base):
    return (int)(math.log(x) / math.log(base))


def iterative_logarithm(n, b):
    if(n > 1.0):
        return 1.0 + iterative_logarithm(_log(n, b), b)
    else:
        return 0
