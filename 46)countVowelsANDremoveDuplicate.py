def fun(str):
    # rmdupli = ''.join(set(str))
    # print(type(rmdupli))
    # print(rmdupli)
    l2 = []
    l1 = list(str)
    for i in l1:
        if i not in l2 :
            l2.append(i)
    str1=''.join(l2)
    print(str1)

    vowels = set('aeiouAEIOU')
    print(vowels)
    count1 = 0
    for i in str:
        if i in vowels:
            count1 = count1 + 1

    print(count1)
str = input('enter string : -')
fun(str)
