# Python program to find second largest number in a list
# list1 = [55,34,56,74,68,21,88]


## using index and sort
# l1.sort()
# print(l1)
# print("the second largest number in list:", l1[-2])



## using for loop and range
# mx = max(l1[0],l1[1])          # max(55,34)= 55
# sec_mx = min(l1[0],l1[1])      # min(55,34)= 34
# for i in range(2,len(l1)):
#     if l1[i] > mx:             # 56 > 55
#         sec_mx = mx            # sec_mx = mx = 55
#         mx = l1[i]             # mx = l1[2] = 56
#     elif l1[i] > sec_mx and mx != l1[i]:
#         sec_mx = l1[i]
# print("the second largest number in list:",sec_mx)


## using copy
# l2 = set(l1[:])
# print(l2)
# l2.remove(max(l2))
# print(max(l2))


list1 = [55,34,56,74,68,21,88]
class Sle:
    def __init__(self,list1):
        self.list1 = list1

    def Second_lg_ele(self):
        largest1 = self.list1[0]
        largest2 = self.list1[1]
        for i in self.list1:
            if i > largest1 and i > largest2:
                c = largest1
                largest1 = i
                largest2 = c
            elif i > largest1:
                d = largest1
                largest1 = i
                largest2 = d
            elif i > largest2:
                e = largest2
                largest2 = i
                largest1 = e
            if largest1 < largest2:
                large = largest1
                largest1 = largest2
                largest2 = large
        print("second largest element in list :-", largest2)
a = Sle(list1)
a.Second_lg_ele()