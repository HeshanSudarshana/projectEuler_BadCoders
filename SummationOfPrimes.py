def is_prime(n):
    if n % 2 == 0: return False
    p = 3
    while p < n ** 0.5 + 1:
        if n % p == 0: return False
        p += 2
    return True


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 5
    tot = 5
    while i<=n:
        if is_prime(i):
            tot+=i
        i+=2
    print(tot)