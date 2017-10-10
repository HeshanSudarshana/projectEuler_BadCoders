t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    i = 2
    j = 3
    count = 4
    num = str(j)
    while len(num)<n:
        temp = j
        j = i + j
        i = temp
        num = str(j)
        count+=1
    print(count)