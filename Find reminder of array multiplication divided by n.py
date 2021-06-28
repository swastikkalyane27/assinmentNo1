def reminder(a,n):
    mult=1
    for i in a:
        mult=mult*(i)

    return mult %  n
a=[11,22,33,44,55,66,77,88]
n=13
print(reminder(a,n))
