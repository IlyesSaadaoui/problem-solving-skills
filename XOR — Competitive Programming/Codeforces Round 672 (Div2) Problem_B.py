t=int(input())
import math
for i in range (t):
    n=int(input())
    T=list(map(int,input().split()))
    T1={}
    som=0
    for j in range (len(T)):
        ch=bin(T[j])[2:]
        s=len(ch)-ch.find("1")-1
        if not (s in T1):
            T1[s]=1
        else:
            T1[s]+=1
    for i in T1:
        if T1[i]!=1:
            som+=math.comb(T1[i], 2)
    print(som)
            
        
        