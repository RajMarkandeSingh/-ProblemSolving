import sys

import math
def isprime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while(i*i<=n):
        if (n%i==0) or n%(i+2)==0:
            return False
        i+=6
    return True
t = int(input().strip())
for a0 in range(t):
    n=int(input())
    s=0
    for i in range(n+1):
        if isprime(i):
            s+=i
    print(s)
        
        
