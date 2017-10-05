t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x=101101
    y=n-1
    ans = 0
    checker=True
    while x<=y and checker:
        if str(y)==str(y)[::-1]:
            for i in range(100,1000):
                if y%i==0 and y//i>=100 and y//i<1000:
                    checker = False
                    ans = y
                    break
        y-=1
    print (ans)