#!/usr/bin/env python
# coding: utf-8

# In[3]:


def rotate(str1,d):
    lfirst = str1[0:d]
    lsecond = str1[d:]
    rfirst = str1[0:len(str1)-d]
    rsecond = str1[len(str1)-d:]
    print('Left rotation:',(lsecond+lfirst))
    print('Rightrotation:',(rsecond+rfirst))
if __name__ == '__main__':
    str1='shubham'
    d = 2
    rotate(str1,d)


# In[ ]:




