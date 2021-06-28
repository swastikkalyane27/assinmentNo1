#2. Python Program to check Armstrong Number

# num=int(input("enter no."))
# l1=list(str(num))
# pow=len(l1)
# sum=0
# for i in l1:
#     sum=sum+int(i)**pow
# if (num)==sum:
#     print(num,'is armstrong no.')
# else:
#     print(num,"not an armstrong no.")
#

# num=int(input("enter a number"))
# sum=0
# temp=num
# pow=len(str(num))
# while temp>0:
#     digit=temp%10
#     sum+=digit**pow
#     temp= temp//10
# if num==sum:
#     print(num,"is a armstrong number")
# else:
#     print(num," is not an armstrong number")

# program to check armstrong number in certain interval:
lower= 100
upper = 2000
for num in range(lower,upper+1):
    pow=len(str(num))
    sum = 0
    temp = num
    while temp >0:
        digit = temp % 10
        sum += digit ** pow
        temp=temp//10
    if sum == num:
        print(num)


