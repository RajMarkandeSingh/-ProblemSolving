n=int(input())
c=0
for i in range(n):
    lis=list(map(int,input().split()))
    s=sum(lis)
    if s>=2:
        c+=1
print(c)
