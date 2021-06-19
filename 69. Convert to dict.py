#Python Convert a list of Tuples into Dictionary:






# x = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# result = dict(x)
# print(result)












# tuples = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# results = {}
# for (key,value) in tuples:
# 	results.setdefault(key,[]).append(value)

# print(results)	












# def Convert(tuple,dict):
# 	for key,value in tuple:
# 		dict.setdefault(key, []).append(value)
# 	return dict
	
# tuples = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# dictionary = {}
# print(Convert(tuples,dictionary))		













def Convert(tuple,dict1):
	dict1 = dict(tuple)
	return dict1

tuples = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
dictionary = {}
print(Convert(tuples,dictionary))	











# print(dict([('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]))

