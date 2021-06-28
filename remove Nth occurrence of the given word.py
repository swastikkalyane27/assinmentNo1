def removeNth(list,ele,n1):
    l1=[]
    count=0
    for i in list:
        if i==ele:
            count+=1
            if count!=n1:
                l1.append(i)
        else:
            l1.append(i)
    return  l1
list=[10,20,20,39,30,40,20,39,20]
ele=20
n1=3
print(removeNth(list,ele,n1))

#
def rmNth(list,ele,n):
    count = 0
    for i in list:
        if i == ele:
            count += 1
            if count == n:
                list.remove(i)
    return list

list = [10,20,20,39,30,40,20,39,20]
ele = 20
n = 2
print(rmNth(list,ele,n))