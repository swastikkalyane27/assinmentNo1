## Python program to find uncommon words from two Strings
str1 = input("enter the string:")
str2 = input("enter the string:")
l1 = str1.split()
l2 = str2.split()
uncommon = ""
for i in l1:
    if i not in l2:
        uncommon = uncommon + " " + i
for i in l2:
    if i not in l1:
        uncommon = uncommon + " " + i

print("all uncommon words from both the string:", uncommon)
