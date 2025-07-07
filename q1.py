import random as rnd
l,ord = [],[]
for i in range(1,100):
    l.append(rnd.randint(1,100))
print(l)
for i in l:
    if l.count(i)==1:
        ord.append(i)
print(ord)