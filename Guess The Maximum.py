def generate_subsequences(lst,n):
    su = []
    for i in range(n):
        for j in range(i + 1, n):
            su.append(lst[i:j + 1])
    return su
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    val=generate_subsequences(l,n)
    a=[]
    for i in val:
        a.append(max(i))
    a.sort()
    print(a[0]-1)
