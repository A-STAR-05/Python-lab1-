#pos,neg,zero counter
a=[]
pos,neg,zer=0,0,0
for i in range(0,10):
    entn=int(input(f'enter{i+1}th element'))
    a.append(entn)
for i in a:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zer+=1
print(f'positive={pos},negative={neg},zero={zer}')