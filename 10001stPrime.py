def is_prime(n):
    if n % 2 == 0: return False
    p = 3
    while p < n ** 0.5 + 1:
        if n % p == 0: return False
        p += 2
    return True


def nth_prime(n):
    prime = 2
    count = 1
    iter = 3
    while count < n:
        if is_prime(iter):
            prime = iter
            count += 1
        iter += 2
    return prime


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    prime = nth_prime(n)
    print(prime)