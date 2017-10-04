t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n = n-1
    num = n//15
    if num>0:
        tot = 7*15*(num-1)*num//2+60*(num)
    else:
        tot = 0
    if n%15>=12:
        tot+=6*15*num+45
    elif n%15>=10:
        tot+=5*15*num+33
    elif n%15>=9:
        tot+=4*15*num+23
    elif n%15>=6:
        tot+=3*15*num+14
    elif n%15>=5:
        tot+=2*15*num+8
    elif n%15>=3:
        tot+=1*15*num+3
    print(tot)