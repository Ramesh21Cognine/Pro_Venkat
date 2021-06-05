num=int(input())
base = int(input())
s=""
while num!=0:
    r=num%base
    s+=str(r)
    num=num//base
p=s[::-1]
l=[]
c=0
for i in p:
    if i=='0':
        c=c+1
    else:
        l.append(c)
        c=0
if(max(l)==0):
    print("-1")
else:
    print(max(l))
