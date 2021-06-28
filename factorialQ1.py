# # 1. Python Program for factorial of a number with and without recursion
# #with recursion
# n=int(input("enter number"))
# fact1=1
# def fact(n):
#     if n==0:
#         fact1=1
#     elif n>0:
#         fact1=n*fact(n-1)
#     return fact1
# print(fact(n))

# without recursion
#
# n=int(input("enter number\n"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# using while

n=int(input("enter valid no\n"))
fact=1

while n>0:
    fact=fact*n
    n-=1
print(fact)


def fact(n):
    return 1 if (n==1 or n==0) else n*fact(n-1);
num = 5
print(fact(num))