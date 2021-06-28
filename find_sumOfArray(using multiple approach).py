
def sumlist1(l1):
    n=len(l1)
    sum=0
    for i in l1:
        sum+=i
    return sum
l1=[10,20,30]
print(sumlist1(l1))
print('#'*10)
l2=[20,30,40,12,303,23]
sum=0
for i in l1:
    sum+=i
print(sum)

print('#'*10)
sum2=0
for i in range(len(l2)):
     sum2=sum2+l2[i]
print(sum2)
print('#'*10)
sum3=0
n=len(l2)
i=0
while i<=n-1:
    sum3=sum3+l2[i]
    i+=1
print(sum3)
print("#"*10)