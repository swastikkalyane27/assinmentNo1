# python prog to print positive numbers in list

## using list comprehension
# lower = int(input("enter the number:"))
# upper = int(input("enter the number:"))
# l1 = [x for x in range(lower,upper) if x>0]
# print(l1)
#


## using for loop and range
# lower = int(input("enter the number:"))
# upper = int(input("enter the number:"))
# lis = []
# for i in range(lower,upper):
#     if i>0:
#         lis.append(i)
# print(lis)
#


## using while loop
# l1 = [-1,2,-3,4,-5,6,-7,8,-9]
# num = 0
# l2 = []
# while num < len(l1):
#     if l1[num] > 0:
#         l2.append(l1[num])
#     num += 1
# print(l2)


## using filter and lambda
# l1 = [-1,2,-3,4,-5,6,-7,8,-9]
# l2 = list(filter(lambda x : x>0,l1))
# print(l2)