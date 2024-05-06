t="hello"
def counthelllo():
    j=0
    name=input()
    for i in range(len(name)):
        if name[i]==t[j]:
            j+=1
        if j==5:
            return "YES"
    return "NO"
print(counthelllo())
