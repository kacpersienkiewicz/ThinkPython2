'''
Exercise 3.1. Write a function named right_justify that takes a string named s as a parameter
and prints the string with enough leading spaces so that the last letter of the string is in column 70
of the display.
>>> right_justify('monty')
monty
Hint: Use string concatenation and repetition. Also, Python provides a built-in function called len
that returns the length of a string, so the value of len('monty') is 5.

'''

def right_justify(word: str):
    offset = len(word)
    right_justified_text = ' ' * (column_space - offset) + word
    print(right_justified_text)

def center_justify(word):
    offset = len(word)
    if offset % 2 == 0:
        center_justified_text = ' ' * ((column_space - offset) // 2) + word + ' ' * ((column_space - offset) // 2)
    else:
        offset -= 1
        center_justified_text = ' ' * ((column_space - offset) // 2) + word + ' ' * ((column_space - offset) // 2)
    print(center_justified_text)

column_space = 70

right_justify('monty')
right_justify('Supercalifragilisticexpialidocious')
center_justify('monty')
center_justify('Supercalifragilisticexpialidocious')