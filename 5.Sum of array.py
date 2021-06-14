#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[5,6,7,8,9]
x=sum(l)
print(x)


# In[6]:


l1=[1,2,3,4,5]
sum=0
for i in range(len(l1)):
    sum+=l1[i]
print('sum of all the elements of an array:',sum)


# In[7]:


def sum(array):
    sum=0
    for i in array:
        sum+=i
    return sum
array=[1,2,3,4,5]
print(sum(array))


# In[ ]:




