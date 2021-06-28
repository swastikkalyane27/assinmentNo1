# ''' Python Dictionary to find mirror characters in a string Counting the frequencies in a list using
# dictionary in Python '''
#
# #
# # def mirrorChars(input, k):
# #     # create dictionary
# #     original = 'abcdefghijklmnopqrstuvwxyz'
# #     reverse = 'zyxwvutsrqponmlkjihgfedcba'
# #     dictChars = dict(zip(original, reverse))
# #     # print(dictChars)
# #     # separate out string after length k to change
# #     # characters in mirror
# #     prefix = input[0:k ]
# #     suffix = input[k:]
# #     mirror = ''
# #
# #     # change into mirror
# #     for i in range(0, len(suffix)):
# #         mirror = mirror + dictChars[suffix[i]]
# #
# #     # concat prefix and mirrored part
# #     print(prefix + mirror)
# #
# # input = 'paradox'
# # k = 3
# # mirrorChars(input, k)
#
#
# # Python program to find mirror characters in string
#
# def mirror(str1, n):
#     # Creating a string having reversed
#     # alphabetical order
#     alphaset = "zyxwvutsrqponmlkjihgfedcba"
#     l = len(str1)
#
#     # The string up to the point specified in the
#     # question, the string remains unchanged and
#     # from the point up to the length of the
#     # string, we reverse the alphabetical order
#     result = ""
#     for i in range(0, n):
#         result = result + str1[i];
#
#     for i in range(n, l):
#         result = (result +
#                   alphaset[ord(str1[i]) - ord('a')]);
#     return result;
#
#
#
# str1 = input("Enter the string ::>")
# n = int(input("Enter the position ::>"))
# result = mirror(str1, n - 1)
# print("The Result ::>", result)
#

from collections import Counter
import string
s = input("Enter the string for mirror caharcters:")
alphabet = string.ascii_lowercase
rev = alphabet[::-1]
pswrd = ""
d = dict(zip(alphabet,rev))        #zip(key,values)
for i in s:
	pswrd = pswrd + d[i]
print(s)
print(pswrd)
print(Counter(pswrd))