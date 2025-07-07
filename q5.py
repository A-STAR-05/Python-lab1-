prime=set()
for i in range(2,50):
    for j in range (2,i):
        if i%j==0:
            break
    else:
        prime.add(i)
checkprime=input("Enter a number to check if it is prime: ")
if int(checkprime) in prime:
    print(f"{checkprime} is a prime number.")
else:
    print(f"{checkprime} is not a prime number.")