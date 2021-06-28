class ListOp:
    def __init__(self,list1):
        self.list1=list1
    def sum1(self):
        sum_l=0
        for i in self.list1:
            sum_l += i
        print('sum of the all element in list :- ',sum_l)


    def sum_recursion(self):

        def sum_recursion_A(list):
           sum_l1=0
           if len(list)>0:
               sum_l1=sum_l1 + list[0]+ sum_recursion_A(list[1:])
           return sum_l1
        return sum_recursion_A

    def Mult(self):
        mult=1
        for i in self.list1:
            mult *= i
        print(mult)
    def Mult_Recursion(self):

         def mult_RE(list):
             mult = 1
             if len(list)>0:
                 mult = mult * list[0] * mult_RE(list[1:])
             return mult
         return mult_RE
    def Smallest_ele(self):
        smallest = self.list1[0]
        for i in self.list1:
            if i < smallest:
                smallest = i
        print( 'smallest no in the list is :-',smallest)

    def Largest_ele(self) :
        largest = self.list1[0]
        for i in self.list1 :
            if i > largest :
                largest = i
        print('largest element in list :- ',largest)
    def Second_lg_ele(self) :
        largest1 = self.list1[0]
        largest2 = self.list1[1]
        for i in self.list1 :
            if i > largest1 and i > largest2 :
                c = largest1
                largest1 = i
                largest2 = c
            elif i > largest1 :
                d = largest1
                largest1 = i
                largest2 = d
            elif i > largest2 :
                e = largest2
                largest2 = i
                largest1 = e
            if largest1 < largest2 :
                large = largest1
                largest1 = largest2
                largest2 = large
        print("second largest element in list :-",largest2)
    def Second_lg_ele1(self):

        mx = max(self.list1[0], self.list1[1])
        secondmax = min(self.list1[0],self.list1[1])
        n = len(self.list1)
        for i in range(2, n):
            if self.list1[i] > mx:
                secondmax = mx
                mx = self.list1[i]
            elif self.list1[i] > secondmax and mx != self.list1[i] :
                secondmax = self.list1[i]

        print("Second highest number is : ",secondmax)







list=[1,2,3,4,5,6]
l=ListOp(list)
l.sum1()
s=l.sum_recursion()
print(s(list))
l.Mult()
m=l.Mult_Recursion()
print(m(list))
l.Smallest_ele()
l.Largest_ele()
l.Second_lg_ele()
l.Second_lg_ele1()