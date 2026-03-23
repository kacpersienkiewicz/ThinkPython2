'''
Exercise 9.1. Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).
'''

fin = open('Ch9\\words.txt')
for line in fin:
    if len(line) > 20:
        print(line)
    else:
        continue