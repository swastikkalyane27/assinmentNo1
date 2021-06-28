l1 = [1,2,(1,2),('hello','swastik'),(),4,5,[10,20,21],'raj','etc',(),[]]
def fun(l1):
    for i in l1 :
        if type(i) == type(()) and len(i) == 0:
        # if i == ():
             l1.remove(i)
        else :
            continue
    return l1
print(fun(l1))


l2 = filter(None,l1)  # empty list and empty touple will be removed by using filter with None function
for i in l2:
    print(i , end=',')
