#!/bin/python

import sys


def ispyth(a,b,c):
    if(a*a+b*b==c*c):
        return True
    return False

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    mx=n
    for a in range(1, n):
        b = n*(n-2*a)/(2*(n-a))
        if(ispyth(a,b,n-a-b) and mx<a*b*(n-a-b)):
            mx = a*b*(n-a-b)
    if(mx==n):
        print -1
    else:
        print mx
