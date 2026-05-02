'''
As usual, you should at least attempt the exercises before you read my solutions.
Exercise 13.1. Write a program that reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
Hint: The string module provides a string named whitespace, which contains space, tab, new-
line, etc., and punctuation which contains the punctuation characters. Let’s see if we can make
Python swear:
>>> import string
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
Also, you might consider using the string methods strip, replace and translate.
'''
# This program breaks each line into its words and each element in the final list is a line in the original file.

import string
txt = open('Ch13\\text.txt', 'r')
lines = []

for line in txt:
    line = line.lower().strip()
    for char in string.punctuation:
        line = line.replace(char, '')
    line = line.split()
    lines.append(line)

print(lines)