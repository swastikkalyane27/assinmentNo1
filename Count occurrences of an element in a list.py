l1=(input('enter element with comma:- '))
list1=list(l1.split(","))
print(list1)
def countOccurence(ele):
    count = 0
    for i in list1:
       if i == ele:
           count =count + 1

    print('count is :- ',count)
ele=input('enter element for which you want to count occurence :- ')
countOccurence(ele)



# def CountOcc(list):
#     d={}
#     for i in list :
#         if i in d.keys():
#             d[i]+=1
#         else:
#             d[i]=1
#      print(d)
# list=[10,29,20,10,20,102,39,10,20]
#
# CountOcc(list)


#
# from collections import Counter
# list=[10,29,20,10,20,102,39,10,20]
# dict1= Counter(list)
# print(dict1)
