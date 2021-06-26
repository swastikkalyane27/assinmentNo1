#!/usr/bin/env python
# coding: utf-8

# In[4]:


#by using list
string = "tutorialspoint"
duplicates = []
for char in string:
    if string.count(char) > 1:
        if char not in duplicates:
            duplicates.append(char)
print(*duplicates)


# In[6]:


#by using dict
string = "tutorialspoint"
duplicates = {}
for char in string:
    if char in duplicates:
        duplicates[char] += 1
    else:
        duplicates[char] = 1
for key, value in duplicates.items():
    if value > 1:
        print(key, end = " ")


# In[2]:


# Python Counter| Find all duplicate characters in string Dictionary Programs: 
from collections import Counter

def find_dup_char(input):

# now create dictionary using counter method
# which will have strings as key and their
# frequencies as value
    WC = Counter(input)
    j = -1


# Finding no. of occurrence of a character
# and get the index of it.
    for i in WC.values():
        j = j + 1
        if( i > 1 ):
            print (i,end=" ")

if __name__ == "__main__":
    input = 'geeksforgeeks'
    find_dup_char(input)


# In[ ]:





# In[ ]:




