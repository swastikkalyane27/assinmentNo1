# Finding Ordered Words In A Dictionary using Python Possible Words using given characters in Python



s = input("enter the string:")
lst = list(s)
lst.sort()
check =''.join(lst)
if (s == check):
	print("TRUE")
else:
    print("FALSE")	