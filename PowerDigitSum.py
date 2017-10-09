t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    num = 2**n
    Num = str(num)
    tot = 0
    for j in range(len(Num)):
        tot+=int(Num[j])
    print(tot)