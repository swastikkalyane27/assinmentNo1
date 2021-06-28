# def RotateArray(list,n,d):
#    temp = []
#    i = 0
#    while i < d:
#        temp.append(list[i])
#        i +=1
#    i = 0
#    while d < n :
#        list[i] = list[d]
#        i
#  += 1
#        d += 1
#    list[:] = list[:i]+temp
#    return list
#
# list = [1,3,2,4,5,6,7,8,9]
# print((RotateArray(list,len(list),2)))
#
#



arr = [1, 2, 3, 4, 5];
# n determine the number of times an array should be rotated
n = 3;

# Displays original array
print("Original array: ");
for i in range(0, len(arr)):
    print(arr[i],end=' ')

# Rotate the given array by n times toward left
for i in range(0, n):
    # Stores the first element of the array
    first = arr[0];

    for j in range(0, len(arr) - 1):
        # Shift element of array by one
        arr[j] = arr[j + 1];

        # First element of array will be added to the end
    arr[len(arr) - 1] = first;

print();

# Displays resulting array after rotation
print("Array after left rotation: ");
for i in range(0, len(arr)):
    print(arr[i],end =' ')
print()

arr=[1,2,3,4,5]

n=3
for i in range (0,n):
    temp=arr[0]
    for k in range (0,len(arr)-1):
        arr[k]=arr[k+1]
    arr[len(arr)-1]=temp

print(arr)