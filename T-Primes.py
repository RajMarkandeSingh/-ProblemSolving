import math
 
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
 
t = int(input())
l = list(map(int, input().split()))
 
for n in l:
    if n == 1:
        print("NO")
        continue
    val = int(math.isqrt(n))  # Use integer square root
    if val * val == n and is_prime(val):
        print("YES")
    else:
        print("NO")
