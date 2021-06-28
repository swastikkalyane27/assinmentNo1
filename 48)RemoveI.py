def rmstrIth(str1,i) :
    a = str1 [: i]
    b = str1 [i+1 : ]
    # str2 = str1.replace(str1[i],"",1)
    # print(str2)
    return a + b
print(rmstrIth('hello my boy',2))

