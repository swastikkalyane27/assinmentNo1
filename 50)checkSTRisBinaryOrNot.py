str1 = input('enter string : - ')
def checkStr(str1) :
    s = '01'
    count = 0
    for ch in str1 :
        if ch not in s :
            count = 1
            break
        else :
            pass
    if count :
        print('given inpute string is not binary')
    else :
        print('given inpute string is binary')
checkStr(str1)


def checkstr1(str1):
    str2 = set(str1)
    s1 = {'1','0'}
    if str2 == s1 or str2 == {'0'} or str2 =={'1'} :
        print('yes, given inpute string is binary')
    else :
        print('no,given inpute string is not binary')
checkstr1(str1)
