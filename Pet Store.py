for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if n%2!=0:
        print("NO")
    else:
        dic={}
        for i in l:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        ans=list(dic.values())
        f=0
        for i in ans:
            if i%2!=0:
                f=1
                break
        if f==0:
            print("YES")
        else:
            print("NO")
