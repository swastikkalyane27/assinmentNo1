# Python code to replace, with . and vice-versa
# maketrans: This static method returns a translation table usable for str.translate(). This builds a translation table,
# which is a mapping of integers or characters to integers, strings, or None.

# translate: This returns a copy of the string where all characters occurring in the optional argument are removed,
# and the remaining characters have been mapped through the translation table, given by the maketrans table.



def Replace(str1):
    maketrans = str1.maketrans
    print(maketrans)
    final = str1.translate(maketrans(', .', '., '))
    return final


# Driving Code
string = "14, 625, 498.002"
print(Replace(string))




# using Replace
# This is more of a logical approach in which we swap the symbols considering third variables.
# The replace method can also be used to replace the methods in strings. We can convert “, ” to a symbol
# then convert “.” to “, ” and the symbol to “.”.

# def Replace(str1):
#     str1 = str1.replace(', ', 'third')
#     str1 = str1.replace('.', ', ')
#     str1 = str1.replace('third', '.')
#     return str1
#
#
# string = "14, 625, 498.002"
# print(Replace(string))
