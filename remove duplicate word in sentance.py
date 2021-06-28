# 68)Python | Remove all duplicates words from a given sentence
# str1 = input('enter string')
# str2 = str1.split(' ')
# # print(str2)
# str3 = []
# for i in str2:
#     if i not in str3:
#         str3.append(i)
# str4 = ' '.join(str3)
# print(str4)

a = 'helle how are you hello'
print(' '.join(dict.fromkeys(a.split())))
# print(dict.fromkeys(a.split()))