t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    max = 0
    for i in range(0,n-k):
        temp = 1
        for j in range(i,i+k):
            temp *= int(num[j])
        if max<temp:
            max = temp
    print (max)