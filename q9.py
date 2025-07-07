list1 = [1, 2, 3, 4, 5]
list2 = [2, 4]
result = []
for x in list1:
    if x in list2:
        continue
    else:
        result.append(x)

print("Resulting list:", result)