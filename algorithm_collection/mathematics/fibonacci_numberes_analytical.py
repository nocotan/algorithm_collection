import math


def fibonacci_numbers_analytical(n):
    return round(pow((1 + math.sqrt(5)) / 2, n) / math.sqrt(5))
