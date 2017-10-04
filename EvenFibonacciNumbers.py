t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    num = 2
    prev = 1
    tot = 0
    while num <= n:
        if num % 2 == 0:
            tot += num
        temp = prev
        prev = num
        num = prev + temp
    print(tot)