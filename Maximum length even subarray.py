for i in range(int(input())):
    n=int(input())
    val=(n*(n+1))//2
    if val%2==0:
        print(n)
    else:
        print(n-1)
