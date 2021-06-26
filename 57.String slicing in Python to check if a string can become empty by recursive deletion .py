#!/usr/bin/env python
# coding: utf-8

# In[1]:


def checkEmpty(input, pattern):

# If both are empty
    if len(input)== 0 and len(pattern)== 0:
        return 'true'
    
# If only pattern is empty
    if len(pattern)== 0:
        return 'true'

    while (len(input) != 0):

# find sub-string in main string
        index = input.find(pattern)

# check if sub-string founded or not
        if (index ==(-1)):
           return 'false'

# slice input string in two parts and concatenate
        input = input[0:index] + input[index + len(pattern):]

    return 'true'
if __name__ == "__main__":
    input ='khokho'
    pattern ='kha'
    print (checkEmpty(input, pattern))


# In[10]:


def solve(s, t):
    while len(s) > 0:
        position = s.find(t)
        print(position)
        if position == -1:
            break
        s = s.replace(t, "", 1)
    return len(s) == 0
s = "pipipinn"
t = "pin"
print(solve(s, t))


# In[ ]:




