#3. Python program to print all Prime numbers in an Interval

# def prime(n):
#     count=0
#     for i in range(2,n):
#         if n%i==0:
#             count+=1
#     if count>1:
#             print(n,"is NOT prime no.")
#     else:
#             print(n,"is prime no.")
# prime(134)

# n=int(input("enter no\n"))
# COUNT=0
# i=1
# while i<n:
#    if n%i==0:
#      COUNT+=1
#    i+=1
# if COUNT>2:
#     print("not prime")
# else:
#     print("prime")


# def prime(low,upper):
#     for num in range(low,upper):
#          if num>1:
#              for i in range(2,num):
#                  if num % i ==0:
#                      break
#              else:
#                      print(num)
# prime(10,20)


num = int(input('enter no : -'))
flag = 0
i = 2
while i< num:
    if num % i == 0:
        flag = 1
        break
    i +=1
if flag == 1:
        print('not prime no')
else:
        print( 'prime no')

# perfect number

num = eval(input())