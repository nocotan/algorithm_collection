import math


def correlation_coefficient(X, Y):
    n = len(X)
    sum_X = 0
    sum_Y = 0
    sum_XY = 0
    squareSum_X = 0
    squareSum_Y = 0

    i = 0
    while i < n:
        sum_X = sum_X + X[i]
        sum_Y = sum_Y + Y[i]

        sum_XY = sum_XY + X[i] * Y[i]

        squareSum_X = squareSum_X + X[i] * X[i]
        squareSum_Y = squareSum_Y + Y[i] * Y[i]

        i = i + 1

    corr = (float)(n * sum_XY - sum_X * sum_Y) / (float)(math.sqrt((n * squareSum_X - sum_X * sum_X)* (n * squareSum_Y - sum_Y * sum_Y)))

    return corr
