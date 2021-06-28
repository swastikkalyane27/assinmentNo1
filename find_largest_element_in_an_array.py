l1=[10,20,30,40,40,12,49,20,23,40]
maxele=l1[0]
for i in l1:
    if i>maxele:
        maxele=i
        # continue
print(maxele)
print("@"*10)
maxele1=l1[0]
for i in range(0,len(l1)):
    if maxele1<l1[i]:
        maxele1=l1[i]
        # continue
print(maxele1)
print("@"*10)
print(max(l1))

