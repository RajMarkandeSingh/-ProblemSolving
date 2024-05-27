def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return fact(n-1)*n
for i in range(int(input())):
    n=int(input())
    val=str(fact(n))
    a=[int(i) for i in val]
    print(sum(a))
    
