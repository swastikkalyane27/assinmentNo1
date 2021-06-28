from operator import itemgetter
# str_comment = ['python','yeah','am','hello']
# print(sorted(str_comment))   #sorted by default accourding to lexicographic order
# print(sorted(str_comment, key=len))   #sorted accourding to length of comment
# print(sorted(str_comment, key=len,reverse=True))   #sorted accourding to length of comment in reverse order
#
# #
# list1 = [("Andini",(1,2,5,4), 18),
#        ("Manjeet",(4,5,1,2), 20 ),
#        ("Nikhil" , (7,1,2,38),19 )]
# print(sorted(list1))   #sorted by default accourding to lexicographic order
# print(sorted(list1,key=itemgetter(1)))   # sort accourding to 2 index if every element in list
# print(sorted(list1,key=itemgetter(1),reverse=True))   # sort accourding to 2 index if every element in list
#  # also we can do by use lamda function             #  in reverse order
# print(sorted(list1,key=lambda x:x[1][1]))
#
# list2 = [{ "name" : "Nandini", "age" : 18},
# { "name" : "Manjeet", "age" : 20 },
# { "name" : "Nikhil" , "age" : 19 }]
# print(sorted(list2,key=itemgetter('age')))     #aslo bye using lamda x:x['age"]
# print(sorted(list2,key=lambda x:x['age']))     #aslo bye using lamda x:x['age"]

# Python code demonstrate the working of sorted()
# and itemgetter

# importing "operator" for implementing itemgetter
from operator import itemgetter

# Initializing list of dictionaries
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

# using sorted and itemgetter to print list sorted by age
# print ("The list printed sorting by age: ")
# print (sorted(lis, key=itemgetter('age')))          #sort accourdind to age

print ("\r")

# using sorted and itemgetter to print list sorted by both age and name
# notice that "Manjeet" now comes before "Nandini"
print ("The list printed sorting by age and name: ")
print (sorted(lis, key=itemgetter('age', 'name')))

print ("\r")

# using sorted and itemgetter to print list sorted by age in descending order
# print ("The list printed sorting by age in descending order: ")
# print (sorted(lis, key=itemgetter('age'),reverse = True))
#
#
#
