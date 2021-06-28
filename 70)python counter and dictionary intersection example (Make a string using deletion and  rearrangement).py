'''Python code to find if we can make first string
from second by deleting some characters from
second and rearranging remaining characters.'''
from collections import Counter
def func(str1,str2):
    dict1 = Counter(str1)
    dict2 = Counter(str2)
    result = dict1 & dict2  # intersection of dict1 and dict2
    if result == dict1:
        print('possible')
    else:
        print('not possible')
func('xxyyzz','xxxxyyyyzz')