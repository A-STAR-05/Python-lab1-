d = {}
n = int(input("How many key-value pairs? "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

search = input("Enter key to search: ")
if search in d:
    print(f"Value: {d[search]}")
else:
    print("Key not found.")