def solve(l):
    for i in range(len(l)):
        if len(set(list(l[i])))!=1:
            return "NO"
    for i in range(len(l)-1):
        if l[i]==l[i+1]:
            return "NO"
    return "YES"
val=[]
a,b=map(int,input().split())
for i in range(a):
    n=input()
    val.append(n)
print(solve(val))
