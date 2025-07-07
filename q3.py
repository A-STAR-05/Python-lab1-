import random as rnd
l,evl = [],[]
for i in range(1,100):
    l.append(rnd.randint(1,100))
print(l)
for i in l:
    if i% 2 == 0:
        evl.append(i)
print(evl)