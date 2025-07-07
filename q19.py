#armstrong between 100 to 999
for i in range(100, 1000):
    sum = 0
    num = i
    while num > 0:
        digit = num % 10
        sum += digit ** 3
        num //= 10
    if sum == i:
        print(i)