t=int(input())
for i in range (t):
    a,b=map(int,input().split())
    ch=list(input())
    s=0
    for j in range (0,len(ch),b):
        if ch[j:min(j+b,len(ch))].count("0")==0:
            s+=1
    print(s)
    
    
