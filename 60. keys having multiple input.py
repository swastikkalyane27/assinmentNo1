#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_dict = {}

a, b, c = 15, 26, 38
my_dict[a, b, c] = a + b - c

a, b, c = 5, 4, 11
my_dict[a, b, c] = a + b - c

print("The dictionary is :")
print(my_dict)


# In[6]:


# dictionary containing longitude and latitude of places
places = {("19.07'53.2", "72.54'51.0"):"Mumbai", ("28.33'34.1", "77.06'16.6"):"Delhi"}

print(places)
print()


# Traversing dictionary with multi-keys and crearing
# different lists from it
lat = []
long = []
plc = []
for i in places:
	lat.append(i[0])
	long.append(i[1])
	plc.append(places[i[0], i[1]])

print(lat)
print(long)
print(plc)


# In[ ]:




