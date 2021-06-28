# l1=[10,20,30,40,40,50,405,2]
# a=l1[0]
# # b=l1[-1]
# l1[0]=l1[-1]
# l1[-1]=a
# print(l1)

# def swapList(list):
#     # Storing the first and last element
#     # as a pair in a tuple variable get
#     get = list[-1], list[0]
#
#     # unpacking those elements
#     list[0], list[-1] = get
#
#     return list
#
# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))
#
#
def swapList(list1):
    start, *middle, end = list1
    print(middle)
    list1 = [end, *middle, start]

    return list1
list = [12,3,4,5,6,7]
print(swapList(list))

#
# def swapList(list):
#     first = list.pop(0)
#     last = list.pop()
#
#     list.insert(0, last)
#     list.append(first)
#
#     return list
#
#
# newList = [12, 35, 9, 56, 24]
# #
# print(swapList(newList))
