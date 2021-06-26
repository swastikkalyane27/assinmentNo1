#python prog to remove ith character from the string

str1 = input("enter the string")
n = int(input("enter the nth num"))
char = input("enter the char")
if n == str1.find(char):
    l1 = list(str1)
    # print(l1)
    l1.remove(char)
    print("".join(l1))


# string = "shubham"
# i = 5
# def remove(string, i):
#     a = string[: i]
#     b = string[i + 1:]
#     return a + b
#
# print(remove(string, i))



string = "shubhamb"
i = 3
def remove(string, i):
    string = string.replace(string[i], "")
    return string

print(remove(string, i))
