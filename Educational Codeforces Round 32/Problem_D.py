n,k=map(int,input().split())
if k==4:
    T=[1,0,0,0,0]
    for i in range (n-k):
        s=1
        for j in range (1,5):
            s=s+T[j]
            T[j]=s
    print(T[0]*24+18*T[1]+14*T[2]+11*T[3]+9*T[4])
elif k==1:
    print(1)
elif k==2:
    b=5
    s=4
    for i in range (n-4):
        b=b+s
        s=s+1
    print(2+b)
else:
    T=[1,1,1,1]
    for i in range (n-4):
        s=1
        for j in range (1,4):
            s=s+T[j]
            T[j]=s
    print(T[0]*6+T[1]*4+T[2]*3+T[3]*2)

    
        
    
        