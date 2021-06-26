#python prog to multiply all numbers in list
lis1 = [1,2,3,4,5]
lis2 = [1,2,3,4,5]

## using for loop and range
# res = 1
# for i in lis1:
#         a = i
#         res = res * a
# print(res)



## using math module
# from math import prod
# a = prod(lis1)
# print(a)



## using functools module
# from functools import reduce
# l1 = list(map(lambda x,y: x+y,lis1,lis2))
# print(l1)
#



## using numpy module
# import numpy as np
# result = np.prod(np.array(lis1))
# print(result)


def prod(lis1):
    mult = 1
    if len(lis1) == 0:
        return 1
    else:
        mult = mult*lis1[0]*prod(lis1[1:])
        return mult
print(prod(lis1))






# from math import prod
# class Lis_op:
#     def __init__(self):
#         pass
#     def m1(self):
#         self.sum = sum(lis1)
#         self.prod = prod(lis1)
#         self.max = max(lis1)
#         self.min = min(lis1)
#         print("sum of elements in list:",self.sum)
#         print("product of elements in list:", self.prod)
#         print("largest no in list:",self.max)
#         print("largest no in list:", self.min)
#
# o = Lis_op()
# print(o.sum)
# o.m1()
#
# #
# class Lis_op:
#     #@staticmethod
#     def m2():
#         add = sum(lis1)
#         mul = prod(lis1)
#         print("sum of elements in list:", add)
#         print("product of elements in list:", mul)
# Lis_op.m2()
# o = Lis_op()
# o.m2()
