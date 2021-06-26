## Python | Permutation of a given string using inbuilt function

# Function to find permutations of a given string
# from itertools import permutations
# def allPermutations(str):
#     # Get all permutations of string 'ABC'
#     permList = permutations(str)
#
#     # print all permutations
#     for perm in list(permList):
#         print(''.join(perm))
#
# # Driver program
# if __name__ == "__main__":
#     str = 'ABC'
#     allPermutations(str)




# from itertools import permutations
# import string
#
# s = "GEEK"
# a = string.ascii_letters
# print(a)
# p = permutations(s)
# print(p)
#
# # Create a list
# d = []
# for i in list(p):
# 	# Print only if not in list
# 	if (i not in d):
# 		d.append(i)
# 		print(''.join(i))






# Python code to demonstrate
# to find all permutation of
# a given string

#Initialising string
ini_str = "abc"

# Printing initial string
print("Initial string", ini_str)
# print(list(ini_str))
# Finding all permutation
result = []

def permute(data, i, length):
	if i == length:
		result.append(''.join(data) )
	else:
		for j in range(i, length):
			# swap
			data[i], data[j] = data[j], data[i]
			permute(data, i + 1, length)
			data[i], data[j] = data[j], data[i]
permute(list(ini_str), 0, len(ini_str))

# Printing result
print("Resultant permutations", str(result))





def permutations(remaining, candidate=""):
    if len(remaining) == 0:
        print(candidate)

    for i in range(len(remaining)):
        newCandidate = candidate + remaining[i]
        newRemaining = remaining[0:i] + remaining[i + 1:]

        permutations(newRemaining, newCandidate)

s = "ABC"
permutations(s)








## Iterative function to generate all permutations of a string in Python
def permutations(s):
    # create a list to store (partial) permutations
    partial = []

    # initialize the list with the first character of the string
    partial.append(s[0])

    # do for every character of the specified string
    for i in range(1, len(s)):

        # consider previously constructed partial permutation one by one

        # iterate backward
        for j in reversed(range(len(partial))):

            # remove the current partial permutation from the list
            curr = partial.pop(j)

            # Insert the next character of the specified string into all
            # possible positions of current partial permutation.
            # Then insert each of these newly constructed strings into the list

            for k in range(len(curr) + 1):
                partial.append(curr[:k] + s[i] + curr[k:])

    print(partial, end='')


if __name__ == '__main__':
    s = "ABC"
    permutations(s)
