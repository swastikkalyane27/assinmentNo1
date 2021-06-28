# 13. Python program to remove Nth occurrence of the given word 
# 14. Python | Ways to find length of list
# 15. Python | Ways to check if element exists in list
# 16. Different ways to clear a list in Python
# 17. Python | Reversing a List Python
class ListOp:
    def __init__(self,list):
        self.list=list
    def findlen(self):
        x=len(self.list)
        print(x)
    def findlen2(self):
        count=0
        for i in self.list:
            count+=1
        print(count)
    def Ele_exists(self,ele):

        if ele in self.list:
            print("element exists in list")
        else:
            print('element not in list')

    def Ele_exists1(self,ele):
        count=0
        for i in self.list:
            if i == ele:
                count+=1
                break
        if count == 1:
                   print('element exists in list')
        else:
                   print('element not in list')
    def clearList(self):
        self.list.clear()
        print(self.list)
    def clearList1(self):
        for i in range(len(self.list)):
            self.list.pop()
        print(self.list)
    def Reverse(self):
        print(self.list[::-1])
    def Reverse1(self):
        newlist=[]
        for i in reversed(self.list):
            newlist.append(i)
        print(newlist)
    def Reverse2(self):
        newlist=[]
        i=len(self.list)
        while i>0:
            newlist.append(self.list[i-1])
            i-=1
        print(newlist)

    def rmNth(self, ele, n):
        count = 0
        for i in range(len(self.list)-1):
            if self.list[i] == ele:
                count += 1
                if count == n:
                    self.list.pop(i)
        print(self.list)
    def rmNth1(self,ele,n):
        newlist = []
        count = 0
        for i in self.list:
            if i == ele:
                count += 1
                if count != n :
                    newlist.append(i)
            else:
                newlist.append(i)
        print(newlist)


list=[10,29,20,30,20,30,40,20,302,20]
a=ListOp(list)
# a.findlen()
# a.findlen2()
# a.Ele_exists(29)
# a.Ele_exists1(232)
# a.Reverse()
# a.Reverse1()
# a.Reverse2()
# a.rmNth(20,2)
# a.rmNth1(20,2)
# # a.clearList()
# a.clearList1()
# print(a.list)