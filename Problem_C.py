t=int(input())
for i in range(t):
    n=int(input())
    T=list(map(int,input().split()))
    T1=[]
    d={}
    for i in range (n-4):
        s=T[i]+T[i+2]-T[i+4]
        T1.append(s)
        if not (s in d):
            d[s]=[i]
        else:
            d[s].append(i)
        
    s2=0
    d1={}
    for i in range (len(T1)):
        s=0
        if i+2<=len(T1)-1:
            if T1[i+2]==T1[i]:
                s=s+1
        if i+4<=len(T1)-1:
            if T1[i+4]==T1[i]:
                s=s+1
        if not (T1[i] in d1):
            d1[T1[i]]=0
        else :
            d1[T1[i]]+=1
        s1=len(d[T1[i]])-d1[T1[i]]-s
        s2=s2+s1-1
    print(s2)
