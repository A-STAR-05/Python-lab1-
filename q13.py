#factorial
a=int(input("enter a number:"))
fact=1
for i in range (1,a+1):
    fact*=i
print("factorial of",a,"is",fact)
