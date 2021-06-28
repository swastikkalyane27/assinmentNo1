l=[]
for i in range(10):
    if i<2:
       l.append(i)
    else:
        l.append(l[-1]+l[-2])
print(*l)
l1=[0,1]
while True:
   l1.append(l1[-1]+l1[-2])
   if len(l1)>10:
       break
print(*l1)


l1=[0,1]
i = 0
while i<10:
   l1.append(l1[-1]+l1[-2])
   i += 1
print(*l1)
