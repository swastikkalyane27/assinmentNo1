#python prog to accept the string which contains all vowels
# str1 = input("enter the string ")
# l1 = ["a","e","i","o","u"]
# l2 = []
# for i in str1:
#     if i in l1:
#         if i not in l2:
#             l2.append(i)
#     # elif i == " ":
#     #     l2.append(i)
# if len(l2) == len(l1):
#     print("string accepted")
# else:
#     print("string rejected")



# Python program for the above approach
# def check(string):
# 	if len(set(string.lower()).intersection("aeiou")) == 5:
# 		return ('accepted')
# 	else:
# 		return ("not accepted")
#
# # Driver code
# if __name__ == "__main__":
# 	string = "Geeksforaeiou aeiou"
# 	print(check(string))


# def check(string):
# 	string = string.replace(' ', '')
# 	string = string.lower()
# 	vowel = [string.count('a'), string.count('e'), string.count(
# 		'i'), string.count('o'), string.count('u')]
#
# 	# If 0 is present int vowel count array
# 	if vowel.count(0) > 0:
# 		return('not accepted')
# 	else:
# 		return('accepted')
#
#
# # Driver code
# if __name__ == "__main__":
#
# 	string = "SEEquoiaL"
#
# 	print(check(string))



