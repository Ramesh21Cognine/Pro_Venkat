n=int(input())
l=[]
for i in range(n):
    r=[]
    s=input()
    for j in s:
        r.append(j)
    l.append(r)
s1=input()
s2=input()
c=0
p=len(s1)
for i in range(n):
    for j in range(n):
        if l[i][j]=="*" and c<p:
            if l[i][j+1]=="*":
                l[i][j:j+len(s2)]=s2
                c+=1
            else:
                l[i][j]=s1[c]
                c+=1
        print(l[i][j],end="")
    print()

            
