# Python counter and dictionary intersection example 



from collections import Counter

s1 = "hello"
s2 = "asdfghhhdeklmnltyo"

# no of characters in s1 must be in s2
# Occurence of each character in s1 must be equal or less in s2

d1 = Counter(s1)
d2 = Counter(s2)

result = d1 & d2
if (result == d1):
	print("possible")
else:
    print("not possible")	

