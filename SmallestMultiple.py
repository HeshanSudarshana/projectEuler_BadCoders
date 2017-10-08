t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i=n
    status = True
    while status:
        for j in range(1,n):
            if i%j!=0:
                i+=n
                break
            if j==n-1:
                status = False
                print(i)