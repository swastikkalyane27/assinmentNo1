#!/usr/bin/env python
# coding: utf-8

# In[14]:


#fibonacci siries
def fibonacci(n):
    if n<0:
        print('incorrect input')
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(9))        


# In[15]:


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
#             print(c)
            a = b
            b = c
        return c
print(fibonacci(9))


# In[23]:


nterms = int(input("How many terms you want? "))  
# first two terms  
n1 = 0  
n2 = 1  
count = 2  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
elif nterms == 1:  
   print("Fibonacci sequence:",n1)  
else:
   print("Fibonacci sequence:")  
   print(n1,",",n2,end=', ')  
   while count < nterms:  
       nth = n1 + n2  
       print(nth,end=' , ')  
       # update values  
       n1 = n2  
       n2 = nth  
       count += 1  
      


# In[ ]:


0,1,1,2,3,5


# In[16]:


0=a 1=b 1=c 


# In[18]:


l=[]
for i in range(10):
    if i<2:
        l.append(i)
    else:
        l.append(l[-1]+l[-2])
print(*l)


# In[34]:


l1=[]
i=0
while i<10:
    if i<2:
        l1.append(i)
    else:
        l1.append(l1[-1]+l1[-2])
    i+=1
   
      
print(*l1)


# In[38]:


# lower=int(input('enter any number'))
# upper=int(input('enter upper'))
a=0
b=1
for i in range(2,10):
	c=a+b
	print(c,end=" ")
	a=b
	b=c


# In[ ]:




