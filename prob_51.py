## Python | Find all close matches of input string from a list

l1 = ["lion","li","tiger","ti"]
element = "lion"
for string in l1:
    if string.startswith(element) or element.startswith(string):
        print(string,end=" ")


# from difflib import get_close_matches
# word = 'banana'
# patterns = ['ana', 'nana', 'ban', 'ran','tan']
# print('matched words:',get_close_matches(word, patterns))