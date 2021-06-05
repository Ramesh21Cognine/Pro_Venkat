t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    t=list(set(l))
    c=0
    for i in t:
        if l.count(i)%2==0:
            c+=1
    if c>=1:
        print("Second")
    else:
        print("First")
        
