#palindorme

num = int(input("Enter a number: "))

if str(num) == str(num)[::-1]:
    print("Palindrome Number!")
else:
    print("Not a Palindrome Number!")
