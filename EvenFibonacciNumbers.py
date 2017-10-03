t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    tot = 0
    a = 1
    b = 1
    c = 0
    while c<=n:
        c=a+b
        b=a
        a=c
        if c%2==0 and c<=n:
            tot+=c
    print (tot)