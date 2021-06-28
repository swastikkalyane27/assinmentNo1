'''python dictionary, set and counter to check if frequencies can become same Scraping And
Finding Ordered Words In A Dictionary using Python Possible Words using given characters in
Python '''
# to check frequencies of all ch are same or not by using counter


from collections import Counter
def check_all_same(my_input):
   my_dict = Counter(my_input)   #convert into dict ch as keys and there frequencies as value by using counter fun()
   input_2 = list(set(my_dict.values()))  # values of dict converted into set and again list (set remove all duplicates)
   if len(input_2) >= 2:
      print('The frequencies are not same')
   # elif len (input_2)==2 and input_2[1]-input_2[0]>1:
   #    print('The frequencies are not same')
   else:
      print('The frequencies are same')

my_str = 'xyz'
print("The string is :")
print(my_str)
check_all_same(my_str)