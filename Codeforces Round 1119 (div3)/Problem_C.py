t=int(input())
for i in range (t):
    n=int(input())
    ch=list(input())
    ch=list(map(int,ch))
    if ch==sorted(ch):
        print(0)
    else:
        
        s0=0
        d={}
        for j in range (len(ch)-1,-1,-1):
            if ch[j]==0:
                s0+=1
            d[j]=s0
        
        if ch[0]==1:
            print(d[1])
        else:
            s1=0
            T=[]
        
            for j in range (len(ch)):
                if ch[j]==1:
                    T.append(d[j]+s1)
                    s1+=1
            print(min(min(T),s1))
            
            
            
            
