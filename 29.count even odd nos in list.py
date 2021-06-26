# python prog to count even and odd numbers in a list

## using for loop
# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = []
# l3 = []
# for i in l1:
#     if i%2 == 0:
#         l2.append(i)
#         a = len(l2)
#     elif i%2 != 0:
#         l3.append(i)
#         b = len(l3)
# print("count of even no: ",a)
# print("count of odd no: ",b)


## using filter and lambda function
# l1 = [1,2,3,4,5,6,7,8,9]
# odd_list = len(list(filter(lambda x: x%2 != 0,l1)))
# print("count of odd nos in list: ",odd_list)
#
# even_list = len(list(filter(lambda x: x%2 == 0,l1)))
# print("count of even nos in list: ",even_list)


## using counter and for loop
l1 = [1,2,3,4,5,6,7,8,9]
even_count = 0
odd_count = 0
for i in l1:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("count of even nos in list: ",even_count)
print("count of odd nos in list: ",odd_count)



## using while loop
l1 = [1,2,3,4,5,6,7,8,9]
num = 0
even_count = 0
odd_count = 0
while num < len(l1):
    if l1[num] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num += 1
print("count of even nos in list: ",even_count)
print("count of odd nos in list: ",odd_count)
