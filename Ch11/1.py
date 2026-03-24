'''
Exercise 11.1. Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn't matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary.
If you did Exercise 10.10, you can compare the speed of this implementation with the list in operator
and the bisection search.
'''

fin = open('Ch9\\words.txt')

def file_to_dict(file):
    file_dict = {}
    for line in file:
        word = line.strip()
        file_dict[word] = word
    return file_dict

file_dict = file_to_dict(fin)
print(file_dict)
print('absorb' in file_dict) # Pretty fast