# Python | Count the Number of matching characters in a pair of string
# str1 = input("enter the string:")
# str2 = input("enter the string:")
# l1 = []
# for i in str1:
#     if i in str2:
#         l1.append(i)
# print(len(set(l1)))


# Python code to count number of unique matching
# characters in a pair of strings

# count function count the common unique
# characters present in both strings .
# def count(str1, str2):
#     # set of characters of string1
#     set_string1 = set(str1)
#     # set of characters of string2
#     set_string2 = set(str2)
#     # using (&) intersection mathematical operation on sets
#     # the unique characters present in both the strings
#     # are stored in matched_characters set variable
#     matched_characters = set_string1 & set_string2
#
#     # printing the length of matched_characters set
#     # gives the no. of matched characters
#     print("No. of matching characters are : " + str(len(matched_characters)))
#
#
# # # Driver code
# if __name__ == "__main__":
#     str1 = 'shubham'  # first string
#     str2 = 'bhushan'  # second string
#
#     # call count function
#     count(str1, str2)





# Count the Number of matching characters in
# a pair of string
# import re
# ip1 = "geeks"
# ip2 = "geeksonly"
#
# c = 0
# for i in ip1:
# 	if re.search(i,ip2):
# 		c=c+1
# print("No. of matching characters are ", c)



# Python code to count number of matching
# characters in a pair of strings

# count function
# def count(str1, str2):
#     c = 0
#
#     # loop executes till length of str1 and
#     # stores value of str1 character by character
#     # and stores in i at each iteration.
#     for i in str1:
#
#         # this will check if character extracted from
#         # str1 is present in str2 or not(str2.find(i)
#         # return -1 if not found otherwise return the
#         # starting occurrence index of that character
#         # in str2) and j == str1.find(i) is used to
#         # avoid the counting of the duplicate characters
#         # present in str1 found in str2
#         if str2.find(i) >= 0 :
#             c += 1
#
#     print('No. of matching characters are : ', c)
#
#
# # Main function
# def main():
#     str1 = 'shubham'  # first string
#     str2 = 'bhushan'  # second string
#     count(str1, str2)  # calling count function
#
# # Driver Code
# if __name__ == "__main__":
#     main()
