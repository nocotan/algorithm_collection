from algorithm_collection.mathematics import gcd


def lcm(a, b):
    if a > b:
        a, b = b, a

    return (a / gcd(a, b)) * b
