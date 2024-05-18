from collections import defaultdict
n=int(input())
l=list(map(int,input().split()))
l1=[]
c=2
ans=0
for i in range(32):
    l1.append(c)
    c*=2
dic=defaultdict(int)
for i in l:
    dic[i]+=1
for i in range(n):
    dic[l[i]]-=1
    for j in l1:
        ans+=dic[j-l[i]]
print(ans)
