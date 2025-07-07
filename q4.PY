text=input("ENTER A STRING: ")
cnt={}
for i in text:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
print(cnt)