#Python | Check if a Substring is Present in a Given String Find length of a string in python (4
#ways)

# str1 = input("enter the string:")
# substr = input("enter the string:")
# if substr in str1:
#     print("Substring present in string")
# else:
#     print("Substring not present in string")


# function to check if small string is
# there in big string
# def check(string, sub_str):
#     if (string.find(sub_str) == -1):
#         print("NO")
#     else:
#         print("YES")
#
# # driver code
# string = "geeks for geeks"
# sub_str = "geek"
# check(string, sub_str)


# def check(s2, s1):
#     if (s2.find(s1) > 0):
#         print("YES")
#     else:
#         print("NO")
#
#
# s2 = "A geek in need is a geek indeed"
# s1 = "geek"
# check(s2, s1)
#


# print(len(str1))
#
# count = 0
# for i in str1:
#     count += 1
# print(count)



# Python code to demonstrate string length
# using while loop.

# Returns length of string
# def findLen(str):
# 	counter = 0
# 	while str[counter:]:
# 		counter += 1
# 	return counter
#
# str = "geeks"
# print(findLen(str))



# Python code to demonstrate string length
# using join and count

# Returns length of string
# def findLen(str):
#     if not str:
#         return 0
#     else:
#         some_random_str = 'p'
#         a = (some_random_str).join(str)
#         print(a)
#         b = a.count("p") + 1
#         return b
# str = "geeks"
# print(findLen(str))
