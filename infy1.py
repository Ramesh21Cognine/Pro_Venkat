l=[int(a) for a in input().split(" ")]
m=[int(a) for a in input().split(" ")]
flag = 0
p=l[:]
q=m[:]
even=[]
odd=[]
for i in range(0,len(l)):
    for j in range(0,len(m)):
         temp = l[i]
         l[i] = m[j]
         m[j] = temp
         if(sum(l)==sum(m)):
             if((l[i]*m[j])%2==0):
                 
                 even.append(m[j])
                 even.append(l[i])
             else:
                 
                 odd.append(m[j])
                 odd.append(l[i])
        
         l=p[:]
         m=q[:]
final=[]
final.extend(even)
final.extend(odd)
if(len(final)==0):
    print("-1")
else:
    for i in range(0,len(final)-1):
        print(final[i],end=",")
    print(final[i+1])
        
