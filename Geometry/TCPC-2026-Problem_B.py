import math
n=int(input())
for i in range (n):
    a,b,c,k=map(float,input().split())
    a= math.radians(a)
    b= math.radians(b)
    c= math.radians(c)
    a= math.sin(a)
    b= math.sin(b)
    c= math.sin(c)
    print(math.sqrt(k/(math.pi -2*a*b*c)))
    

    