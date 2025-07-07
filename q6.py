l1,l2=[],[]
for i in range (0,3):
    l1.append(input("Enter a number: ")) 
for i in range (0,3):
    l2.append(input("Enter a number: "))
l1=set(l1) 
l2=set(l2)
l=l1 & l2
print(l)
