# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum
def returnSum(dict):
    sum = 0
    for i in dict.keys():
        if type(i)==type(1) :
          sum = sum + i

    return sum



dict = {1: 100, 3: 200, 6: 300}
print("Sum :", returnSum(dict))