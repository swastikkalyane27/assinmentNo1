l1=[10,20,30,40,50,60,70,80]
l2=[]
for i in range(len(l1)):
    if i<2:
        continue
    else:
        l2.append(l1[i])
l2=l2+l1[:2]
print(l2)