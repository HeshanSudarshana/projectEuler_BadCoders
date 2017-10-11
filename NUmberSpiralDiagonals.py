t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    n = (n-1)/2
    tot = (8*n*(n+1)*(2*n+1)/3)+2*n*(n+1)+4*n+1
    print(int(tot)%((10**9)+7))