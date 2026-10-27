a,b=map(int,input().split())
if a%2!=b%2 or a>b:                    
    print(-1)
else:
    ch=bin(a)[2:][::-1]
    h=b-a
    ch1=bin(h)[2:][::-1][1:]
    T=[int(c) for c in ch1]
    if h==0:
        T=[0]
    T1=[]
    for j in range(max(len(ch),len(T))):          
        tj = T[j] if j<len(T) else 0
        aj = int(ch[j]) if j<len(ch) else 0
        T1.append(2*tj+aj)

    M=[[0]*len(T1) for i in range(max(T1))]
    for j in range(len(T1)):
        for k in range(T1[j]):
            M[k][j]=1
    T2=[int("".join(map(str,r))[::-1],2) for r in M]
    print(len(T2))
    print(" ".join(map(str,T2)))