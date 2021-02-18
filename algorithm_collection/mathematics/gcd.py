

def gcd(a, b):
    if a > b:
        a, b = b, a

    if a == 0:
        return b
    return gcd(b % a, a)
