#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#for 3 digits
num=int(input('enter any number:'))
sum=0
i=num
while i>0:
    digit=i%10
    sum+=digit**3
    i//=10
if num==sum:
    print(num,'is an Armstrong number')
else:
    print(num,'is not an Armstrong number')


# In[2]:


# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)


# In[1]:


#for n digits 1234 12345
n = int(input('enter any number'))
result = 0
a = len(str(n))
temp=n
for i in range(a+1):
    if i>0:
        digit = temp % 10
        result += digit ** a
        temp = temp // 10
print(result)
if result == n:
    print(n,'is an armstrong number')
else:
    print(n,'is not an armstrong number')

        


# In[ ]:


<!-- 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number -->

