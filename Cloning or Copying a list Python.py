# Cloning or Copying a list Python
def copylist(list):
    newlist=[]
    newlist = list.copy()
    # newlist.pop()
    # # list.append(10)
    # list[6].append(10)
    # list[6].pop()
    # print(list)
    print(newlist)
list=[10,20,30,39,47,37,[38,49,32],37]
copylist(list)

newlist =[ i for i in list]
print(newlist)
l1 =[]
l1.extend(list)
print(l1)
