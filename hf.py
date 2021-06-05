n,q=map(int,input().split())
r=[0]*n
g=[0]*n
b=[0]*n
for i in range(n):
    r[i],g[i],b[i]=map(int,input().split())
for i in range(q):
    l=list(map(int,input().split()))
    f=0
    for j in range(n):
        if r[j]==l[0] and g[j]<=l[1] and b[j]<=l[2]:
            if g[j]==l[1] and b[j]==l[2]:
                f=3
                break
            f=1
            break
    for j in range(n):
        if f==0 or f==3:
            break
        if r[j]<=l[0] and g[j]==l[1] and b[j]<=l[2]:
            if r[j]==l[0] and b[j]==l[2]:
                f=3
                break
            f+=1
            break
    for j in range(n):
        if f<2 or f==3:
            break
        if r[j]<=l[0] and g[j]<=l[1] and b[j]==l[2]:
            f+=1
            break
    print(f)
    if f==3:
        print("YES")
    else:
        print("NO")
        
        
