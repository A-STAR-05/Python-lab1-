#fibbo
n=int(input("enter a nth term:"))
a,b,c=1,1,0
print(a,b,end=' ');
for i in range(2,n):
    c=a+b
    print(c,end=' ')
    a=b
    b=c