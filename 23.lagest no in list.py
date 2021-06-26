# Python program to find largest number in a list
# l1 = [55,34,56,74,68,21,88]

## using for loop and range
# a = l1[0]
# n = len(l1)
# for i in range(1,n):
#     if l1[i] > a:
#         a = l1[i]
# print(a)


## using function
# def Max(l1):
#     max = l1[0]
#     for x in l1:
#         if x > max:
#             max = x
#     return max
# Max(l1)


## using in built function min
# print(max(l1))


## using slicing
# l1.sort()
# print(l1)
# print("the smallest number in list:", l1[-1])


## using numpy module
# import numpy as np
# result = np.max(np.array(l1))
# print(result)
