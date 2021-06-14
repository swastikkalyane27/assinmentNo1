#!/usr/bin/env python
# coding: utf-8

# In[1]:


#factorial of n with recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        f=n*fact(n-1)
        return f
num=int(input('enter a number:'))
result=fact(num)
print(result)


# In[2]:


#without recursion
import math
def factorial(n):
    return(math.factorial(n))
num=int(input('enter a number:'))
print('Factorial of',num,'is',factorial(num))


# In[1]:


# using for loop
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
    print(" Factorial does not exist for negative numbers")    
elif num == 0:    
    print("The factorial of 0 is 1")    
else:    
    for i in range(1,num + 1):    
        factorial = factorial*i    
    print("The factorial of",num,"is",factorial)    


# In[3]:


def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  
  
num = 5  
print("Factorial of",num,"is",)  
fact(num) 


# In[ ]:




