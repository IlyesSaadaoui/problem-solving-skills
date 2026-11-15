import sys
input=sys.stdin.readline
n=int(input())
T=list(map(int,input().split()))
T2=[]
T3=[]
s2=0
s3=0
for i in range (n-1):
    if T[i]<=T[i+1]:
        T2.append(1)
        s2+=1
    else:
        T2.append(0)
for i in range (n-1):
    if T[i]>=T[i+1]:
        T3.append(1)
        s3+=1
    else:
        T3.append(0)
q=int(input())
res=[]
for i in range (q):
    ch=input().split()
    if ch[0]=="2":
        if s2==n-1:
            res.append("YES")
        else:
            res.append("NO")
    elif ch[0]=="3":
        if s3==n-1:
            res.append("YES")
        else:
            res.append("NO")
    else:
        j=int(ch[1])-1
        x=int(ch[2])
        T[j]=x
        if j>0:
            k=j-1
            s2-=T2[k]
            s3-=T3[k]
            if T[k]<=T[k+1]:
                T2[k]=1
            else:
                T2[k]=0
            if T[k]>=T[k+1]:
                T3[k]=1
            else:
                T3[k]=0
            s2+=T2[k]
            s3+=T3[k]
        if j<n-1:
            k=j
            s2-=T2[k]
            s3-=T3[k]
            if T[k]<=T[k+1]:
                T2[k]=1
            else:
                T2[k]=0
            if T[k]>=T[k+1]:
                T3[k]=1
            else:
                T3[k]=0
            s2+=T2[k]
            s3+=T3[k]
print("\n".join(res))