for i in range(int(input())):
    n,m=map(int,input().split())
    a=input()
    dic={"A":a.count("A"),"B":a.count("B"),"C":a.count("C"),"D":a.count("D"),"E":a.count("E"),"F":a.count("F"),"G":a.count("G")}
    val=list(dic.values())
    v=0
    for i in val:
        if i<m:
            v+=(m-i)
    print(v)
