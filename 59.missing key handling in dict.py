#!/usr/bin/env python
# coding: utf-8

# In[8]:


d = { 'a' : 1 , 'b' : 2 }
# trying to output value of absent key
print ("The value associated with 'c' is : ")
print (d['c'])


# Method 1 : Using get()
# 
# get(key,def_val) method is useful when we have to check for the key. If the key is present, value associated with the key is printed, else the def_value passed in arguments is returned.

# In[4]:


country_code = {'India' : '0091','Australia' : '0025','Nepal' : '00977'}

# search dictionary for country code of India
print(country_code.get('India', 'Not Found'))

# search dictionary for country code of Japan
print(country_code.get('Japan', 'Not Found'))
print(country_code)


# Method 2 : Using setdefault()
# 
# setdefault(key, def_value) works in a similar way as get(), but the difference is that each time a key is absent, a new key is created with the def_value associated to the key passed in arguments.
# 

# In[5]:


country_code = {'India' : '0091','Australia' : '0025','Nepal' : '00977'}

# Set a default value for Japan
country_code.setdefault('Japan', 'Not Present')

# search dictionary for country code of India
print(country_code['India'])

# search dictionary for country code of Japan
print(country_code['Japan'])
print(country_code)


# Method 3 : Using defaultdict
# 
# “defaultdict” is a container that is defined in module named “collections“. It takes a function(default factory) as its argument. By default, default factory is set to “int” i.e 0. If a key is not present is defaultdict, the default factory value is returned and displayed. It has advantages over get() or setdefault().
# 
# A default value is set at the declaration. There is no need to invoke the function again and again and pass similar value as arguments. Hence saving time.
# The implementation of defaultdict is faster than get() or setdefault()
# 

# In[7]:


# Python code to demonstrate defaultdict

# importing "collections" for defaultdict
import collections
def show():
    return 'key not found'

# declaring defaultdict
# sets default value 'Key Not found' to absent keys
country_dict = collections.defaultdict(show())

# initializing values
country_dict['a'] = 1

# initializing values
country_dict['b'] = 2

# printing value
print ("The value associated with 'a' is : ",end="")
print (country_dict['a'])

# printing value associated with 'c'
print ("The value associated with 'c' is : ",end="")
print (country_dict['c'])


# In[ ]:




