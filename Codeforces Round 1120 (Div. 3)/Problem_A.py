t=int(input())
for i in range (t):
    n=int(input())
    a,b,c= (map(int,input().split()))
    if n>max(a,b,c):
        print(n-min(a,b,c))
    else:
        print(max(a,b,c)-min(a,b,c))
        
