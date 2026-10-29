t=int(input())
for i in range (t):
    n=int(input())
    T=list(map(int,input().split()))
    s1=0
    s2=0
    s3=0
    for j in range (len(T)):
        if T[j]%2!=0:
            s1+=1
        else:
            if (T[j]//2)%2==1:
                s2+=1
            else:
                s3+=1
    print(max(s1,s2,s3))
            
