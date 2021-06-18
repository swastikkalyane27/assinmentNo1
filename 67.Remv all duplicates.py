# Remove all duplicates words from a given sentence:



# str1 = "hello how are you hello"
# str2 = str1.split(" ")
# print("The original sentence is:",str1)
# list1 = []
# for i in str2:
# 	if i not in list1:
# 		list1.append(i)

# 	output= " ".join(list1)	


# print("The duplicate free sentence is:",output)



	










a = "hello how are you hello"
print(' '.join(dict.fromkeys(a.split())))









# str1 = 'ABBCCDDDDEEF'
# output = ''
# for ch in str1:
# 	if ch not in output:
# 		output = output + ch
# print(output)		








# s = 'AABCCCDEEF'
# s1 = set(s)
# output = ''.join(s1)
# print(output)