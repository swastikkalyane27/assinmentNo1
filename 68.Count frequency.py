# Python Dictionary to find mirror characters in a string Counting the frequencies in a list using dictionary in Python


# Mirror characters 
# abc = zyx 





# import string
# s = input("Enter the string for mirror caharcters:")
# alphabet = string.ascii_lowercase
# rev = alphabet[::-1]
# pswrd = ""
# d = dict(zip(alphabet,rev))        #zip(key,values)
# for i in s:
# 	pswrd = pswrd + d[i]
# print(s)
# print(pswrd)	









# def mirrorChars(str1,k):
# 	original = 'abcdefghijklmnopqsturvwxyz'
# 	reverse = original[::-1]
# 	dict1 = dict(zip(original,reverse))

# 	a = str1[0:k-1]
# 	# print(a)
# 	b = str1[k-1:]
# 	# print(b)
# 	mirror = ''

# 	for i in range(0,len(b)):
# 		mirror = mirror + dict1[b[i]]

# 	print(a + mirror)

# if __name__ == '__main__':
# 	str1 = 'abcdef'
# 	k = 1 
# 	mirrorChars(str1,k)






















# Counting the frequencies in a string using dict:



# num1 = [1,2,3,4,5,4,3,2,1,2,3,2,1,1]
# dict1 ={}
# for num in num1:
# 	if num in dict1:
# 		dict1[num] += 1
# 	else:
# 	    dict1[num] = 1
# print(dict1)    	










from collections import Counter

lis = [11,22,33,22,11,44,55,55,66]
frequency_lst = Counter(lis)
print(frequency_lst)



