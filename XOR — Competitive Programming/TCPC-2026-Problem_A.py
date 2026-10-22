t=int(input())
for i in range (t):
    n=int(input())
    T=list(map(int,input().split()))
    d={}
    d1={}
    for j in range(31):
        d[j]={0:[],1:[]}
        d1[j]={0:0,1:0}
    for j in range (len(T)):
        ch=bin(T[j])[2:]
        ch=ch[::-1]
        for k in range (len(ch)):
            if ch[k]=="1":
                d1[k][1]+=1
            else:
                d1[k][0]+=1
            d[k][0].append(d1[k][0])
            d[k][1].append(d1[k][1])
        for k in range (len(ch),31):
            d1[k][0]+=1
            d[k][0].append(d1[k][0])
            d[k][1].append(d1[k][1])        
    s=int(input())
    for i in range (s):
        a,b=map(int,input().split())
        som=0
        for k in d:
            if a >= 2:
                z0 = d[k][0][a-2]
                z1 = d[k][1][a-2]
            else:
                z0 = 0
                z1 = 0
            som+=(d[k][0][b-1]-z0)*(d[k][1][b-1]-z1)*(2**k)
        print(som)
            
        
        
    
