n=int(input())
lis=list(map(int,input().split()))
teams=[[],[],[]]
for i in range(n):
    if lis[i]==1:
        teams[0].append(i+1)
    elif lis[i]==2:
        teams[1].append(i+1)
    elif lis[i]==3:
        teams[2].append(i+1)
val=min(len(teams[0]),len(teams[1]),len(teams[2]))
print(val)
for i in range(val):
    print(teams[0][i],teams[1][i],teams[2][i])
