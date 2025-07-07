import random as rnd
l = []
for i in range(1, 100):
    l.append(rnd.randint(1, 100))
t = tuple(l)
print(t)
print(max(t))
print(min(t))