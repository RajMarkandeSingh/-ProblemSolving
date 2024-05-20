def sockMerchant(n, ar):
    # Write your code here
    dic={}
    for i in ar:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    val=list(dic.values())
    c=0
    for i in val:
        if i>=2:
            c+=i//2
    return c
