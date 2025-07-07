#LARGEST AND SMALLEST IN A LIST
a=[]

for i in range(0,int(input('enter the number of elements'))):
    entn=int(input(f'enter{i+1}th element'))
    a.append(entn)
print(a);
print(max(a),min(a))