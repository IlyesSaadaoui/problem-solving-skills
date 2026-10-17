t=int(input())
for i in range(t):
    n=int(input())
    T=list(map(int,input().split()))
    T1=[]
    for i in range (n-4):
        T1.append(T[i]+T[i+2]-T[i+4])
    s2=0
    for i in range (len(T1)):
        s=0
        if i+2<=len(T1)-1:
            if T1[i+2]==T1[i]:
                s=s+1
        if i+4<=len(T1)-1:
            if T1[i+4]==T1[i]:
                s=s+1
        
        s1=T1[i:].count(T1[i])-s
        s2=s2+s1-1
    print(s2)
            
