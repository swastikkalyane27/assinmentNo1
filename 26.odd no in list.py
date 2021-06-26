# python prog to print odd numbers in list

## using list comprehension
# n = int(input("enter the num: "))
# l1 = [x for x in range(n) if x%2 !=0 and x>0]
# print(l1)


## using for loop and range
# lis = []
# n = int(input("enter the num: "))
# for i in range(n):
#     if i%2 != 0 and i>0:
#         lis.append(i)
# print(lis)


## using filter and lambda function
# l1 = [55,34,56,74,68,21,8,13,47]
# l2 = list(filter(lambda x : x%2 != 0,l1))
# print(l2)


## using while loop
# l1 = [55,34,56,74,68,21,8,13,47]
# num = 0
# while num < len(l1):
#     if l1[num] % 2 != 0 :
#         print(l1[num], end=" ")
#     num += 1