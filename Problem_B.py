t=int(input())
for i in range (t):
    n=int(input())
    ch= input()
    T=[1]*n
    d=[]
    for i in range (n):
        if ch[i]=="1":
            d.append(i)
        elif ch[i]=="2": 
            if len(d)==0:
                T[i]=0
            else:
                T[d[len(d)-1]]=0
                del(d[len(d)-1])
        else:
            T[i]=0
    d1=[]
    for i in range (len(T)):
        if T[i]==1:
            d1.append(i+1)
    if len(d1)==0:
        print(0)
        print("")
    else:
        print(len(d1))
        print(" ".join(map(str,d1)))

                
                

