

def sieve_of_eratosthenes_optimized(n):
    MAX_SIZE = 1000001
    is_prime = [True] * MAX_SIZE
    prime = []
    SPF = [None] * MAX_SIZE

    is_prime[0] = is_prime[1] = False
    for i in range(2, n):
        if is_prime[i]:
            prime.append(i)
            SPF[i] = i

        j = 0
        while (j < len(prime)) and (i * prime[j] < n) and (prime[j] <= SPF[i]):
            is_prime[i * prime[j]] = False
            SPF[i * prime[j]] = prime[j]
            j += 1

    return prime
