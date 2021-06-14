#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#prime numbers in given range 
lower=int(input('enter a lower value='))
upper=int(input('enter a upper value='))
for num in range (lower,upper+1):
    if num>1:
        for i in range (2,num):
            if (num%i)==0:
                break
        else:
                print(num)


# In[2]:


#given num is prime or not
num=int(input("enter a num:"))
flag=0
i=2
while i<num:
    if num%i==0:
        flag=1
    break
    i+=1
if flag==1:
    print("Not a prime num:",num)
else:
    print("prime num:",num)


# In[ ]:


#perfect number
num=eval(input("enter a num"))
i=1
sum=0
while i<num:
    if num%i==0:
        sum+=i
    i+=1
if sum==num:
    print('num is perfect num:',num)
else:
    print('not a perfect num:',num)

