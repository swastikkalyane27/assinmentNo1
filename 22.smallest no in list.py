# Python program to find smallest number in a list
l1 = [55,34,56,74,68,21,88]

## using for loop and range
# a = l1[0]
# n = len(l1)
# for i in range(1,n):
#     if l1[i] < a:
#         a = l1[i]
# print(a)


## using function
# def Min(l1):
#     min = l1[0]
#     for x in l1:
#         if x < min:
#             min = x
#     return min
# Min(l1)
#


## using slicing
# l1.sort()
# print(l1)
# print("the smallest number in list:", *l1[:1])


## using in built function min
# print(min(l1))


## using numpy module
# import numpy as np
# result = np.min(np.array(l1))
# print(result)