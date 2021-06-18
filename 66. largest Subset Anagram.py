#python counter to find size of largest subset of anagram words.




# what is anagram:

# An anagram is a word or phrase formed by rearranging the letters 
# of a different word or a phrase,typically using all the originl letters exactly once

# Example: silent : listen 










# from collections import Counter
# def check(s):
# 	lst = s.split()
# 	print(lst)
# 	for i in range(0,len(lst)):
# 		lst[i] = ''.join(sorted(lst[i]))
# 	print(lst)

# 	d = Counter(lst)
# 	print(d)
# 	print(max(d.values()))
		



# s = "top pot listen silent agenta magneta magneta  "
# check(s)














# from collections import Counter
# def largestana(str1):
# 	str1 = str1.split(" ")
# 	print(str1)
# 	for i in range(0,len(str1)):
# 		str1[i] = ''.join(sorted(str1[i]))
# 	print(str1)

# 	newstr1 = Counter(str1)
# 	print(newstr1)
# 	print("The size of largest subset of Anagram word is:",max(newstr1.items()))
		


# #Driver program

# if __name__ == '__main__':
#     str1 = input("Enter the string:")
# largestana(str1)	
















# def largestAnagramSet(arr, n) :
 
#     maxSize = 0
#     count = {}
 
#     for i in range(n) :
 
       
#         arr[i] = ''.join(sorted(arr[i]))
 
     
#         if arr[i] in count :
#             count[arr[i]] += 1
#         else :
#             count[arr[i]] = 1
 
      
#         maxSize = max(maxSize, count[arr[i]])
 
#     return maxSize
 

# arr = [ "ant", "magneta", "magnate", "atn", "gnamate" ]
# n = len(arr)
# print(largestAnagramSet(arr, n))
 
# arr1 = [ "cars", "bikes", "arcs", "steer" ]
# n = len(arr1)
# print(largestAnagramSet(arr1, n))
 
