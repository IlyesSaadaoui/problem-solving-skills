t=int(input())
for i in range (t):
    a,b,c=map(int,input().split())
    if a>=b:
        print(a+c-b)
    else:
        if a+c-b>=b-a:
            print(a+c-b)
        else:
            print(b-a)
