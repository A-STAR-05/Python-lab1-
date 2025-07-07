l = ["Bob", "John", "Alice", "Mike", "Sara", "Ram", "Ram"]
count = {}

for i in l:
    if i in count:
        count[i] = count.get(i, 0) + 1
    else:
        count[i] = 1

print(count)
