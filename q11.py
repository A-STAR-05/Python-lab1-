a=int(input("enter a numner:"))
print("you entered:",a)
for i in range (2,a):
    if a %i==0:
        print("not prime")
        break   
else:
    print("prime")