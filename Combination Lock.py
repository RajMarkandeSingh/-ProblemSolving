n=int(input())
a=input()
b=input()
c=0
for i in range(n):
    v=abs(int(a[i])-int(b[i]))
    if v<=5:
        c+=(v+1)
    else:
        c+=(10-v)+1
print(c-n)
